# Klausurvorbereitung: Arrays & 2D-Arrays

## Szenario: Kino-Wochenprogramm

---

## Das Szenario

Ein Kino zeigt in einer Woche **5 verschiedene Filme**. Für jeden Film werden die **Ticketverkäufe an 7 Tagen** (Montag bis Sonntag) erfasst.

Deine Aufgabe: Schreibe ein Java-Programm, das diese Daten speichert, auswertet und auf der Konsole ausgibt.

Dieses Szenario wird in zwei Schritten gelöst:
- **Aufgabe A** – Zuerst nur ein einzelner Film → **1D-Array**
- **Aufgabe B** – Alle fünf Filme gleichzeitig → **2D-Array**

---

## Aufgabe A – Ein Film, eine Woche (1D-Array)

### Die Aufgabe (Klausur-Text)

Ein Kino erfasst die Ticketverkäufe eines Films für die sieben Tage der Woche:

| Tag       | Mo  | Di | Mi  | Do  | Fr  | Sa  | So  |
|-----------|-----|----|-----|-----|-----|-----|-----|
| Tickets   | 120 | 85 | 200 | 175 | 300 | 410 | 380 |

Schreibe eine Klasse `KinoWoche` mit einer `main`-Methode, die:
1. Die Verkaufszahlen in einem `int`-Array speichert.
2. Die **Gesamtanzahl** aller verkauften Tickets berechnet und ausgibt.
3. Den **Index des besten Tages** (meiste Tickets) ermittelt und ausgibt.

### Schritt 1: Das Array deklarieren

Ein Array speichert mehrere Werte **desselben Typs** unter einem Namen.

```java
// 7 Werte, ein Array – Index läuft von 0 bis 6
int[] verkaufe = {120, 85, 200, 175, 300, 410, 380};
```

Wichtig: Der erste Tag (Montag) hat den Index **0**, Sonntag hat Index **6**.

```
Index:    0    1    2    3    4    5    6
Wert:   120   85  200  175  300  410  380
Tag:     Mo   Di   Mi   Do   Fr   Sa   So
```

### Schritt 2: Alle Werte summieren (for-Schleife)

Mit einer `for`-Schleife und `array.length` lässt sich jedes Array durchlaufen, egal wie groß es ist.

```java
int summe = 0;
for (int i = 0; i < verkaufe.length; i++) {
    summe = summe + verkaufe[i];  // addiere Eintrag an Stelle i
}
System.out.println("Gesamt: " + summe + " Tickets");
```

### Schritt 3: Den besten Tag finden

Wir merken uns den Index des bisher besten Wertes und aktualisieren ihn bei jedem Fund.

```java
int maxIndex = 0;                             // Index 0 ist der erste Kandidat
for (int i = 1; i < verkaufe.length; i++) {  // i=1: Index 0 ist bereits gesetzt,
    if (verkaufe[i] > verkaufe[maxIndex]) {   //      alle anderen werden verglichen
        maxIndex = i;                         // besseren Tag merken
    }
}
System.out.println("Bester Tag: Index " + maxIndex
                   + " mit " + verkaufe[maxIndex] + " Tickets");
```

**Warum beginnt die Schleife bei `i = 1`?**
`maxIndex = 0` bedeutet: „Ich nehme erstmal an, dass Index 0 der beste ist."
Die Schleife muss dann nur noch alle *übrigen* Einträge (Index 1 bis 6) dagegen prüfen.
Mit `i = 0` würde man Index 0 gegen sich selbst vergleichen — das ist unnötig, aber kein Fehler.

### Vollständige Musterlösung A

```java
public class KinoWoche {

    public static void main(String[] args) {

        // Ticketverkäufe Mo bis So
        int[] verkaufe = {120, 85, 200, 175, 300, 410, 380};

        // --- Gesamtverkäufe berechnen ---
        int summe = 0;
        for (int i = 0; i < verkaufe.length; i++) {
            summe = summe + verkaufe[i];
        }
        System.out.println("Gesamt: " + summe + " Tickets");

        // --- Besten Tag ermitteln ---
        int maxIndex = 0;                        // Index 0 ist der erste Kandidat
        for (int i = 1; i < verkaufe.length; i++) { // i=1: alle übrigen prüfen
            if (verkaufe[i] > verkaufe[maxIndex]) {
                maxIndex = i;
            }
        }
        System.out.println("Bester Tag: Index " + maxIndex
                           + " mit " + verkaufe[maxIndex] + " Tickets");
    }
}
```

Erwartete Ausgabe in BlueJ:

```
Gesamt: 1670 Tickets
Bester Tag: Index 5 mit 410 Tickets
```

---

## Aufgabe B – Alle Filme (2D-Array)

### Die Aufgabe (Klausur-Text)

Das Kino zeigt jetzt 5 Filme gleichzeitig. Die Tabelle sieht so aus:

|         | Mo  | Di  | Mi  | Do  | Fr  | Sa  | So  |
|---------|-----|-----|-----|-----|-----|-----|-----|
| Film 0  | 120 |  85 | 200 | 175 | 300 | 410 | 380 |
| Film 1  |  95 | 110 | 130 | 160 | 220 | 370 | 340 |
| Film 2  | 200 | 190 | 210 | 205 | 280 | 450 | 420 |
| Film 3  |  50 |  60 |  55 |  70 |  90 | 150 | 140 |
| Film 4  | 170 | 155 | 180 | 160 | 240 | 390 | 360 |

