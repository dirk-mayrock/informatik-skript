# Praktikum 11: OOP – Vollständiger Getränkeautomat

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Klassen mit Attributen und Konstruktor definieren
**Heute lernen wir:** Kapselung (private/public), Getter/Setter, mehrere Klassen zusammen
**Danach können wir:** Den vollständigen OOP-Getränkeautomaten mit 3 Klassen
:::

---

## Neue Syntax

### Kapselung: private und public

Attribute sollten **nicht direkt von außen** zugänglich sein – sie werden `private` gemacht:

```java
public class Getraenk {
    private String name;   // von außen nicht änderbar
    private double preis;
    private int    bestand;
}
```

Zugriff nur über **Getter** und **Setter**:

```java
// Getter: Wert lesen
public String getName()  { return name; }
public double getPreis() { return preis; }
public int getBestand()  { return bestand; }

// Setter: Wert (kontrolliert) setzen
public void setBestand(int bestand) {
    if (bestand >= 0) {          // Prüfung vor Zuweisung!
        this.bestand = bestand;
    }
}
```

### Zugriffsmodifizierer

| Modifizierer | Sichtbar von |
|---|---|
| `private` | Nur innerhalb der eigenen Klasse |
| `public` | Überall |
| `protected` | Eigene Klasse + Unterklassen |

### `toString()` überschreiben

`toString()` wird automatisch aufgerufen wenn ein Objekt als Text ausgegeben wird:

```java
@Override
public String toString() {
    return String.format("%-15s %.2f EUR  (%d Dosen)", name, preis, bestand);
}
```

```java
Getraenk cola = new Getraenk("Cola", 1.50, 5);
System.out.println(cola);   // ruft toString() auf
// Ausgabe: Cola            1.50 EUR  (5 Dosen)
```

### Mehrere Klassen zusammen

Ein Programm kann aus mehreren Klassen bestehen. In BlueJ legt man für jede Klasse eine eigene `.java`-Datei im selben Projektordner an.

```
P11_OOP_Getraenkeautomat/
├── Getraenk.java   ← Klasse für ein Getränk
├── Geldfach.java   ← Klasse für das Geld
└── Automat.java    ← Hauptklasse (enthält main)
```

---

## Die drei Klassen im Überblick

### UML-Klassendiagramm

```
┌─────────────────────────┐       ┌──────────────────────────┐
│        Getraenk         │       │         Geldfach         │
├─────────────────────────┤       ├──────────────────────────┤
│ - name : String         │       │ - betrag : double        │
│ - preis : double        │       ├──────────────────────────┤
│ - bestand : int         │       │ + einwerfen(double)      │
├─────────────────────────┤       │ + abziehen(double)       │
│ + getName() : String    │       │ + zurueckgeben() : double│
│ + getPreis() : double   │       │ + wechselgeldAlsText()   │
│ + getBestand() : int    │       │ + toString()             │
│ + istVerfuegbar() : bool│       └──────────────────────────┘
│ + ausgeben() : bool     │                   ▲
│ + toString() : String   │                   │ verwendet
└─────────────────────────┘       ┌────────────┴─────────────┐
              ▲                   │          Automat         │
              │ verwendet         ├──────────────────────────┤
              └───────────────────│ - getraenke : Getraenk[] │
                                  │ - geldfach  : Geldfach   │
                                  ├──────────────────────────┤
                                  │ + zeigeMenu()            │
                                  │ + geldPhase() : bool     │
                                  │ + kaufPhase()            │
                                  │ + start()                │
                                  │ + main()                 │
                                  └──────────────────────────┘
```

---

## Klasse `Getraenk`

```java
public class Getraenk {

    private String name;
    private double preis;
    private int    bestand;

    public Getraenk(String name, double preis, int bestand) {
        this.name    = name;
        this.preis   = preis;
        this.bestand = bestand;
    }

    public String getName()    { return name; }
    public double getPreis()   { return preis; }
    public int    getBestand() { return bestand; }

    public boolean istVerfuegbar() { return bestand > 0; }

    public boolean ausgeben() {
        if (bestand > 0) { bestand--; return true; }
        return false;
    }

    @Override
    public String toString() {
        return String.format("%-15s %.2f EUR  (%d Dosen)", name, preis, bestand);
    }
}
```

---

## Klasse `Geldfach`

