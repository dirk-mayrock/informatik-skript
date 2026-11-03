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

| Film    | Mo  | Di  | Mi  | Do  | Fr  | Sa  | So  |
|---------|-----|-----|-----|-----|-----|-----|-----|
| Film 0  | 120 |  85 | 200 | 175 | 300 | 410 | 380 |
| Film 1  | 210 | 340 | 180 | 160 | 220 | 270 | 190 |
| Film 2  | 200 | 190 | 210 | 205 | 450 | 380 | 420 |
| Film 3  |  50 | 140 |  55 | 170 |  90 | 150 |  80 |
| Film 4  | 170 | 155 | 390 | 160 | 240 | 310 | 280 |

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
    {210, 340, 180, 160, 220, 270, 190},  // Film 1
    {200, 190, 210, 205, 450, 380, 420},  // Film 2
    { 50, 140,  55, 170,  90, 150,  80},  // Film 3
    {170, 155, 390, 160, 240, 310, 280}   // Film 4
};
```

Ein einzelner Wert wird mit **zwei Indizes** abgerufen:

```java
programm[2][4]   // Film 2, Freitag  → 450 Tickets
programm[0][0]   // Film 0, Montag   → 120 Tickets
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
            {120,  85, 200, 175, 300, 410, 380},  // Film 0 – bester Tag: Sa
            {210, 340, 180, 160, 220, 270, 190},  // Film 1 – bester Tag: Di
            {200, 190, 210, 205, 450, 380, 420},  // Film 2 – bester Tag: Fr
            { 50, 140,  55, 170,  90, 150,  80},  // Film 3 – bester Tag: Do
            {170, 155, 390, 160, 240, 310, 280}   // Film 4 – bester Tag: Mi
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
Film 1: 1570 Tickets
Film 2: 2055 Tickets
Film 3:  735 Tickets
Film 4: 1705 Tickets
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

## Aufgabe C – Erweiterung: Klasse Film (Zusatzaufgabe)

Diese Aufgabe ist **optional** und verbindet Arrays (Aufgabe A & B) mit Objektorientierung (Thema 11).

### Das Problem mit dem bisherigen Ansatz

Bisher speichern wir nur Zahlen im Array. Wenn wir zusätzliche Informationen pro Film brauchen – Titel, Dauer, Genre – passen diese nicht in ein `int[][]`, weil ein `int`-Array nur ganze Zahlen speichern kann.

Parallele Arrays wären eine schlechte Lösung:

```java
// Schlecht – alles auseinandergezogen, leicht zu verwechseln
String[] titel   = {"Matrix", "Barbie", "Oppenheimer", "Dune", "Avatar"};
int[]    dauer   = {136, 114, 180, 155, 192};
int[][]  verkaufe = { {120, 85, ...}, ... };
```

Die saubere Lösung: eine eigene Klasse `Film`.

### Schritt 1: Die Klasse Film schreiben

Alles, was zu einem Film gehört, kommt in eine Klasse. Die Verkaufsdaten sind ein `int[]`-Attribut innerhalb der Klasse.

```java
public class Film {

    // Attribute
    private String titel;
    private int    dauer;       // Laufzeit in Minuten
    private String genre;
    private int[]  verkaufe;    // Ticketverkäufe Mo bis So

    // Konstruktor
    public Film(String titel, int dauer, String genre, int[] verkaufe) {
        this.titel    = titel;
        this.dauer    = dauer;
        this.genre    = genre;
        this.verkaufe = verkaufe;
    }

    // Getter
    public String getTitel()    { return titel; }
    public int    getDauer()    { return dauer; }
    public String getGenre()    { return genre; }
    public int[]  getVerkaufe() { return verkaufe; }

    // Hilfsmethode: Gesamtverkäufe berechnen
    public int getGesamtverkaufe() {
        int summe = 0;
        for (int i = 0; i < verkaufe.length; i++) {
            summe = summe + verkaufe[i];
        }
        return summe;
    }
}
```

### Schritt 2: Ein Array von Film-Objekten anlegen

Statt `int[][]` verwenden wir jetzt `Film[]` – ein Array von Objekten.

```java
Film[] programm = {
    new Film("Matrix",      136, "SciFi",   new int[]{120,  85, 200, 175, 300, 410, 380}),
    new Film("Barbie",      114, "Komoedie",new int[]{210, 340, 180, 160, 220, 270, 190}),
    new Film("Oppenheimer", 180, "Drama",   new int[]{200, 190, 210, 205, 450, 380, 420}),
    new Film("Dune",        155, "SciFi",   new int[]{ 50, 140,  55, 170,  90, 150,  80}),
    new Film("Avatar",      192, "SciFi",   new int[]{170, 155, 390, 160, 240, 310, 280})
};
```

