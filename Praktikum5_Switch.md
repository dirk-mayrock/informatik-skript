# Praktikum 5: switch

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Mit if/else Entscheidungen treffen
**Heute lernen wir:** switch – elegante Auswahl bei festen Werten
**Danach können wir:** Getränke per Nummer (1–5) sauber auswählen
:::

---

## Neue Syntax

### switch

```java
switch (ausdruck) {
    case wert1:
        // Code für wert1
        break;
    case wert2:
        // Code für wert2
        break;
    default:
        // Code wenn kein case passt
}
```

| Teil | Bedeutung |
|------|-----------|
| `switch (x)` | Welche Variable wird verglichen? |
| `case 3:` | Wenn x == 3, führe diesen Block aus |
| `break;` | Verlässt den switch – ohne `break` "fällt" der Code zum nächsten `case` durch! |
| `default:` | Wird ausgeführt wenn kein `case` passt (wie `else`) |

### Wann switch statt if-else?

- `switch` ist besser lesbar wenn **viele feste Einzelwerte** geprüft werden.
- `if-else` ist besser wenn Bereichsprüfungen nötig sind (z.B. `> 100`).

```java
// switch: gut für feste Werte
switch (wahl) {
    case 1: ...   case 2: ...   case 3: ...
}

// if-else: besser für Bereiche
if (punkte >= 90) { ... }
else if (punkte >= 75) { ... }
```

### Vergessen von `break` – Durchfall-Effekt

```java
int x = 2;
switch (x) {
    case 1: System.out.println("eins");
    case 2: System.out.println("zwei");   // kein break!
    case 3: System.out.println("drei");
}
// Ausgabe: "zwei"  UND  "drei"  ← Durchfall!
```

---

## Im Getränkeautomaten anwenden

```java
import java.util.Scanner;

public class SwitchBeispiel {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Unser Angebot:");
        System.out.println("  1 - Cola          1.50 EUR");
        System.out.println("  2 - Apfelschorle  1.00 EUR");
        System.out.println("  3 - Wasser        1.00 EUR");
        System.out.println("  4 - Eistee        1.20 EUR");
        System.out.println("  5 - Limo          1.30 EUR");

        System.out.print("Deine Wahl (1-5): ");
        int wahl = scanner.nextInt();

        String gewaehltesGetraenk;
        double gewaehlterPreis;

        switch (wahl) {                           // NEU ←
            case 1:
                gewaehltesGetraenk = "Cola";
                gewaehlterPreis    = 1.50;
                break;
            case 2:
                gewaehltesGetraenk = "Apfelschorle";
                gewaehlterPreis    = 1.00;
                break;
            case 3:
                gewaehltesGetraenk = "Wasser";
                gewaehlterPreis    = 1.00;
                break;
            case 4:
                gewaehltesGetraenk = "Eistee";
                gewaehlterPreis    = 1.20;
                break;
            case 5:
                gewaehltesGetraenk = "Limo";
                gewaehlterPreis    = 1.30;
                break;
            default:                              // NEU ←
                gewaehltesGetraenk = "Unbekannt";
                gewaehlterPreis    = 0.00;
                System.out.println("Ungueltige Auswahl!");
        }

        if (!gewaehltesGetraenk.equals("Unbekannt")) {
            System.out.println("Du hast gewaehlt: " + gewaehltesGetraenk);
            System.out.println("Preis: " + gewaehlterPreis + " EUR");
        }

        scanner.close();
    }
}
```

Beispiel-Sitzung:

```
Deine Wahl (1-5): 4
Du hast gewaehlt: Eistee
Preis: 1.2 EUR
```

---

## Aufgabe

Füge ein sechstes Getränk **"Sprudel"** für **0,90 EUR** (Taste `6`) in den switch ein.

## Lösung

```java
case 6:
    gewaehltesGetraenk = "Sprudel";
    gewaehlterPreis    = 0.90;
    break;
```

Und ergänze das Menü mit `System.out.println("  6 - Sprudel        0.90 EUR");`.

---

## Merksätze

1. `switch` vergleicht einen Wert gegen mehrere feste `case`-Werte.
2. Jeder `case`-Block **muss** mit `break;` enden – sonst läuft der Code in den nächsten `case` weiter.
3. `default` fängt alle Werte auf, die kein `case` abdeckt.
4. `switch` funktioniert mit `int`, `char`, `String` und einigen anderen Typen.
5. Bei Bereichen (`> 100`) ist `if-else` besser geeignet als `switch`.
