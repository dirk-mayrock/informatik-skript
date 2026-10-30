# Praktikum 9: Methoden – Fortgeschritten

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Einfache Methoden schreiben und aufrufen
**Heute lernen wir:** Methoden überladen, Konstanten, Wechselgeld-Algorithmus
**Danach können wir:** Den vollständigen prozeduralen Getränkeautomaten fertigstellen
:::

---

## Neue Syntax

### Methoden überladen (Overloading)

Zwei Methoden dürfen **denselben Namen** haben, wenn sie **verschiedene Parameter** haben:

```java
public static void kaufe(int nummer, double betrag) { ... }
public static void kaufe(String name, double betrag) { ... }
```

Java erkennt automatisch, welche Methode gemeint ist:

```java
kaufe(2, 1.50);        // → kaufe(int, double)
kaufe("Cola", 1.50);   // → kaufe(String, double)
```

### Konstanten mit `final`

```java
static final double MAX_MUENZE = 2.00;
static final int    ANZAHL     = 5;
```

`final` = der Wert kann **nach der Zuweisung nicht mehr geändert werden**.
Konvention: Konstanten werden **GROSSGESCHRIEBEN**.

### Geltungsbereich (Scope)

Eine Variable existiert nur innerhalb der geschweiften Klammern, in denen sie deklariert wurde:

```java
public static void beispiel() {
    int x = 10;      // x lebt in dieser Methode
}
// x ist hier nicht mehr zugänglich!
```

Klassenvariablen (`static`) sind in allen Methoden der Klasse sichtbar:

```java
public class Automat {
    static String[] namen = {"Cola", "Wasser"};   // überall sichtbar

    public static void zeigeMenu() {
        System.out.println(namen[0]);   // funktioniert!
    }
}
```

### Wechselgeld-Algorithmus (Münz-Stückelung)

Grundidee: Immer die **größtmögliche Münze** wählen, bis der Rest 0 ist.

```java
double[] muenzen = {2.00, 1.00, 0.50, 0.20, 0.10};
int cents = (int) Math.round(rueckgeld * 100);   // in Cent umrechnen

for (double muenze : muenzen) {
    int muenzCents = (int) Math.round(muenze * 100);
    int anzahl     = cents / muenzCents;
    if (anzahl > 0) {
        System.out.print(anzahl + " × " + muenze + " EUR  ");
        cents -= anzahl * muenzCents;
    }
}
```

Beispiel: 0,80 EUR Wechselgeld → `1 × 0.50 EUR  1 × 0.20 EUR  1 × 0.10 EUR`

---

## Im Getränkeautomaten anwenden

Das vollständige prozedurale Programm – alle Funktionen sauber in Methoden aufgeteilt:

```java
import java.util.Scanner;

public class Getraenkeautomat {

    static final double[] MUENZEN = {2.00, 1.00, 0.50, 0.20, 0.10};  // NEU ←
    static String[] namen   = {"Cola", "Apfelschorle", "Wasser", "Eistee", "Limo"};
    static double[] preise  = {1.50, 1.00, 1.00, 1.20, 1.30};
    static int[]    bestand = {5, 3, 5, 2, 4};

    public static void zeigeMenu() { ... }

    public static double geldEinwerfen(Scanner scanner) { ... }

    public static void gibWechselgeld(double betrag) {    // NEU ←
        int cents = (int) Math.round(betrag * 100);
        System.out.print("Wechselgeld: ");
        for (double m : MUENZEN) {
            int mc = (int) Math.round(m * 100);
            int n  = cents / mc;
            if (n > 0) {
                System.out.print(n + " × " + m + " EUR  ");
                cents -= n * mc;
            }
        }
        System.out.println();
    }

    // Überladen: kaufe per Nummer                       NEU ←
    public static void kaufeGetraenk(int wahl, double betrag) {
        int index = wahl - 1;
        if (betrag >= preise[index]) {
            bestand[index]--;
            System.out.println(">>> " + namen[index] + " ausgegeben! <<<");
            gibWechselgeld(betrag - preise[index]);
        } else {
            System.out.println("Nicht genug Geld.");
            gibWechselgeld(betrag);
        }
    }

    // Überladen: kaufe per Name                         NEU ←
    public static void kaufeGetraenk(String name, double betrag) {
        for (int i = 0; i < namen.length; i++) {
            if (namen[i].equalsIgnoreCase(name)) {
                kaufeGetraenk(i + 1, betrag);
                return;
            }
        }
        System.out.println("Getraenk nicht gefunden.");
    }

    public static void main(String[] args) { ... }
}
```

Der vollständige Code befindet sich in:
`java/P09_Methoden_Fortgeschritten/Getraenkeautomat.java`

---

## Aufgabe

Die Methode `gibWechselgeld(double betrag)` gibt den Betrag in Münzen aus.
Schreibe zusätzlich eine Methode `gibWechselgeldAlsText(double betrag)`, die statt zu drucken einen **String zurückgibt**:

```
"2 × 0.20 EUR  1 × 0.10 EUR"
```

## Lösung

```java
public static String gibWechselgeldAlsText(double betrag) {
    StringBuilder sb = new StringBuilder();
    int cents = (int) Math.round(betrag * 100);
    for (double m : MUENZEN) {
        int mc = (int) Math.round(m * 100);
        int n  = cents / mc;
        if (n > 0) {
            sb.append(n).append(" × ").append(m).append(" EUR  ");
            cents -= n * mc;
        }
    }
    return sb.toString().trim();
}
```

---

## Merksätze

1. Methoden überladen: gleicher Name, unterschiedliche Parameter – Java wählt automatisch die passende.
2. `final` macht eine Variable zur Konstante – der Wert kann nicht mehr geändert werden.
3. Konstanten in GROSSBUCHSTABEN schreiben (Konvention).
4. Scope: Variablen existieren nur in den `{}` in denen sie deklariert wurden.
5. Wechselgeld: in Cent umrechnen (Ganzzahl), dann von größter Münze abwärts aufteilen.