### Schritt 3: Die for-Schleife bleibt gleich – nur der Zugriff ändert sich

```java
for (int i = 0; i < programm.length; i++) {
    System.out.println(programm[i].getTitel()
                       + ": " + programm[i].getGesamtverkaufe()
                       + " Tickets (" + programm[i].getGenre() + ")");
}
```

### Vollständige Musterlösung C

Zwei Dateien in BlueJ – `Film.java` und `KinoProgrammOOP.java`.

#### Film.java

```java
public class Film {

    private String titel;
    private int    dauer;
    private String genre;
    private int[]  verkaufe;

    public Film(String titel, int dauer, String genre, int[] verkaufe) {
        this.titel    = titel;
        this.dauer    = dauer;
        this.genre    = genre;
        this.verkaufe = verkaufe;
    }

    public String getTitel()    { return titel; }
    public int    getDauer()    { return dauer; }
    public String getGenre()    { return genre; }
    public int[]  getVerkaufe() { return verkaufe; }

    public int getGesamtverkaufe() {
        int summe = 0;
        for (int i = 0; i < verkaufe.length; i++) {
            summe = summe + verkaufe[i];
        }
        return summe;
    }

    public String toString() {
        return titel + " (" + genre + ", " + dauer + " min)"
               + " – " + getGesamtverkaufe() + " Tickets";
    }
}
```

#### KinoProgrammOOP.java

```java
public class KinoProgrammOOP {

    public static void main(String[] args) {

        // Film-Array – jedes Element ist ein Objekt mit Metadaten + Verkaufszahlen
        Film[] programm = {
            new Film("Matrix",      136, "SciFi",    new int[]{120,  85, 200, 175, 300, 410, 380}),
            new Film("Barbie",      114, "Komoedie", new int[]{210, 340, 180, 160, 220, 270, 190}),
            new Film("Oppenheimer", 180, "Drama",    new int[]{200, 190, 210, 205, 450, 380, 420}),
            new Film("Dune",        155, "SciFi",    new int[]{ 50, 140,  55, 170,  90, 150,  80}),
            new Film("Avatar",      192, "SciFi",    new int[]{170, 155, 390, 160, 240, 310, 280})
        };

        // Alle Filme ausgeben
        for (int i = 0; i < programm.length; i++) {
            System.out.println(programm[i].toString());
        }

        // Bester Film gesamt
        int maxIdx = 0;
        for (int i = 1; i < programm.length; i++) {  // i=1: programm[0] ist erster Kandidat
            if (programm[i].getGesamtverkaufe() > programm[maxIdx].getGesamtverkaufe()) {
                maxIdx = i;
            }
        }
        System.out.println("Erfolgreichster Film: " + programm[maxIdx].getTitel());
    }
}
```

Erwartete Ausgabe in BlueJ:

```
Matrix (SciFi, 136 min) – 1670 Tickets
Barbie (Komoedie, 114 min) – 1570 Tickets
Oppenheimer (Drama, 180 min) – 2055 Tickets
Dune (SciFi, 155 min) – 735 Tickets
Avatar (SciFi, 192 min) – 1705 Tickets
Erfolgreichster Film: Oppenheimer
```

### Was hat sich geändert?

| Aufgabe B | Aufgabe C |
|-----------|-----------|
| `int[][] programm` | `Film[] programm` |
| `programm[i][tag]` | `programm[i].getVerkaufe()[tag]` |
| `programm.length` | `programm.length` |
| kein Titel, kein Genre | `programm[i].getTitel()`, `programm[i].getGenre()` |

Die verschachtelte for-Schleife bleibt **strukturell identisch**. Nur der Zugriff auf die Daten geht jetzt durch die Klasse.

---

## Merksätze

1. Arrays speichern mehrere Werte **desselben Typs** unter einem Namen.
2. Der erste Index ist immer **0**, der letzte ist `array.length - 1`.
3. `array.length` gibt die Anzahl der Elemente zurück – **kein Methodenaufruf** (kein `()`).
4. Ein 2D-Array ist ein **Array von Arrays**: `int[][] tabelle = new int[zeilen][spalten];`.
5. Beim Zugriff auf `tabelle[zeile][spalte]` ist die **Zeile immer zuerst**.
6. `ArrayIndexOutOfBoundsException` entsteht, wenn der Index kleiner als 0 oder größer als `length - 1` ist.
7. Wenn ein Array verschiedene Datentypen pro Element braucht, ist eine **eigene Klasse** die richtige Lösung.
8. `Film[]` ist ein Array von Objekten – `programm.length` funktioniert genauso wie bei `int[]`.
