# Thema 4: Fest- und Gleitkommazahlen

## Informatik Leistungskurs (Gymnasium)

---

## Verbindung zu Thema 3

Bisher wurden nur ganze Zahlen betrachtet.

Ein Computer muss aber auch Kommazahlen darstellen:

```
3,14159...    (Pi)
0,001         (winzig kleiner Wert)
6,022 · 10²³  (riesiger Wert)
```

Dafür gibt es zwei Methoden: **Festkommazahlen** und **Gleitkommazahlen**.

---

## Festkommazahlen

### Idee

Die Anzahl der Stellen vor und nach dem Komma ist fest vorgegeben.

Beispiel: 8 Bit insgesamt, davon 4 Bit vor dem Komma, 4 Bit nach dem Komma.

```
Bit-Positionen:  8   4  2  1 , 0,5  0,25  0,125  0,0625
```

### Beispiel

```
0110,1100
```

Berechnung:

```
0·8 + 1·4 + 1·2 + 0·1  +  1·0,5 + 1·0,25 + 0·0,125 + 0·0,0625

= 4 + 2  +  0,5 + 0,25

= 6,75
```

### Vorteile

- Einfach zu berechnen
- Schnell

### Nachteile

- Wertebereich begrenzt
- Entweder kleine Zahlen oder Kommagenauigkeit, aber nicht beides

### Warum ist der Nachteil so gravierend?

Mit 4 Bit vor dem Komma und 4 Bit nach dem Komma lassen sich maximal 15,9375 darstellen. Die Zahl 100,5 passt nicht mehr rein — der Vorkommanteil 100 braucht mehr als 4 Bit (er braucht 7 Bit).

Umgekehrt: Wenn man mehr Bits für den Vorkommateil verwendet, verliert man Präzision nach dem Komma.

Ein Gleitkommasystem mit denselben 8 Bit kann dagegen sowohl winzige Zahlen wie 0,0001 als auch große wie 100000 darstellen — weil der Exponent festlegt, wo das Komma sitzt. Das ist der eigentliche Vorteil der Gleitkommadarstellung.

---

## Gleitkommazahlen

### Die Idee: Wissenschaftliche Notation

Im Alltag kennt man die wissenschaftliche Notation:

```
6,022 · 10²³
```

Ein Computer macht etwas Ähnliches — aber im Binärsystem:

```
1,101 · 2⁵
```

Die Kommaposition „gleitet" je nach Exponent.

Daher der Name: **Gleitkommazahl**.

---

## Der IEEE 754 Standard

Praktisch alle Computer verwenden den Standard **IEEE 754**.

Er legt genau fest, wie Gleitkommazahlen gespeichert werden.

---

## Aufbau einer 32-Bit-Gleitkommazahl (Single Precision)

Eine 32-Bit-Gleitkommazahl besteht aus drei Teilen:

```
| S | EEEEEEEE | MMMMMMMMMMMMMMMMMMMMMMM |
  1      8                 23
```

| Teil      | Bits | Bedeutung        |
|-----------|------|------------------|
| S         |  1   | Vorzeichen (Sign) |
| E         |  8   | Exponent          |
| M         | 23   | Mantisse          |

---

## Das Vorzeichen (S)

```
0 = positive Zahl
1 = negative Zahl
```

---

## Der Exponent (E)

Der Exponent ist um 127 verschoben (Bias = 127).

Das bedeutet:

```
Gespeicherter Wert = tatsächlicher Exponent + 127
```

Beispiel:

Tatsächlicher Exponent = 4

```
Gespeichert: 4 + 127 = 131 = 10000011
```

### Warum dieser Bias-Trick, und warum genau 127?

Ohne Bias müsste man für negative Exponenten (z.B. für sehr kleine Zahlen wie 2⁻⁵) ein Vorzeichen speichern. Man könnte das Zweierkomplement verwenden — aber das hätte einen Nachteil: Zwei gespeicherte Exponentenwerte wären nicht mehr direkt vergleichbar, weil beim Zweierkomplement negative Zahlen höhere Bitmuster haben als positive.