Schreibe eine Klasse `KinoProgramm`, die:
1. Diese Tabelle als **zweidimensionales Array** speichert.
2. Mit einer **verschachtelten for-Schleife** die Gesamtverkäufe pro Film berechnet und ausgibt.

### Schritt 1: Das 2D-Array verstehen

Ein 2D-Array ist ein Array von Arrays – also eine Tabelle mit Zeilen und Spalten.

```
programm[zeile][spalte]
          Film    Tag
```

Deklaration und Initialisierung:

```java
int[][] programm = {
    {120,  85, 200, 175, 300, 410, 380},  // Film 0
    { 95, 110, 130, 160, 220, 370, 340},  // Film 1
    {200, 190, 210, 205, 280, 450, 420},  // Film 2
    { 50,  60,  55,  70,  90, 150, 140},  // Film 3
    {170, 155, 180, 160, 240, 390, 360}   // Film 4
};
```

Ein einzelner Wert wird mit **zwei Indizes** abgerufen:

```java
programm[2][5]   // Film 2, Samstag → 450 Tickets
programm[0][0]   // Film 0, Montag  → 120 Tickets
```

### Schritt 2: Verschachtelte for-Schleife

Die äußere Schleife geht durch die Filme (Zeilen), die innere durch die Tage (Spalten).

```java
// Äußere Schleife: jede Zeile = ein Film
for (int film = 0; film < programm.length; film++) {

    int summe = 0;

    // Innere Schleife: jede Spalte = ein Tag
    for (int tag = 0; tag < programm[film].length; tag++) {
        summe = summe + programm[film][tag];
    }

    System.out.println("Film " + film + ": " + summe + " Tickets");
}
```

`programm.length` gibt die Anzahl der Zeilen (5 Filme).
`programm[film].length` gibt die Anzahl der Spalten (7 Tage) der aktuellen Zeile.

### Vollständige Musterlösung B

```java
public class KinoProgramm {

    public static void main(String[] args) {

        // 5 Filme x 7 Tage  (Zeile = Film, Spalte = Tag)
        int[][] programm = {
            {120,  85, 200, 175, 300, 410, 380},  // Film 0
            { 95, 110, 130, 160, 220, 370, 340},  // Film 1
            {200, 190, 210, 205, 280, 450, 420},  // Film 2
            { 50,  60,  55,  70,  90, 150, 140},  // Film 3
            {170, 155, 180, 160, 240, 390, 360}   // Film 4
        };

        // Gesamtverkäufe pro Film berechnen
        for (int film = 0; film < programm.length; film++) {
            int summe = 0;
            for (int tag = 0; tag < programm[film].length; tag++) {
                summe = summe + programm[film][tag];
            }
            System.out.println("Film " + film + ": " + summe + " Tickets");
        }
    }
}
```

Erwartete Ausgabe in BlueJ:

```
Film 0: 1670 Tickets
Film 1: 1425 Tickets
Film 2: 1955 Tickets
Film 3:  615 Tickets
Film 4: 1655 Tickets
```

---

## Typische Klausuraufgaben

### Aufgabe 1

Was gibt folgender Code aus?

```java
int[] zahlen = {10, 20, 30, 40, 50};
System.out.println(zahlen[2]);
System.out.println(zahlen.length);
```

#### Lösung

```
30
5
```

`zahlen[2]` ist der Wert an Index 2 (also der dritte Wert = 30). `length` gibt die Anzahl der Elemente zurück, also 5.

---

### Aufgabe 2

Was passiert bei diesem Code und warum?

```java
int[] zahlen = {10, 20, 30};
System.out.println(zahlen[3]);
```

#### Lösung

```
ArrayIndexOutOfBoundsException: Index 3 out of bounds for length 3
```

Das Array hat nur die Indizes 0, 1 und 2. Index 3 existiert nicht. Java wirft eine Laufzeit-Ausnahme.

---

### Aufgabe 3

Schreibe eine for-Schleife, die alle Elemente des Arrays `noten` der Reihe nach ausgibt.

```java
int[] noten = {2, 1, 3, 2, 4, 1};
```

#### Lösung

```java
for (int i = 0; i < noten.length; i++) {
    System.out.println(noten[i]);
}
```

---

### Aufgabe 4

Gegeben ist folgendes 2D-Array:

```java
int[][] tabelle = {
    {1, 2, 3},
    {4, 5, 6}
};
```

Was gibt `tabelle[1][2]` aus?

#### Lösung

```
6
```

Zeile 1 ist `{4, 5, 6}`, Spalte 2 ist der dritte Wert: 6.

---

## Merksätze

1. Arrays speichern mehrere Werte **desselben Typs** unter einem Namen.
2. Der erste Index ist immer **0**, der letzte ist `array.length - 1`.
3. `array.length` gibt die Anzahl der Elemente zurück – **kein Methodenaufruf** (kein `()`).
4. Ein 2D-Array ist ein **Array von Arrays**: `int[][] tabelle = new int[zeilen][spalten];`.
5. Beim Zugriff auf `tabelle[zeile][spalte]` ist die **Zeile immer zuerst**.
6. `ArrayIndexOutOfBoundsException` entsteht, wenn der Index kleiner als 0 oder größer als `length - 1` ist.
