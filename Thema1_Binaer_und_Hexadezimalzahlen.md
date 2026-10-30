# Thema 1: Binärzahlen und Hexadezimalzahlen

# Informatik Leistungskurs (Gymnasium)

## Warum gibt es überhaupt unterschiedliche Zahlensysteme?

Im Alltag benutzen Menschen das Dezimalsystem. Es besitzt zehn verschiedene Ziffern:

```
0 1 2 3 4 5 6 7 8 9
```

Der Grund dafür ist vermutlich einfach: Menschen haben zehn Finger.

Computer besitzen jedoch keine Finger. Ein Computer arbeitet mit elektronischen Bauteilen. Diese Bauteile können sehr zuverlässig zwischen nur zwei Zuständen unterscheiden:

```
Strom aus = 0
Strom an  = 1
```

Deshalb verwendet ein Computer das Binärsystem.

---

## Was ist das Binärsystem?

Das Binärsystem ist ein Zahlensystem mit nur zwei Ziffern:

```
0 und 1
```

Das Wort „Binär“ bedeutet „aus zwei Teilen bestehend“.

Während das Dezimalsystem auf Potenzen von 10 basiert, basiert das Binärsystem auf Potenzen von 2.

### Vergleich

Dezimalsystem:

```
345

= 3 · 10² + 4 · 10¹ + 5 · 10⁰
= 300 + 40 + 5
```

Binärsystem:

```
1101

= 1 · 2³ + 1 · 2² + 0 · 2¹ + 1 · 2⁰
= 8 + 4 + 0 + 1
= 13
```

---

## Warum braucht ein Computer Binärzahlen?

### Grund 1: Zuverlässigkeit

Elektrische Signale sind nie perfekt.

Wenn ein Computer zehn verschiedene Spannungswerte unterscheiden müsste, würden Fehler leicht auftreten.

Beispiel:

```
0,2 Volt
0,4 Volt
0,6 Volt
0,8 Volt
...
```

Kleine Störungen könnten dazu führen, dass eine Zahl falsch erkannt wird.

Bei nur zwei Zuständen ist die Erkennung sehr einfach:

```
unter Schwellwert -> 0
über Schwellwert -> 1
```

Dadurch werden Computer sehr zuverlässig.

### Grund 2: Einfache Hardware

Elektronische Schalter (Transistoren) können leicht zwischen AN und AUS wechseln.

Genau das entspricht:

```
0 = AUS
1 = AN
```

Moderne Prozessoren enthalten Milliarden solcher Transistoren.

### Grund 3: Einfache Berechnungen

Alle Rechenoperationen können letztlich auf Kombinationen von 0 und 1 reduziert werden.

Dadurch können Prozessoren sehr schnell arbeiten.

---

## Was ist ein Bit?

Die kleinste Informationseinheit eines Computers heißt:

```
Bit
```

Ein Bit kann lediglich zwei Zustände speichern:

```
0
oder
1
```

---

## Was ist ein Byte?

Acht Bits werden zu einem Byte zusammengefasst.

```
1 Byte = 8 Bit
```

Beispiel:

```
01010110
```

Dieses Byte kann 256 verschiedene Zustände darstellen.

Warum?

```
2⁸ = 256
```

---

## Wie zählt man im Binärsystem?

| Dezimal | Binär |
|----------|--------|
| 0 | 0000 |
| 1 | 0001 |
| 2 | 0010 |
| 3 | 0011 |
| 4 | 0100 |
| 5 | 0101 |
| 6 | 0110 |
| 7 | 0111 |
| 8 | 1000 |

Man erkennt:

Nach der 1 kommt nicht die 2.

Stattdessen muss ein Übertrag durchgeführt werden.

### Warum funktioniert der Übertrag?

Das Prinzip ist identisch mit dem Dezimalsystem. Wenn alle Ziffern einer Stelle ausgeschöpft sind, wird die Stelle auf 0 zurückgesetzt und die nächsthöhere Stelle um 1 erhöht.

