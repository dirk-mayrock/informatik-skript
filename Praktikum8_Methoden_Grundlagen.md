# Praktikum 8: Methoden – Grundlagen

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Münzen einwerfen (while), Menü ausgeben (for), Getränk wählen (switch)
**Heute lernen wir:** Methoden – Code in wiederverwendbare Bausteine aufteilen
**Danach können wir:** zeigeMenu() und berechneBetrag() als eigene Methoden auslagern
:::

---

## Neue Syntax

### Methode deklarieren

```java
public static void methodenName() {
    // Code der Methode
}
```

| Teil | Bedeutung |
|------|-----------|
| `public` | Von überall aufrufbar |
| `static` | Gehört zur Klasse, nicht zu einem Objekt (nötig solange kein OOP) |
| `void` | Die Methode gibt keinen Wert zurück |
| `methodenName` | Name der Methode (beginnt mit Kleinbuchstabe) |
| `()` | Parameter-Liste (hier leer) |

### Methode mit Parameter

```java
public static void begruesse(String name) {
    System.out.println("Hallo, " + name + "!");
}
```

Aufruf: `begruesse("Hannah");`

### Methode mit Rückgabewert

```java
public static int addiere(int a, int b) {
    return a + b;   // return gibt den Wert zurück
}
```

Aufruf: `int ergebnis = addiere(3, 4);`

Der Rückgabetyp steht statt `void` → hier `int`.

### Methode aufrufen

```java
public static void main(String[] args) {
    sagHallo();                  // void-Methode aufrufen
    begruesse("Hannah");         // mit Parameter
    int s = addiere(3, 4);       // mit Rückgabewert
}
```

### Warum Methoden?

Ohne Methode:

```java
// An drei verschiedenen Stellen im Code:
System.out.println("======");
System.out.println(" Menü");
System.out.println("======");
// ... (10 Zeilen Menü-Code)
// ... (10 Zeilen Menü-Code)
// ... (10 Zeilen Menü-Code)
```

Mit Methode:

```java
zeigeMenu();   // einmal definiert, dreimal aufgerufen – keine Wiederholung
```

---

## Im Getränkeautomaten anwenden

Wir lagern die Menü-Ausgabe und die Münz-Addition in Methoden aus:

```java
public class MethodenGrundlagen {

    // --- Menü ausgeben (Methode) ---                  NEU ←
    public static void zeigeMenu(String[] namen, double[] preise, int[] bestand) {
        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        for (int i = 0; i < namen.length; i++) {
            if (bestand[i] > 0) {
                System.out.println("  " + (i+1) + " - "
                    + namen[i] + "  " + preise[i] + " EUR");
            }
        }
        System.out.println();
    }

    // --- Münze zum Betrag addieren (Methode) ---      NEU ←
    public static double addiereMuenze(double betrag, double muenze) {
        return betrag + muenze;
    }

    // --- Hauptprogramm ---
    public static void main(String[] args) {
        String[] namen   = {"Cola", "Apfelschorle", "Wasser", "Eistee", "Limo"};
        double[] preise  = {1.50, 1.00, 1.00, 1.20, 1.30};
        int[]    bestand = {5, 3, 5, 2, 4};

        zeigeMenu(namen, preise, bestand);   // Einzeiler!  NEU ←

        double betrag = 0.0;
        betrag = addiereMuenze(betrag, 1.00);
        betrag = addiereMuenze(betrag, 0.50);
        System.out.println("Eingeworfen: " + betrag + " EUR");
    }
}
```

---

## Aufgabe

Schreibe eine Methode `gibNachricht(double betrag, double preis)`, die folgendes ausgibt:
- Wenn genug Geld: `"Getraenk wird ausgegeben!"`
- Sonst: `"Bitte mehr Geld einwerfen."`

## Lösung

```java
public static void gibNachricht(double betrag, double preis) {
    if (betrag >= preis) {
        System.out.println("Getraenk wird ausgegeben!");
    } else {
        System.out.println("Bitte mehr Geld einwerfen.");
    }
}
```

Aufruf: `gibNachricht(1.50, 1.50);`

---

## Merksätze

1. Eine Methode fasst zusammengehörigen Code unter einem Namen zusammen.
2. `void` = kein Rückgabewert; statt `void` steht der Typ des Rückgabewerts.
3. Parameter sind Variablen, die beim Aufruf einen Wert erhalten.
4. `return` gibt einen Wert zurück und beendet die Methode sofort.
5. Methoden vermeiden Code-Wiederholung und machen Programme lesbarer.
