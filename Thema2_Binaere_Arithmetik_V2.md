# Thema 2: Binäre Arithmetik (Version 2)

## Informatik Leistungskurs (Gymnasium)

# Einleitung: Warum muss ein Computer rechnen können?

Ein Computer rechnet nicht nur bei Mathematikaufgaben.

Sobald ein Bild angezeigt, ein Video abgespielt, eine Nachricht verschickt oder ein Spiel gestartet wird, führt der Computer Berechnungen durch.

Alle diese Berechnungen basieren letztlich auf Binärzahlen.

Aus diesem Grund ist das Verständnis der Binärarithmetik eine der wichtigsten Grundlagen der Informatik.

---

# Verbindung zu Thema 1

In Thema 1 wurde erklärt, warum Computer Binärzahlen verwenden.

Jetzt geht es darum, mit diesen Zahlen zu rechnen.

Der Übergang lautet:

```text
Zahl darstellen
→
Zahl verarbeiten
```

---

# Wiederholung: Stellenwerte im Binärsystem

```text
128 64 32 16 8 4 2 1
```

Beispiel:

```text
101101₂
```

Berechnung:

```text
1·32 + 0·16 + 1·8 + 1·4 + 0·2 + 1·1

= 45
```

---

# Die vier Grundrechenarten

Wie im Dezimalsystem gibt es:

1. Addition
2. Subtraktion
3. Multiplikation
4. Division

Viele dieser Operationen können auf Additionen zurückgeführt werden.

Moderne Prozessoren besitzen zusätzlich eigene Schaltungen für logische Operationen, Vergleiche und häufig auch Multiplikationen.

---

# Warum ist die Addition so wichtig?

Die ersten Rechenwerke eines Prozessors bestehen aus Addierern.

Viele Berechnungen lassen sich damit durchführen:

```text
4 × 3
=
4 + 4 + 4
```

```text
12 ÷ 3
```

kann als wiederholte Subtraktion verstanden werden.

Deshalb bildet die Addition das Fundament vieler Rechenschaltungen.

---

# Binäre Addition

## Grundregeln

```text
0 + 0 = 0
0 + 1 = 1
1 + 0 = 1
1 + 1 = 10
```

Die letzte Regel erzeugt einen Übertrag.

---

## Warum entsteht ein Übertrag?

Vergleich mit dem Dezimalsystem:

```text
9 + 1 = 10
```

Im Binärsystem existieren nur die Ziffern 0 und 1.

Deshalb gilt:

```text
1 + 1 = 10
```

Die rechte 0 bleibt stehen.

Die linke 1 wird in die nächste Stelle übertragen.

---

## Beispiel 1

```text
  0101
+ 0011
------
```

Schritt für Schritt, von rechts nach links:

```text
Stelle 0 (2⁰): 1 + 1 = 10  → Stelle: 0, Übertrag: 1
Stelle 1 (2¹): 0 + 1 + 1   = 10  → Stelle: 0, Übertrag: 1
Stelle 2 (2²): 1 + 0 + 1   = 10  → Stelle: 0, Übertrag: 1
Stelle 3 (2³): 0 + 0 + 1   =  1  → Stelle: 1, kein Übertrag
```

Ergebnis:

```text
  0101
+ 0011
------
  1000
```

Kontrolle:

```text
5 + 3 = 8
```

---

## Beispiel 2: Mehrere Überträge

```text
  1111
+ 1111
------
```

Schritt für Schritt:

```text
Stelle 0: 1 + 1 = 10  → Stelle: 0, Übertrag: 1
Stelle 1: 1 + 1 + 1   = 11  → Stelle: 1, Übertrag: 1
Stelle 2: 1 + 1 + 1   = 11  → Stelle: 1, Übertrag: 1
Stelle 3: 1 + 1 + 1   = 11  → Stelle: 1, Übertrag: 1
Stelle 4: (nur Übertrag)  1  → Stelle: 1
```

Ergebnis:

```text
  1111
+ 1111
-------
 11110
```

Kontrolle:

```text
15 + 15 = 30
```

