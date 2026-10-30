# Praktikum 2: Variablen und Datentypen

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Text auf der Konsole ausgeben
**Heute lernen wir:** Daten in Variablen speichern
**Danach können wir:** Namen, Preise und Bestände eines Getränks speichern
:::

---

## Neue Syntax

### Variable deklarieren und initialisieren

```java
Typ name = Wert;
```

```java
int    alter       = 17;
double preis       = 1.50;
String getraenk    = "Cola";
boolean istKalt    = true;
```

### Die wichtigsten Datentypen

| Typ | Beispiel | Speicher | Verwendung |
|-----|----------|----------|------------|
| `int` | `42`, `-7` | 32 Bit | Ganzzahlen |
| `double` | `3.14`, `1.50` | 64 Bit | Kommazahlen |
| `String` | `"Cola"` | variabel | Text |
| `boolean` | `true`, `false` | 1 Bit | Wahrheitswert |
| `char` | `'A'` | 16 Bit | einzelnes Zeichen |

### Variable in Ausgabe einbauen

```java
String name = "Hannah";
int alter = 17;
System.out.println("Name: " + name);
System.out.println("Alter: " + alter + " Jahre");
```

Der `+`-Operator verbindet Text → **String-Verkettung**.

### Wert ändern

```java
int alter = 17;
alter = 18;    // neuer Wert – kein "int" mehr davor!
```

### Rechnen mit Variablen

```java
int a = 10;
int b = 3;
System.out.println(a + b);   // 13
System.out.println(a - b);   // 7
System.out.println(a * b);   // 30
System.out.println(a / b);   // 3  ← Ganzzahldivision!
System.out.println(a % b);   // 1  ← Rest (Modulo)
```

Achtung: `10 / 3 = 3` – der Nachkommaanteil wird **abgeschnitten**, nicht gerundet.
Für genaue Division: mindestens ein `double` verwenden:

```java
double ergebnis = 10.0 / 3;   // 3.333...
```

---

## Im Getränkeautomaten anwenden

Wir speichern ein Getränk mit Name und Preis in Variablen:

```java
public class Variablen {
    public static void main(String[] args) {

        System.out.println("============================");
        System.out.println(" Willkommen beim");
        System.out.println(" Getraenkeautomaten!");
        System.out.println("============================");

        String getraenk1Name  = "Cola";
        double getraenk1Preis = 1.50;

        String getraenk2Name  = "Apfelschorle";
        double getraenk2Preis = 1.00;

        String getraenk3Name  = "Wasser";      // NEU ←
        double getraenk3Preis = 1.00;           // NEU ←

        System.out.println("Unser Angebot:");
        System.out.println("  " + getraenk1Name + "  " + getraenk1Preis + " EUR");
        System.out.println("  " + getraenk2Name + "  " + getraenk2Preis + " EUR");
        System.out.println("  " + getraenk3Name + "  " + getraenk3Preis + " EUR");
    }
}
```

Ausgabe:

```
============================
 Willkommen beim
 Getraenkeautomaten!
============================
Unser Angebot:
  Cola  1.5 EUR
  Apfelschorle  1.0 EUR
  Wasser  1.0 EUR
```

---

## Aufgabe

Füge ein viertes Getränk **"Orangensaft"** für **1,20 EUR** hinzu und gib es im Menü aus.

## Lösung

```java
String getraenk4Name  = "Orangensaft";
double getraenk4Preis = 1.20;
System.out.println("  " + getraenk4Name + "  " + getraenk4Preis + " EUR");
```

---

## Merksätze

1. Eine Variable muss erst **deklariert** (Typ + Name) und **initialisiert** (Wert zugewiesen) werden.
2. `int` für Ganzzahlen, `double` für Kommazahlen, `String` für Text, `boolean` für ja/nein.
3. `int / int` ergibt immer eine Ganzzahl – der Rest wird abgeschnitten.
4. `%` liefert den Rest der Ganzzahldivision.
5. Text und Variablen werden mit `+` verbunden.