Im Dezimalsystem hat man die Ziffern 0–9. Nach der 9 gibt es keine weitere Ziffer, also wird die aktuelle Stelle 0 und die nächste Stelle erhöht: aus 9 wird 10.

Im Binärsystem hat man nur 0 und 1. Nach der 1 gibt es keine weitere Ziffer, also wird die aktuelle Stelle 0 und die nächste Stelle erhöht: aus 01 wird 10. Aus 011 wird 100.

Das führt dazu, dass beim Zählen von 7 (0111) auf 8 (1000) alle drei unteren Stellen umklappen — weil sich der Übertrag wie eine Welle durch alle vollen Stellen durchschlägt, bis er eine freie (0) Stelle findet.

---

## Umrechnung Dezimal → Binär

Beispiel:

```
13
```

Durch wiederholte Division durch 2:

```
13 : 2 = 6 Rest 1
 6 : 2 = 3 Rest 0
 3 : 2 = 1 Rest 1
 1 : 2 = 0 Rest 1
```

Von unten nach oben lesen:

```
1101₂
```

### Warum liest man die Reste von unten nach oben?

Das klingt zunächst willkürlich, hat aber eine klare Begründung.

Der erste Rest (ganz oben) entsteht beim ersten Dividieren von 13. Dabei fragt man: „Wie oft passt 2 in 13, und was bleibt übrig?" Der Rest ist genau das niedrigste Bit der Binärzahl — also die 2⁰-Stelle (Einerstelle). Er gibt an, ob die Zahl gerade oder ungerade ist.

Jede weitere Division arbeitet mit dem Quotienten der vorherigen Stufe und ermittelt so das nächsthöhere Bit. Der letzte Rest gehört damit zur höchsten Stelle — genauso wie beim Schreiben einer Dezimalzahl die größte Stelle ganz links steht.

Deshalb liest man die Reste von unten nach oben: Der letzte Rest ist das höchste Bit, der erste Rest das niedrigste.

Kontrolle:

```
8 + 4 + 1 = 13
```

---

## Umrechnung Binär → Dezimal

Beispiel:

```
101101₂
```

Berechnung:

```
1 · 2⁵ = 32
0 · 2⁴ = 0
1 · 2³ = 8
1 · 2² = 4
0 · 2¹ = 0
1 · 2⁰ = 1
```

Gesamt:

```
32 + 8 + 4 + 1
= 45
```

---

# Das Problem langer Binärzahlen

Eine Speicheradresse oder Farbe könnte beispielsweise so aussehen:

```
11111110101011001010111110001100
```

Das ist für Menschen schwer lesbar.

Deshalb wurde das Hexadezimalsystem eingeführt.

---

# Was ist das Hexadezimalsystem?

Das Hexadezimalsystem besitzt 16 Zeichen.

```
0 1 2 3 4 5 6 7 8 9 A B C D E F
```

Dabei gilt:

```
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
```

---

## Warum braucht man Hexadezimalzahlen?

Hexadezimalzahlen sind nur eine kompaktere Schreibweise für Binärzahlen.

Der große Vorteil:

```
4 Bit = genau 1 Hex-Zeichen
```

### Warum passt das so perfekt zusammen?

Mit 4 Bit kann man genau 2⁴ = 16 verschiedene Werte darstellen (0000 bis 1111, also 0 bis 15).

Das Hexadezimalsystem hat genau 16 Symbole: 0–9 und A–F.

Das ist kein Zufall — das Hexadezimalsystem wurde genau so gewählt, weil es sich lückenlos mit Binärzahlen deckt. Jeder der 16 möglichen 4-Bit-Werte hat genau ein Hex-Symbol, und jedes Hex-Symbol steht für genau einen 4-Bit-Wert.

Das bedeutet: Man kann eine beliebig lange Binärzahl in 4er-Gruppen aufteilen und jede Gruppe direkt durch ein Hex-Zeichen ersetzen — ohne jede Berechnung.

Beispiel:

```
1111 = F
```

Dadurch werden lange Binärzahlen sehr viel kürzer.

---

## Umrechnung Binär → Hexadezimal

Beispiel:

```
11111111
```