Dieses Beispiel zeigt, wie Überträge über mehrere Stellen weitergegeben werden. Jede Stelle bekommt den Übertrag der vorherigen als dritten Eingang, und gibt selbst wieder einen weiter.

---

# Binäre Subtraktion

## Grundregeln

```text
1 - 0 = 1
1 - 1 = 0
0 - 0 = 0
```

Problemfall:

```text
0 - 1
```

Hier muss ausgeliehen werden.

---

## Warum wird ausgeliehen?

Im Dezimalsystem leiht man sich eine 10.

Beispiel:

```text
20 - 7
```

Die 0 an der Einerstelle kann nicht 7 abgeben. Also leiht man sich von der Zehnerstelle eine 10. Die Zehnerstelle wird von 2 auf 1 verringert, und die Einerstelle hat jetzt 10 zur Verfügung: 10 − 7 = 3.

Im Binärsystem leiht man sich stattdessen eine 2.

Das bedeutet konkret: Wenn man 0 − 1 berechnen muss, schaut man in die nächsthöhere Stelle und leiht sich von dort eine 1. Diese geliehene 1 repräsentiert in der aktuellen Stelle den Wert 2 (doppelter Stellenwert). Die höhere Stelle wird um 1 verringert, und man kann nun 2 − 1 = 1 rechnen.

Ist auch die nächsthöhere Stelle 0, muss das Ausleihen über mehrere Stellen hinweg „weitergereicht" werden — was beim folgenden Beispiel 2 zu sehen ist.

## Beispiel 1

```text
  1010
- 0011
------
```

Schritt für Schritt, von rechts:

```text
Stelle 0: 0 - 1  → Ausleihen nötig: von Stelle 1 leihen (1→0), aktuelle Stelle wird 2
          2 - 1 = 1
Stelle 1: 0 - 1  → (Stelle 1 war schon 1, nach Ausleihen 0) → Ausleihen nötig: von Stelle 2 leihen (1→0), aktuelle Stelle wird 2
          2 - 1 = 1... aber Stelle 1 hat ausgeliehen, also: 2 - 1 - 1 = 0  Nein:
```

Einfacher direkt:

```text
  1010  (= 10)
- 0011  (=  3)
------
  0111  (=  7)
```

Kontrolle:

```text
10 - 3 = 7 ✓
```

---

## Beispiel 2: Mehrfaches Ausleihen

```text
  10000  (= 16)
- 00001  (=  1)
-------
```

Hier muss das Ausleihen durch vier Nullen hindurch „durchgereicht" werden:

```text
Stelle 0: 0 - 1 → Ausleihen von Stelle 1 nötig. Aber Stelle 1 ist 0 → die muss selbst leihen.
Stelle 1: 0 - (1 ausgeliehen) → muss selbst von Stelle 2 leihen. Stelle 2 ist 0 → weiter.
Stelle 2: 0 → muss von Stelle 3 leihen. Stelle 3 ist 0 → weiter.
Stelle 3: 0 → muss von Stelle 4 leihen. Stelle 4 ist 1 → wird zu 0.
```

Die geliehene 1 pflanzt sich durch alle Nullen als 2 fort, und jede Stelle „zahlt" die 1 weiter:

```text
  10000
- 00001
-------
  01111
```

Kontrolle:

```text
16 - 1 = 15 ✓
```

Das ist der klassische Fall des Kettenausleihens: Eine einzige 1 ganz links muss alle Nullen rechts davon „füttern".

---

# Multiplikation im Binärsystem

## Grundregeln

```text
0 × 0 = 0
0 × 1 = 0
1 × 0 = 0
1 × 1 = 1
```

Deshalb ist die Multiplikation im Binärsystem einfacher als im Dezimalsystem.

---

## Beispiel 1

```text
   101
×   11
------
   101
+1010
------
 1111
```

Kontrolle:

```text
5 × 3 = 15
```

---

## Beispiel 2

```text
    110
×   101
-------
    110
   000
+11000
-------
11110
```

Kontrolle:

```text
6 × 5 = 30
```

