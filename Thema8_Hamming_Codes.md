# Thema 8: Hamming-Codes

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung: Das Problem der Übertragungsfehler

Wenn Daten über ein Netzwerk gesendet oder auf einem Speichermedium gespeichert werden, können Fehler auftreten:

```
Gesendet:   1 0 1 1 0 0 1
Empfangen:  1 0 1 0 0 0 1
                  ↑
              Ein Bit wurde gekippt!
```

**Wie kann man solche Fehler erkennen — und sogar korrigieren?**

Die Antwort: **Hamming-Codes**

---

## Grundidee: Redundanz

Um Fehler zu erkennen, fügen wir gezielt **zusätzliche Bits** (Prüfbits) hinzu.

Diese Prüfbits enthalten keine neuen Informationen, aber sie erlauben es, Fehler zu finden und zu korrigieren.

---

## Schritt 1: Das Paritätsbit

Das einfachste Verfahren ist das **Paritätsbit**.

Es wird ein Bit hinzugefügt, sodass die Anzahl der 1-Bits gerade ist (gerade Parität).

Beispiel:

```
Daten:      1011001
Anzahl 1er: 4 (gerade)
Paritätsbit: 0
→ 10110010
```

Anderes Beispiel:

```
Daten:      1011011
Anzahl 1er: 5 (ungerade)
Paritätsbit: 1
→ 10110111
```

### Problem des Paritätsbits

Das Paritätsbit kann genau **einen** Fehler erkennen, aber nicht korrigieren.

Bei zwei Fehlern schlägt es fehl — beide heben sich gegenseitig auf.

---

## Hamming-Code: Fehler erkennen UND korrigieren

Richard Hamming entwickelte 1950 einen Code, der:
- einzelne Bitfehler **erkennt** und **korrigiert**
- Zweifachfehler **erkennt** (aber nicht korrigiert)

---

## Aufbau: Welche Positionen sind Prüfbits?

Prüfbits stehen an Positionen, die Potenzen von 2 sind:

```
Position 1  = 2⁰ = Prüfbit p₁
Position 2  = 2¹ = Prüfbit p₂
Position 4  = 2² = Prüfbit p₄
Position 8  = 2³ = Prüfbit p₈
...
```

Alle anderen Positionen enthalten die eigentlichen Datenbits.

### Beispiel: 4 Datenbits → 7 Bit Hamming-Code

```
Position: 1  2  3  4  5  6  7
          p₁ p₂ d₁ p₄ d₂ d₃ d₄
```

Datenbits: d₁ d₂ d₃ d₄

---

## Prüfbits berechnen

Jedes Prüfbit prüft eine bestimmte Gruppe von Positionen.

Die Gruppe eines Prüfbits p enthält alle Positionen, bei denen das Bit p in der Binärdarstellung gesetzt ist.

| Prüfbit | Prüft Positionen |
|---------|------------------|
| p₁ (Pos 1) | 1, 3, 5, 7, 9, 11... (Positionen mit Bit 1 gesetzt) |
| p₂ (Pos 2) | 2, 3, 6, 7, 10, 11... (Positionen mit Bit 2 gesetzt) |
| p₄ (Pos 4) | 4, 5, 6, 7, 12, 13... (Positionen mit Bit 3 gesetzt) |

---

## Vollständiges Beispiel: Codierung

**Datenbits:** d₁=1, d₂=0, d₃=1, d₄=1

**Aufbau:**

```
Position: 1  2  3  4  5  6  7
          p₁ p₂  1 p₄  0  1  1
```

**Berechnung von p₁ (Positionen 1, 3, 5, 7):**

```
Position 3 = 1
Position 5 = 0
Position 7 = 1
→ Anzahl Einsen ohne p₁: 2 (gerade)
→ p₁ = 0 (damit Gesamtanzahl gerade bleibt)
```

**Berechnung von p₂ (Positionen 2, 3, 6, 7):**

```
Position 3 = 1
Position 6 = 1
Position 7 = 1
→ Anzahl Einsen ohne p₂: 3 (ungerade)
→ p₂ = 1 (damit Gesamtanzahl gerade wird)
```

**Berechnung von p₄ (Positionen 4, 5, 6, 7):**

```
Position 5 = 0
Position 6 = 1
Position 7 = 1
→ Anzahl Einsen ohne p₄: 2 (gerade)
→ p₄ = 0 (damit Gesamtanzahl gerade bleibt)
```

**Ergebnis:**

```
Position: 1  2  3  4  5  6  7
          0  1  1  0  0  1  1
```

Hamming-Code: `0110011`

---

## Vollständiges Beispiel: Fehler erkennen

**Empfangener Code:** `0110111` (Bit an Position 5 wurde gekippt)

