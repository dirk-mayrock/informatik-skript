# Praktikum 3: Konsoleneingabe

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Variablen deklarieren und Werte ausgeben
**Heute lernen wir:** Eingaben vom Nutzer einlesen (Scanner)
**Danach können wir:** Den Nutzer nach seiner Getränkewahl fragen
:::

---

## Neue Syntax

### Scanner importieren und anlegen

```java
import java.util.Scanner;   // ganz oben in der Datei, vor der Klasse

Scanner scanner = new Scanner(System.in);
```

`import` lädt eine fertige Java-Bibliothek.
`new Scanner(System.in)` erzeugt ein Scanner-Objekt, das die Tastatureingabe liest.

### Eingabe lesen

| Methode | Was sie liest | Beispiel |
|---------|---------------|---------|
| `scanner.nextLine()` | Eine ganze Zeile (Text) | `"Hannah"` |
| `scanner.nextInt()` | Eine Ganzzahl | `42` |
| `scanner.nextDouble()` | Eine Kommazahl | `1.50` |

```java
System.out.print("Wie heisst du? ");
String name = scanner.nextLine();
System.out.println("Hallo, " + name + "!");
```

### `print` vs. `println`

```java
System.out.print("Deine Eingabe: ");   // kein Umbruch → Cursor bleibt in der Zeile
System.out.println("Fertig.");         // mit Umbruch
```

### Pufferbereinigung nach `nextInt()`

`nextInt()` liest die Zahl, lässt aber den Zeilenumbruch im Puffer. Das nächste `nextLine()` würde dann sofort eine leere Zeile lesen. Lösung:

```java
int zahl = scanner.nextInt();
scanner.nextLine();   // Puffer leeren ← immer nach nextInt()/nextDouble()
```

### Scanner schließen

```java
scanner.close();   // am Ende des Programms
```

---

## Im Getränkeautomaten anwenden

```java
import java.util.Scanner;

public class Konsoleneingabe {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);   // NEU ←

        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        System.out.println("Unser Angebot:");
        System.out.println("  1 - Cola          1.50 EUR");
        System.out.println("  2 - Apfelschorle  1.00 EUR");
        System.out.println("  3 - Wasser        1.00 EUR");
        System.out.println();

        System.out.print("Welches Getraenk moechtest du? (Nummer eingeben): ");
        int wahl = scanner.nextInt();               // NEU ←
        System.out.println("Du hast Getraenk Nr. " + wahl + " gewaehlt.");

        scanner.close();
    }
}
```

Beispiel-Sitzung:

```
============================
 Getraenkeautomat
============================
Unser Angebot:
  1 - Cola          1.50 EUR
  2 - Apfelschorle  1.00 EUR
  3 - Wasser        1.00 EUR

Welches Getraenk moechtest du? (Nummer eingeben): 2
Du hast Getraenk Nr. 2 gewaehlt.
```

---

## Aufgabe

Erweitere das Programm: Nach der Getränkewahl soll der Nutzer auch seinen **Namen** eingeben. Das Programm soll dann ausgeben:

```
Danke, Hannah! Du hast Getraenk Nr. 2 gewaehlt.
```

## Lösung

```java
System.out.print("Welches Getraenk? ");
int wahl = scanner.nextInt();
scanner.nextLine();   // Puffer leeren

System.out.print("Dein Name? ");
String name = scanner.nextLine();

System.out.println("Danke, " + name + "! Du hast Getraenk Nr. " + wahl + " gewaehlt.");
```

---

## Merksätze

1. `import java.util.Scanner;` steht ganz oben, vor der Klasse.
2. `new Scanner(System.in)` erstellt das Eingabe-Objekt.
3. `nextLine()` → Text, `nextInt()` → Ganzzahl, `nextDouble()` → Kommazahl.
4. Nach `nextInt()` oder `nextDouble()` immer `scanner.nextLine()` aufrufen (Puffer leeren).
5. `scanner.close()` am Ende nicht vergessen.
