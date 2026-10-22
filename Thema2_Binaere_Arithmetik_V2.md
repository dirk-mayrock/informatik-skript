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
+0011
-----
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
+1111
------
11110
```

Kontrolle:

```text
15 + 15 = 30
```

Dieses Beispiel zeigt, wie Überträge über mehrere Stellen weitergegeben werden.

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

Im Binärsystem leiht man sich stattdessen eine 2.

---

## Beispiel 1

```text
 1010
-0011
-----
 0111
```

Kontrolle:

```text
10 - 3 = 7
```

---

## Beispiel 2: Mehrfaches Ausleihen

```text
10000
-00001
------
01111
```

Kontrolle:

```text
16 - 1 = 15
```

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

Warum?

Jede Stelle rückt um eine Position nach links.

Dadurch verdoppelt sich der Wert.

```text
11 × 2 = 22
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

Beispiel:

```text
1 + 1
```

Ergebnis:

```text
Summe = 0
Übertrag = 1
```

---

# Volladdierer

Sobald mehrere Stellen addiert werden, müssen Überträge berücksichtigt werden.

Deshalb verwendet ein Prozessor Volladdierer.

Diese können den Übertrag der vorherigen Stelle mitverarbeiten.

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
+0001
-----
10000
```

Für einen 4-Bit-Speicher ist jedoch kein Platz für die fünfte Stelle vorhanden.

Dies nennt man Overflow.

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
