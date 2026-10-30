# Praktikum 6: Arrays, for und for-each

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Einzelne Getränke mit Variablen speichern und per switch wählen
**Heute lernen wir:** Arrays – viele Werte in einer Variablen; for und for-each Schleifen
**Danach können wir:** Alle 5 Getränke in Arrays speichern und das Menü automatisch ausgeben
:::

---

## Neue Syntax

### Array deklarieren und befüllen

Ein Array speichert **mehrere Werte desselben Typs** hintereinander im Speicher.

```java
// Variante 1: direkte Initialisierung
String[] namen  = {"Cola", "Wasser", "Limo"};
double[] preise = {1.50, 1.00, 1.30};

// Variante 2: erst Größe, dann Werte eintragen
int[] bestand = new int[3];
bestand[0] = 5;
bestand[1] = 3;
bestand[2] = 4;
```

| Begriff | Bedeutung |
|---------|-----------|
| `String[]` | Array-Typ: Array aus Strings |
| `namen[0]` | Erstes Element (Index beginnt bei **0**!) |
| `namen.length` | Anzahl der Elemente |

### for-Schleife mit Index

```java
for (int i = 0; i < namen.length; i++) {
    System.out.println(namen[i]);
}
```

Struktur: `for (Start; Bedingung; Schritt)`

### for-each-Schleife

Kürzer, wenn kein Index gebraucht wird:

```java
for (String name : namen) {
    System.out.println(name);
}
```

Lies: *"Für jeden String `name` in `namen` tue ..."*

### Häufiger Fehler: ArrayIndexOutOfBoundsException

```java
String[] namen = {"Cola", "Wasser"};   // Länge 2: Index 0 und 1
System.out.println(namen[2]);          // Fehler! Index 2 existiert nicht
```

Merke: Bei einem Array der Länge `n` sind gültige Indizes `0` bis `n-1`.

---

## Im Getränkeautomaten anwenden

Statt 5 einzelner Variablenpaare speichern wir alles in Arrays.
Das Menü wird per Schleife ausgegeben – kein Copy-Paste mehr!

```java
import java.util.Scanner;

public class GetraenkeListe {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // Arrays statt einzelner Variablen              NEU ←
        String[] namen   = {"Cola", "Apfelschorle", "Wasser", "Eistee", "Limo"};
        double[] preise  = {1.50, 1.00, 1.00, 1.20, 1.30};
        int[]    bestand = {5, 3, 5, 2, 4};

        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        System.out.println("Unser Angebot:");

        // Menü per Schleife – läuft automatisch für alle Einträge  NEU ←
        for (int i = 0; i < namen.length; i++) {
            if (bestand[i] > 0) {
                System.out.println("  " + (i + 1) + " - "
                    + namen[i] + "  " + preise[i] + " EUR"
                    + "  (noch " + bestand[i] + " Dosen)");
            }
        }

        System.out.println();
        System.out.print("Deine Wahl (1-5): ");
        int wahl  = scanner.nextInt();
        int index = wahl - 1;   // Array ist 0-basiert!

        if (index >= 0 && index < namen.length && bestand[index] > 0) {
            System.out.println("Du hast gewaehlt: " + namen[index]);
            System.out.println("Preis: " + preise[index] + " EUR");
        } else {
            System.out.println("Ungueltige Wahl oder ausverkauft.");
        }

        scanner.close();
    }
}
```

Beispiel-Ausgabe:

```
Unser Angebot:
  1 - Cola          1.5 EUR  (noch 5 Dosen)
  2 - Apfelschorle  1.0 EUR  (noch 3 Dosen)
  3 - Wasser        1.0 EUR  (noch 5 Dosen)
  4 - Eistee        1.2 EUR  (noch 2 Dosen)
  5 - Limo          1.3 EUR  (noch 4 Dosen)
```

---

## Aufgabe

Füge ein sechstes Getränk **"Sprudel"** für **0,90 EUR** mit Bestand **3** zu den Arrays hinzu. Das Menü soll es automatisch anzeigen.

## Lösung

```java
String[] namen   = {"Cola", "Apfelschorle", "Wasser", "Eistee", "Limo", "Sprudel"};
double[] preise  = {1.50, 1.00, 1.00, 1.20, 1.30, 0.90};
int[]    bestand = {5, 3, 5, 2, 4, 3};
```

Die Schleife läuft automatisch bis `namen.length` – keine weitere Anpassung nötig!

---

## Merksätze

1. Ein Array speichert viele Werte des gleichen Typs in einer Variablen.
2. Die Indizes beginnen bei **0** – letzter Index ist `länge - 1`.
3. `array.length` gibt die Anzahl der Elemente zurück.
4. `for (int i = 0; i < array.length; i++)` läuft durch alle Elemente mit Index.
5. `for (Typ x : array)` ist kürzer, wenn kein Index gebraucht wird.