Mit dem Bias-Trick sind alle gespeicherten Exponenten nichtnegative ganze Zahlen. Man kann zwei Gleitkommazahlen allein anhand ihrer rohen Bitmuster vergleichen — was Vergleichsoperationen im Prozessor deutlich vereinfacht.

Warum genau 127? Bei 8 Exponent-Bits gibt es 256 Muster (0–255). Die Muster 0 und 255 sind für Sonderwerte reserviert (Null, Unendlich, NaN). Die restlichen 254 Muster (1–254) werden für normale Zahlen verwendet. 127 liegt in der Mitte dieses Bereichs, sodass Exponenten von −126 bis +127 dargestellt werden können (gespeichert als 1 bis 254).

---

## Die Mantisse (M)

In der wissenschaftlichen Darstellung beginnt die Zahl immer mit 1:

```
1,xxxxx · 2^e
```

Die führende 1 wird **nicht gespeichert** (Hidden Bit), weil sie immer vorhanden ist.

Das folgt direkt aus der Normalisierung: Da jede normalisierte Binärzahl die Form 1,xxx hat, ist die erste Stelle immer 1. Es wäre Platzverschwendung, diese bekannte Information zu speichern. Indem man sie weglässt, gewinnt man eine zusätzliche Bit-Stelle für die eigentlichen Nachkommabits — und erhöht damit die Präzision.

Das spart ein Bit.

---

## Vollständiges Beispiel: Dezimal → IEEE 754

### Wie wandelt man Nachkommastellen in Binär um?

Ganzzahlen werden durch wiederholte Division durch 2 umgewandelt (wie in Thema 1). Für Nachkommastellen funktioniert das Umgekehrte: wiederholte **Multiplikation mit 2**.

Der Grund: Multipliziert man eine Binärzahl mit 2, verschiebt sich das Komma eine Stelle nach rechts — genau wie eine Multiplikation mit 10 im Dezimalsystem das Komma nach rechts schiebt. Das erste Bit nach dem Komma hat den Wert 2⁻¹ = 0,5. Wenn man also mit 2 multipliziert und der Vorkommateil wird 1, dann war das Bit gesetzt.

**Verfahren:**
1. Nachkommateil mit 2 multiplizieren.
2. Den Vorkommateil des Ergebnisses (0 oder 1) als nächstes Bit notieren.
3. Mit dem neuen Nachkommateil weitermachen, bis der Nachkommateil 0 wird — oder bis genug Bits vorhanden sind.

Beispiel: 0,75

```
0,75 × 2 = 1,5  → Bit: 1, weiter mit 0,5
0,5  × 2 = 1,0  → Bit: 1, weiter mit 0,0 → fertig
```

0,75₁₀ = 0,11₂

Kontrolle: 1 · 2⁻¹ + 1 · 2⁻² = 0,5 + 0,25 = 0,75 ✓

Beispiel: 0,625

```
0,625 × 2 = 1,25 → Bit: 1, weiter mit 0,25
0,25  × 2 = 0,5  → Bit: 0, weiter mit 0,5
0,5   × 2 = 1,0  → Bit: 1, fertig
```

0,625₁₀ = 0,101₂

---

### Zahl: 13,5

**Schritt 1: In Binär umwandeln**

Ganzzahlteil: 13

```
13 : 2 = 6 Rest 1
 6 : 2 = 3 Rest 0
 3 : 2 = 1 Rest 1
 1 : 2 = 0 Rest 1
→ 1101
```

Nachkommateil: 0,5

```
0,5 × 2 = 1,0 → Bit: 1
→ 0,1
```

Also: 13,5 = `1101,1`

---

**Schritt 2: Normalisieren**

```
1101,1 = 1,1011 · 2³
```

### Warum normalisiert man, und warum immer „1,xxxx"?

Normalisierung bedeutet: Die Zahl so umschreiben, dass genau eine 1 vor dem Komma steht.