```java
public class Geldfach {

    private double betrag;
    private static final double[] MUENZEN = {2.00, 1.00, 0.50, 0.20, 0.10};

    public Geldfach() { this.betrag = 0.0; }

    public double getBetrag() { return betrag; }

    public boolean einwerfen(double muenze) {
        for (double m : MUENZEN) {
            if (Math.abs(muenze - m) < 0.001) {
                betrag += muenze;
                betrag = Math.round(betrag * 100) / 100.0;
                return true;
            }
        }
        return false;   // ungültige Münze
    }

    public void abziehen(double preis) {
        betrag -= preis;
        betrag = Math.round(betrag * 100) / 100.0;
    }

    public double zurueckgeben() {
        double r = betrag; betrag = 0.0; return r;
    }

    public String wechselgeldAlsText() {
        StringBuilder sb = new StringBuilder();
        int cents = (int) Math.round(betrag * 100);
        for (double m : MUENZEN) {
            int mc = (int) Math.round(m * 100);
            int n  = cents / mc;
            if (n > 0) {
                sb.append(n).append(" × ").append(String.format("%.2f", m))
                  .append(" EUR  ");
                cents -= n * mc;
            }
        }
        return sb.toString().trim();
    }

    @Override
    public String toString() { return String.format("%.2f EUR", betrag); }
}
```

---

## Klasse `Automat` (Hauptklasse)

```java
import java.util.Scanner;

public class Automat {

    private Getraenk[] getraenke;
    private Geldfach   geldfach;
    private Scanner    scanner;

    public Automat() {
        geldfach  = new Geldfach();
        scanner   = new Scanner(System.in);
        getraenke = new Getraenk[]{
            new Getraenk("Cola",         1.50, 5),
            new Getraenk("Apfelschorle", 1.00, 3),
            new Getraenk("Wasser",       1.00, 5),
            new Getraenk("Eistee",       1.20, 2),
            new Getraenk("Limo",         1.30, 4)
        };
    }

    public void start() {
        System.out.println("Willkommen beim Getraenkeautomaten!");
        boolean weiter = true;
        while (weiter) {
            zeigeMenu();
            if (geldPhase()) kaufPhase();
            System.out.print("Nochmal? (j/n): ");
            weiter = scanner.nextLine().equalsIgnoreCase("j");
        }
        System.out.println("Auf Wiedersehen!");
        scanner.close();
    }

    public static void main(String[] args) {
        new Automat().start();
    }

    // ... zeigeMenu(), geldPhase(), kaufPhase() wie in der .java-Datei
}
```

Der vollständige Code befindet sich in:
`java/P11_OOP_Getraenkeautomat/`

---

## Beispiel-Sitzung

```
Willkommen beim Getraenkeautomaten!
============================
 Getraenkeautomat  v2.0
============================
Unser Angebot:
  1 - Cola            1.50 EUR  (5 Dosen)
  2 - Apfelschorle    1.00 EUR  (3 Dosen)
  3 - Wasser          1.00 EUR  (5 Dosen)
  4 - Eistee          1.20 EUR  (2 Dosen)
  5 - Limo            1.30 EUR  (4 Dosen)

Muenzen einwerfen:
  Aktuell: 0.00 EUR  |  Muenze: 1.00
  Aktuell: 1.00 EUR  |  Muenze: 0.50
  Aktuell: 1.50 EUR  |  Muenze: 0

Gesamtbetrag: 1.50 EUR
Deine Wahl (1-5, 0 = Abbruch): 1
>>> Cola wird ausgegeben! <<<

Nochmal? (j/n): n
Auf Wiedersehen!
```

---

## Aufgabe

Erweitere den `Automat` um eine Methode `befuelleAlleGetraenke()`, die alle Getränke auf vollen Bestand auffüllt (nutze die `auffuellen()`-Methode aus `Getraenk`).

## Lösung

In `Getraenk.java`:

```java
public void auffuellen() {
    bestand = 5;   // MAX_BESTAND
}
```

In `Automat.java`:

```java
public void befuelleAlleGetraenke() {
    for (Getraenk g : getraenke) {
        g.auffuellen();
    }
    System.out.println("Alle Getraenke aufgefuellt.");
}
```

---

## Merksätze

1. `private` schützt Attribute vor unkontrolliertem Zugriff von außen.
2. Getter lesen, Setter setzen Attributwerte – sie können dabei prüfen ob der Wert gültig ist.
3. `@Override toString()` ermöglicht direkte Ausgabe eines Objekts mit `println`.
4. Mehrere Klassen im gleichen Projektordner können sich gegenseitig verwenden.
5. OOP macht Programme wartbarer: Änderung an `Getraenk` wirkt sich automatisch überall aus.