In Vierergruppen aufteilen:

```
1111 1111
```

Nun umwandeln:

```
1111 = F
1111 = F
```

Ergebnis:

```
FF₁₆
```

---

## Umrechnung Hexadezimal → Dezimal

Hexadezimalzahlen funktionieren nach demselben Stellenwert-Prinzip wie Dezimal- und Binärzahlen — nur mit der Basis 16.

Das bedeutet: Die erste Stelle von rechts hat den Stellenwert 16⁰ = 1, die zweite Stelle 16¹ = 16, die dritte 16² = 256 usw.

Beispiel: AF₁₆

```
A = 10
F = 15

A · 16¹ + F · 16⁰
= 10 · 16 + 15 · 1
= 160 + 15
= 175
```

Beispiel: 3C₁₆

```
3 · 16¹ + C · 16⁰
= 3 · 16 + 12 · 1
= 48 + 12
= 60
```

### Schnellweg: Hex → Binär → Dezimal

Oft ist es einfacher, zuerst jedes Hex-Zeichen in 4 Bit umzuwandeln und dann die Binärzahl auszuwerten.

```
AF₁₆

A = 1010
F = 1111

→ 10101111₂

= 128 + 32 + 8 + 4 + 2 + 1
= 175
```

---

## Wo wird Hexadezimal verwendet?

### Farben im Web

Rot:

```
#FF0000
```

Grün:

```
#00FF00
```

Blau:

```
#0000FF
```

### Speicheradressen

Betriebssysteme und Prozessoren zeigen Speicheradressen häufig in Hexadezimaldarstellung an.

### Debugging

Programmierer lesen Maschinendaten häufig in Hexadezimalform.

---

# Verbindung zu anderen Themen des Skripts

## Verbindung zu Binärarithmetik

Bevor ein Computer rechnen kann, müssen Zahlen als Binärzahlen dargestellt werden.

## Verbindung zum Zweierkomplement

Negative Zahlen werden durch spezielle Binärmuster dargestellt.

## Verbindung zu Fest- und Gleitkommazahlen

Auch Kommazahlen bestehen intern aus Binärwerten.

## Verbindung zu Hashing

Hashwerte werden meist in Hexadezimalform dargestellt.

Beispiel:

```
A94A8FE5CCB1...
```

## Verbindung zur Datenkompression

Komprimierte Daten bestehen ebenfalls aus Bitfolgen.

## Verbindung zu Java

Jede Variable im Speicher besteht am Ende aus Binärdaten.

---

# Typische Klausuraufgaben

## Aufgabe 1

Wandle 25 in eine Binärzahl um.

### Lösung

```
25 : 2 = 12 Rest 1
12 : 2 =  6 Rest 0
 6 : 2 =  3 Rest 0
 3 : 2 =  1 Rest 1
 1 : 2 =  0 Rest 1
```

Von unten nach oben lesen:

```
25 = 11001₂
```

Kontrolle:

```
1 · 2⁴ + 1 · 2³ + 0 · 2² + 0 · 2¹ + 1 · 2⁰
= 16 + 8 + 0 + 0 + 1
= 25 ✓
```

---

## Aufgabe 2

Wandle 110101₂ in eine Dezimalzahl um.

### Lösung

```
32 + 16 + 4 + 1
= 53
```

---

## Aufgabe 3

Wandle die Binärzahl um:

```
10101111
```

### Lösung

```
1010 1111

1010 = A
1111 = F

AF₁₆
```

---

## Aufgabe 4

Wie viele Werte kann ein Byte speichern?

### Lösung

```
2⁸ = 256
```

---

# Merksätze

1. Computer arbeiten mit Zuständen und deshalb mit Binärzahlen.
2. Ein Bit kann genau zwei Zustände speichern.
3. Ein Byte besteht aus 8 Bit.
4. Hexadezimal ist nur eine kompakte Schreibweise von Binärzahlen.
5. Ein Hex-Zeichen entspricht genau 4 Bit.
6. Fast alle späteren Themen im Informatikunterricht bauen auf dem Binärsystem auf.