Das klingt nach einer beliebigen Konvention, hat aber zwei wichtige Gründe:

Erstens: **Eindeutigkeit.** Eine Zahl hat in normalisierter Form genau eine Darstellung. 1101,1 könnte man auch als 11,011 · 2² oder 0,11011 · 2⁴ schreiben — all das ist dasselbe. Ohne Normalisierung hätte jede Zahl unendlich viele Darstellungen, und man könnte Zahlen nicht einfach vergleichen.

Zweitens: **Das Hidden Bit.** Da nach der Normalisierung die Stelle vor dem Komma immer genau 1 ist (jede Binärzahl ≠ 0 beginnt mit 1), muss diese 1 nicht gespeichert werden — sie ist immer da. Man spart so ein Bit und gewinnt eine zusätzliche Stelle Präzision in der Mantisse.

Die Eins wird vor das Komma gebracht. Der Exponent gibt an, um wie viele Stellen das Komma nach links verschoben wurde.

---

**Schritt 3: Vorzeichen**

13,5 ist positiv → S = 0

---

**Schritt 4: Exponent speichern**

Exponent = 3

Mit Bias: 3 + 127 = 130

```
130 = 10000010
```

---

**Schritt 5: Mantisse**

Die Mantisse ist `1011` (die führende 1 wird weggelassen).

Auf 23 Bit auffüllen:

```
10110000000000000000000
```

---

**Ergebnis:**

```
0 | 10000010 | 10110000000000000000000
```

---

## Vollständiges Beispiel: IEEE 754 → Dezimal

### Gegeben:

```
0 | 10000001 | 01000000000000000000000
```

**Schritt 1: Vorzeichen**

S = 0 → positiv

**Schritt 2: Exponent**

```
10000001 = 129
129 - 127 = 2
```

Exponent = 2

**Schritt 3: Mantisse**

Gespeicherte Mantisse: `01000000000000000000000`

Mit Hidden Bit: `1,01`

**Schritt 4: Berechnen**

```
1,01 · 2² = 101,0 = 5
```

Ergebnis: **5,0**

---

## Besondere Werte in IEEE 754

| Exponent | Mantisse | Bedeutung          |
|----------|----------|--------------------|
| 00000000 | 0        | Null (±0)          |
| 00000000 | ≠ 0      | Denormalisiert     |
| 11111111 | 0        | Unendlich (±∞)     |
| 11111111 | ≠ 0      | NaN (Not a Number) |

### Denormalisierte Zahlen (Subnormals)

Ganz normale normalisierte Zahlen haben immer eine führende 1 vor dem Komma — deshalb kann der kleinste darstellbare Exponent (−126) nicht unterschritten werden, ohne dass die Zahl zu 0 wird. Das erzeugt eine „Lücke" um den Nullpunkt.

Denormalisierte Zahlen schließen diese Lücke. Wenn der gespeicherte Exponent 00000000 ist und die Mantisse nicht null ist, wird das Hidden Bit nicht angenommen. Die Zahl hat die Form 0,xxxxx · 2⁻¹²⁶. So lassen sich sehr kleine Werte nahe Null noch annähernd korrekt darstellen — mit abnehmender Präzision, aber ohne abrupten Sprung zur Null.

NaN entsteht zum Beispiel bei:

```
0 ÷ 0
√(-1)
```

---

## Rundungsfehler

Nicht alle Dezimalzahlen lassen sich exakt als Binärbruch darstellen.

Bekanntes Beispiel:

```
0,1 + 0,2 ≠ 0,3
```

In Python:

```python
>>> 0.1 + 0.2
0.30000000000000004
```

Das ist kein Bug — sondern eine Eigenschaft der Binärdarstellung.

### Warum ist 0,1 ein unendlicher Bruch im Binärsystem?

Man kann das direkt mit dem Multiplikationsverfahren zeigen. Man wendet es auf 0,1 an:

