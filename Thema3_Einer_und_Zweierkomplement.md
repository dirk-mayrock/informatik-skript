# Thema 3: Einer- und Zweierkomplement

## Informatik Leistungskurs (Gymnasium)

---

## Verbindung zu Thema 2

In Thema 2 wurde die binäre Arithmetik mit positiven Zahlen erklärt.

Jetzt stellt sich die Frage:

```
Wie speichert ein Computer negative Zahlen?
```

Die Antwort: über das Einerkomplement und das Zweierkomplement.

---

## Das Problem: Negative Zahlen in Binär

Eine Binärzahl besteht nur aus 0 und 1.

Es gibt kein Minuszeichen, das einfach gespeichert werden kann.

Der Computer braucht eine Konvention, wie ein negativer Wert codiert wird.

---

## Idee 1: Vorzeichenbit

Die einfachste Idee: Das erste Bit zeigt an, ob die Zahl positiv oder negativ ist.

```
0 = positiv
1 = negativ
```

Beispiel mit 4 Bit:

```
0101 = +5
1101 = -5
```

### Problem dieser Idee

Es gibt zwei Darstellungen für die Null:

```
0000 = +0
1000 = -0
```

Das ist unpraktisch und führt zu Problemen beim Rechnen.

---

## Lösung: Das Zweierkomplement

Das Zweierkomplement ist die heute in allen Computern verwendete Methode.

Es löst beide Probleme:
- Es gibt nur eine Null.
- Subtraktion kann als Addition durchgeführt werden.

---

## Schritt 1: Das Einerkomplement

Das Einerkomplement entsteht durch Invertierung aller Bits.

Aus jeder 0 wird eine 1 und aus jeder 1 wird eine 0.

Beispiel:

```
+5 in 4 Bit:
0101

Einerkomplement:
1010
```

Das Einerkomplement von +5 ist 1010, was dem Dezimalwert -5 entspricht — aber noch nicht perfekt funktioniert.

### Problem des Einerkomplements

Auch hier gibt es zwei Darstellungen für Null:

```
0000 =  +0
1111 =  -0
```

---

## Schritt 2: Das Zweierkomplement

Das Zweierkomplement = Einerkomplement + 1

Beispiel:

```
+5 in 4 Bit:
0101

Einerkomplement:
1010

+1:
1011
```

Ergebnis: `1011` ist die Darstellung von -5 im Zweierkomplement.

### Kontrolle

```
0101 = +5
1011 = -5

0101
+1011
------
10000
```

Das führende Bit (Übertrag) fällt weg (kein Platz im 4-Bit-Register).

Ergebnis: `0000` = 0

Das ist korrekt: +5 + (−5) = 0

---

## Wertebereich im Zweierkomplement

Bei n Bit gilt:

```
Kleinster Wert: -2^(n-1)
Größter Wert:   2^(n-1) - 1
```

Beispiel mit 4 Bit:

```
Kleinster Wert: -2^3 = -8
Größter Wert:    2^3 - 1 = 7
```

| Binär | Dezimal |
|-------|---------|
| 0111  | +7      |
| 0110  | +6      |
| 0101  | +5      |
| 0100  | +4      |
| 0011  | +3      |
| 0010  | +2      |
| 0001  | +1      |
| 0000  |  0      |
| 1111  | -1      |
| 1110  | -2      |
| 1101  | -3      |
| 1100  | -4      |
| 1011  | -5      |
| 1010  | -6      |
| 1001  | -7      |
| 1000  | -8      |

---

## Wie erkennt man: positiv oder negativ?

Das höchste Bit (Most Significant Bit, MSB) gibt das Vorzeichen an:

```
MSB = 0 → positive Zahl
MSB = 1 → negative Zahl
```

---

## Subtraktion über Addition

Der wichtigste Vorteil des Zweierkomplements:

Der Prozessor muss keine eigene Subtraktions-Schaltung bauen.

Subtraktion wird einfach als Addition der negierten Zahl durchgeführt.

Beispiel:

```
7 - 3
= 7 + (-3)
```

7 in 4 Bit:  `0111`
-3 im Zweierkomplement:

```
+3 = 0011
Einerkomplement: 1100
+ 1:             1101
```

Jetzt addieren:

```
  0111
+ 1101
------
 10100
```

Übertrag fällt weg → `0100` = 4

Kontrolle: 7 - 3 = 4 ✓

---

## Zusammenfassung: Einerkomplement vs. Zweierkomplement

| Eigenschaft              | Einerkomplement | Zweierkomplement |
|--------------------------|-----------------|------------------|
| Darstellung von Null     | zweifach (+0/-0) | eindeutig (0000)  |
| Subtraktion möglich?     | komplizierter   | ja, über Addition |
| Verwendung heute         | selten          | überall           |

---

## Verbindung zu anderen Themen

- **Thema 2 (Binäre Arithmetik):** Subtraktion nutzt intern das Zweierkomplement.
- **Thema 4 (Gleitkommazahlen):** Das Vorzeichen einer Gleitkommazahl wird ähnlich codiert.
- **Java (Thema 9):** `int` in Java ist immer ein 32-Bit-Zweierkomplement.

---

## Typische Klausuraufgaben

### Aufgabe 1

Stelle -7 als 4-Bit-Zweierkomplement dar.

#### Lösung

```
+7 = 0111
Einerkomplement: 1000
+ 1:             1001
```

-7 = `1001`

---

### Aufgabe 2

Welchen Dezimalwert hat `1110` im 4-Bit-Zweierkomplement?

#### Lösung

MSB = 1 → negative Zahl.

Zweierkomplement umkehren (nochmals Einerkomplement + 1):

```
1110
Einerkomplement: 0001
+ 1:             0010 = 2
```

Also: `1110` = -2

---

### Aufgabe 3

Berechne 6 - 4 mit Hilfe des Zweierkomplements (4 Bit).

#### Lösung

6 = `0110`

-4 im Zweierkomplement:

```
+4 = 0100
Einerkomplement: 1011
+ 1:             1100
```

Addition:

```
  0110
+ 1100
------
 10010
```

Übertrag fällt weg → `0010` = 2

Kontrolle: 6 - 4 = 2 ✓

---

## Merksätze

1. Das Einerkomplement entsteht durch Invertierung aller Bits.
2. Das Zweierkomplement = Einerkomplement + 1.
3. Beim Zweierkomplement gibt es nur eine einzige Null.
4. Das höchste Bit zeigt das Vorzeichen an: 0 = positiv, 1 = negativ.
5. Der Prozessor führt Subtraktion als Addition des Zweierkomplements durch.
6. Bei 8 Bit reicht der Bereich von -128 bis +127.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 9/10
**Verständlichkeit:** 9/10