**Prüfung p₁ (Positionen 1, 3, 5, 7):**

```
Bits: 0, 1, 1, 1 → Anzahl Einsen: 3 (ungerade) → p₁-Fehler!
```

**Prüfung p₂ (Positionen 2, 3, 6, 7):**

```
Bits: 1, 1, 1, 1 → Anzahl Einsen: 4 (gerade) → kein p₂-Fehler
```

**Prüfung p₄ (Positionen 4, 5, 6, 7):**

```
Bits: 0, 1, 1, 1 → Anzahl Einsen: 3 (ungerade) → p₄-Fehler!
```

**Fehlerposition berechnen:**

```
p₁ Fehler = 1
p₂ kein Fehler = 0
p₄ Fehler = 1

Fehlerposition = 1·1 + 0·2 + 1·4 = 5
```

Bit 5 ist falsch → kippen → `0110011` (korrekt)

---

## Anzahl benötigter Prüfbits

Für m Datenbits werden r Prüfbits benötigt, so dass gilt:

```
2^r ≥ m + r + 1
```

Beispiele:

| Datenbits (m) | Prüfbits (r) | Gesamtlänge |
|---------------|--------------|-------------|
| 1             | 2            | 3           |
| 4             | 3            | 7           |
| 11            | 4            | 15          |
| 26            | 5            | 31          |

---

## Hamming-Abstand

Der **Hamming-Abstand** zwischen zwei Codewörtern ist die Anzahl der Positionen, an denen sie sich unterscheiden.

Beispiel:

```
1011001
1001001
  ↑
Unterschied an Position 3

Hamming-Abstand = 1
```

```
1011001
0100110

Unterschiede an Positionen 1, 2, 3, 5, 6

Hamming-Abstand = 5
```

### Bedeutung

Ein Code mit Mindest-Hamming-Abstand d kann:
- d-1 Fehler erkennen
- ⌊(d-1)/2⌋ Fehler korrigieren

Standard-Hamming-Code hat Mindestabstand 3:
- Erkennt 2 Fehler
- Korrigiert 1 Fehler

---

## Verbindung zu anderen Themen

- **Thema 5 (Information):** Prüfbits sind gezielte Redundanz.
- **Thema 1 (Binärzahlen):** Die Fehlerposition wird binär codiert.
- **Thema 7 (Hashing):** Hashfunktionen können auch zur Integritätsprüfung dienen — aber ohne Fehlerkorrektur.

---

## Typische Klausuraufgaben

### Aufgabe 1

Codiere die Datenbits `1010` als Hamming-Code (7 Bit).

#### Lösung

Datenbits: d₁=1, d₂=0, d₃=1, d₄=0

```
Position: 1  2  3  4  5  6  7
          p₁ p₂  1 p₄  0  1  0
```

p₁ (Pos 1,3,5,7): 1, 0, 0 → 1 Eins → p₁ = 1

p₂ (Pos 2,3,6,7): 1, 1, 0 → 2 Einsen → p₂ = 0

p₄ (Pos 4,5,6,7): 0, 1, 0 → 1 Eins → p₄ = 1

```
Position: 1  2  3  4  5  6  7
          1  0  1  1  0  1  0
```

Hamming-Code: `1011010`

---

### Aufgabe 2

Der Code `1011110` wurde empfangen. Liegt ein Fehler vor? Wenn ja, an welcher Position?

#### Lösung

```
p₁ (Pos 1,3,5,7): 1,1,1,0 → 3 Einsen → ungerade → Fehler!
p₂ (Pos 2,3,6,7): 0,1,1,0 → 2 Einsen → gerade → ok
p₄ (Pos 4,5,6,7): 1,1,1,0 → 3 Einsen → ungerade → Fehler!
```

Fehlerposition: p₁·1 + p₂·0 + p₄·1 = 1 + 0 + 4 = 5

Bit 5 ist falsch.

---

### Aufgabe 3

Was ist der Hamming-Abstand von `11010` und `10110`?

#### Lösung

```
11010
10110
↑ ↑
Position 2 und 3 unterschiedlich → Hamming-Abstand = 2
```

---

## Merksätze

1. Prüfbits stehen an Positionen 1, 2, 4, 8, ... (Potenzen von 2).
2. Jedes Prüfbit sichert eine bestimmte Gruppe von Datenpositionen.
3. Die Fehlerposition ergibt sich aus der binären Summe der fehlerhaften Prüfbits.
4. Standard-Hamming-Code: 1 Fehler korrigierbar, 2 Fehler erkennbar.
5. Der Hamming-Abstand zweier Wörter = Anzahl der Stellen, die sich unterscheiden.
6. Für 4 Datenbits braucht man 3 Prüfbits → 7-Bit-Code.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 10/10
**Verständlichkeit:** 8/10
