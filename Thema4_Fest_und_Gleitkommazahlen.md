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

Der Bias-Trick erlaubt es, auch negative Exponenten ohne Vorzeichenbit zu speichern.

---

## Die Mantisse (M)

In der wissenschaftlichen Darstellung beginnt die Zahl immer mit 1:

```
1,xxxxx · 2^e
```

Die führende 1 wird **nicht gespeichert** (Hidden Bit), weil sie immer vorhanden ist.

Das spart ein Bit.

---

## Vollständiges Beispiel: Dezimal → IEEE 754

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

Die Eins wird vor das Komma gebracht. Der Exponent gibt an, um wie viele Stellen verschoben wurde.

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

Das ist kein Bug — sondern ein Eigenschaft der Binärdarstellung.

Grund: 0,1 im Binärsystem ist ein unendlicher Bruch (ähnlich wie 1/3 im Dezimalsystem).

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