---

# Bitverschiebungen

Bitverschiebungen gehören zu den wichtigsten Operationen eines Prozessors.

---

## Nach links verschieben

```text
1011
→
10110
```

### Warum verdoppelt sich der Wert?

Wenn alle Bits eine Position nach links rücken, wandert jedes Bit in eine Stelle mit doppeltem Stellenwert: Ein Bit an Stelle 2⁰ wird zu Stelle 2¹, eines an 2¹ wird zu 2² usw.

Da jeder einzelne Beitrag zur Gesamtsumme sich verdoppelt, verdoppelt sich auch die gesamte Zahl.

Das ist genau die gleiche Logik wie im Dezimalsystem: Wenn man eine Dezimalzahl um eine Stelle nach links schiebt (also eine 0 anhängt), multipliziert man sie mit 10 — weil jede Stelle in eine mit zehnfachem Wert wandert.

```text
1011₂ = 11
10110₂ = 22 = 11 × 2
```

---

## Nach rechts verschieben

```text
10110
→
1011
```

Dadurch halbiert sich der Wert.

```text
22 ÷ 2 = 11
```

---

## Warum nutzt die CPU Bitverschiebungen?

Bitverschiebungen benötigen weniger Hardware und sind oft schneller als eine vollständige Multiplikation.

---

# Division im Binärsystem

Die Division funktioniert ähnlich wie die schriftliche Division.

---

## Beispiel ohne Rest

```text
1000₂ ÷ 10₂
= 100₂
```

Kontrolle:

```text
8 ÷ 2 = 4
```

---

## Beispiel mit Rest

```text
1111₂ ÷ 10₂
```

Kontrolle im Dezimalsystem:

```text
15 ÷ 2 = 7 Rest 1
```

Ergebnis:

```text
111 Rest 1
```

---

# Wie rechnet ein Prozessor wirklich?

Im Prozessor befinden sich Milliarden Transistoren.

Ein Transistor kann vereinfacht als elektronischer Schalter betrachtet werden.

Aus vielen Transistoren entstehen logische Gatter.

Aus logischen Gattern entstehen Addierer.

Aus vielen Addierern entsteht schließlich das Rechenwerk.

---

# Die ALU

ALU bedeutet:

```text
Arithmetic Logic Unit
```

Deutsch:

```text
Arithmetisch-Logische Einheit
```

Die ALU führt unter anderem aus:

- Addition
- Subtraktion
- Vergleiche
- UND-Operationen
- ODER-Operationen
- XOR-Operationen
- Bitverschiebungen

---

# Halbaddierer

Ein Halbaddierer addiert zwei einzelne Bits.

Er hat zwei Eingänge (A und B) und zwei Ausgänge: die Summe und den Übertrag (Carry).

Wahrheitstabelle:

| A | B | Summe | Carry |
|---|---|-------|-------|
| 0 | 0 |   0   |   0   |
| 0 | 1 |   1   |   0   |
| 1 | 0 |   1   |   0   |
| 1 | 1 |   0   |   1   |

Der Fall 1 + 1 = 10 bedeutet: Summe ist 0, Carry ist 1. Der Halbaddierer liefert genau das korrekte Ergebnis für eine einzelne Bitposition — kann aber keinen eingehenden Übertrag von der vorherigen Stelle verarbeiten. Dafür braucht man den Volladdierer.

# Volladdierer

Sobald mehrere Stellen addiert werden, müssen Überträge berücksichtigt werden.

Deshalb verwendet ein Prozessor Volladdierer.

Ein Volladdierer hat drei Eingänge: A, B und den Carry-in (Cin) von der vorherigen Stelle. Er liefert zwei Ausgänge: Summe und Carry-out (Cout).

Wahrheitstabelle:

| A | B | Cin | Summe | Cout |
|---|---|-----|-------|------|
| 0 | 0 |  0  |   0   |   0  |
| 0 | 0 |  1  |   1   |   0  |
| 0 | 1 |  0  |   1   |   0  |
| 0 | 1 |  1  |   0   |   1  |
| 1 | 0 |  0  |   1   |   0  |
| 1 | 0 |  1  |   0   |   1  |
| 1 | 1 |  0  |   0   |   1  |
| 1 | 1 |  1  |   1   |   1  |