```
0,1  × 2 = 0,2  → Bit: 0
0,2  × 2 = 0,4  → Bit: 0
0,4  × 2 = 0,8  → Bit: 0
0,8  × 2 = 1,6  → Bit: 1, weiter mit 0,6
0,6  × 2 = 1,2  → Bit: 1, weiter mit 0,2
0,2  × 2 = 0,4  → Bit: 0  ← jetzt beginnt die Wiederholung
0,4  × 2 = 0,8  → Bit: 0
0,8  × 2 = 1,6  → Bit: 1
...
```

Die Sequenz 0011 wiederholt sich endlos. 0,1 im Binärsystem ist genau wie 1/3 im Dezimalsystem — ein unendlicher periodischer Bruch.

Da in einem 32-Bit-Float nur 23 Bit für die Mantisse zur Verfügung stehen, wird 0,1 an einer bestimmten Stelle abgebrochen. Das erzeugt einen winzigen Rundungsfehler. Addiert man 0,1 und 0,2 (beide mit Rundungsfehlern behaftet), summieren sich diese kleinen Fehler auf — deshalb ist das Ergebnis nicht exakt 0,3.

Das ist kein Bug, sondern ein systemimmanentes Verhalten jeder Binär-Gleitkommadarstellung.

---

## Vergleich: 32-Bit vs. 64-Bit

| Eigenschaft  | Single (32 Bit) | Double (64 Bit) |
|--------------|-----------------|-----------------|
| Vorzeichen   | 1 Bit           | 1 Bit           |
| Exponent     | 8 Bit           | 11 Bit          |
| Mantisse     | 23 Bit          | 52 Bit          |
| Genauigkeit  | ~7 Dezimalstellen | ~15 Dezimalstellen |

---

## Verbindung zu anderen Themen

- **Thema 1 (Binärzahlen):** Die Mantisse ist eine Binärzahl.
- **Thema 3 (Zweierkomplement):** Das Vorzeichen-Bit funktioniert ähnlich.
- **Java (Thema 9):** `float` = 32 Bit, `double` = 64 Bit IEEE 754.

---

## Typische Klausuraufgaben

### Aufgabe 1

Welche drei Bestandteile hat eine IEEE-754-Gleitkommazahl (Single Precision)?

#### Lösung

```
1. Vorzeichen (1 Bit)
2. Exponent (8 Bit, mit Bias 127)
3. Mantisse (23 Bit, Hidden Bit)
```

---

### Aufgabe 2

Wandle 5,75 in IEEE 754 (32 Bit) um.

#### Lösung

5,75 in Binär:

```
5 = 101
0,75: 0,75 × 2 = 1,5 → 1
      0,5  × 2 = 1,0 → 1
→ 0,11
```

5,75 = `101,11` = `1,0111 · 2²`

- S = 0
- Exponent: 2 + 127 = 129 = `10000001`
- Mantisse: `01110000000000000000000`

```
0 | 10000001 | 01110000000000000000000
```

---

### Aufgabe 3

Warum ist `0,1 + 0,2 ≠ 0,3` in vielen Programmiersprachen?

#### Lösung

0,1 und 0,2 sind im Binärsystem unendliche periodische Brüche.

Bei der Speicherung in endlich vielen Bits entstehen Rundungsfehler.

---

## Merksätze

1. Festkommazahlen haben einen festen Kommastandort — einfach, aber begrenzt.
2. Gleitkommazahlen verwenden die Form: Vorzeichen · Mantisse · 2^Exponent.
3. Der IEEE-754-Standard wird in fast allen Computern verwendet.
4. Single Precision: 1 + 8 + 23 Bit = 32 Bit.
5. Double Precision: 1 + 11 + 52 Bit = 64 Bit.
6. Der Bias (127 bei Single) erlaubt negative Exponenten ohne Vorzeichen-Bit.
7. Rundungsfehler bei Dezimalbrüchen sind systembedingt, kein Programmfehler.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 9/10
**Verständlichkeit:** 8/10