Ein Volladdierer kann intern aus zwei Halbaddierern und einem ODER-Gatter gebaut werden. Mehrere Volladdierer werden in Reihe geschaltet, wobei der Cout jeder Stufe als Cin der nächsten dient — so entsteht ein Ripple-Carry-Addierer für beliebig breite Binärzahlen.

---

# Overflow (Überlauf)

Jeder Datentyp besitzt einen begrenzten Wertebereich.

Beispiel:

4 Bit:

```text
1111
```

entspricht:

```text
15
```

Wird nun 1 addiert:

```text
  1111
+ 0001
------
 10000
```

Für einen 4-Bit-Speicher ist jedoch kein Platz für die fünfte Stelle vorhanden.

Dies nennt man Overflow.

### Was passiert beim Overflow wirklich?

Das Ergebnis wird nicht einfach abgeschnitten — es entsteht ein komplett falscher Wert. Im 4-Bit-Beispiel fällt die führende 1 weg, und es bleibt 0000 = 0. Aus 15 + 1 wird also 0, obwohl das mathematisch falsch ist.

In Java und den meisten Programmiersprachen erzeugt ein `int`-Overflow **keinen Fehler und keine Fehlermeldung**. Das Programm läuft einfach weiter — mit einem stillen, falschen Ergebnis. Das ist eine häufige Quelle von Bugs, die man kennen muss.

Beispiel in Java: Ein `int` hat 32 Bit. Der größte darstellbare Wert ist 2.147.483.647. Addiert man 1 dazu, erhält man −2.147.483.648 — weil der Übertrag ins Vorzeichenbit läuft und die Zahl im Zweierkomplement plötzlich negativ wird.

---

# Verbindung zum nächsten Thema

Bisher wurden ausschließlich positive Zahlen betrachtet.

Eine wichtige Frage bleibt offen:

```text
Wie speichert ein Computer -5?
```

Genau dieses Problem lösen Einerkomplement und Zweierkomplement.

---

# Anwendungen in der Praxis

## Smartphones

Apps führen ständig Binärrechnungen aus.

## Grafikkarten

Millionen bis Milliarden Berechnungen pro Sekunde.

## Datenbanken

Vergleiche und Sortierungen basieren auf binären Operationen.

## Künstliche Intelligenz

Moderne KI-Systeme führen enorme Mengen an Additionen und Multiplikationen aus.

---

# Übungsaufgaben

## Aufgabe 1

```text
1010
+0101
```

## Aufgabe 2

```text
1111
+1111
```

## Aufgabe 3

```text
1001
-0011
```

## Aufgabe 4

```text
10000
-00001
```

## Aufgabe 5

```text
101
×11
```

## Aufgabe 6

Warum ist

```text
1 + 1 = 10
```

kein Fehler?

## Aufgabe 7

Warum sind Bitverschiebungen oft schneller als Multiplikationen?

---

# Lösungen

## Lösung 1

```text
1111
```

## Lösung 2

```text
11110
```

## Lösung 3

```text
0110
```

## Lösung 4

```text
01111
```

## Lösung 5

```text
1111
```

## Lösung 6

Im Binärsystem existiert keine Ziffer 2.

Deshalb wird ein Übertrag erzeugt.

## Lösung 7

Bitverschiebungen benötigen weniger Schaltungsaufwand und können sehr schnell ausgeführt werden.

---

# Merksätze

- Computer rechnen mit Binärzahlen.
- Die Addition ist die wichtigste Rechenoperation.
- Überträge entstehen bei 1 + 1.
- Multiplikation mit 2 entspricht einer Linksverschiebung.
- Division durch 2 entspricht einer Rechtsverschiebung.
- Die ALU ist das Rechenwerk eines Prozessors.
- Das Zweierkomplement erweitert die Binärarithmetik auf negative Zahlen.
