# Praktikum 4: Bedingungen

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Nutzereingaben lesen
**Heute lernen wir:** if / else if / else – Entscheidungen treffen
**Danach können wir:** Prüfen ob der Nutzer genug Geld eingeworfen hat
:::

---

## Neue Syntax

### if / else if / else

```java
if (Bedingung) {
    // wird ausgeführt wenn Bedingung wahr ist
} else if (andereBedingung) {
    // wird ausgeführt wenn andereBedingung wahr ist
} else {
    // wird ausgeführt wenn keine Bedingung zutrifft
}
```

Nur **ein** Block wird ausgeführt – der erste, dessen Bedingung `true` ist.

### Vergleichsoperatoren

| Operator | Bedeutung | Beispiel |
|----------|-----------|---------|
| `==` | gleich | `a == 5` |
| `!=` | ungleich | `a != 0` |
| `>` | größer | `betrag > preis` |
| `<` | kleiner | `alter < 18` |
| `>=` | größer oder gleich | `punkte >= 60` |
| `<=` | kleiner oder gleich | `i <= 10` |

Achtung: `=` ist **Zuweisung**, `==` ist **Vergleich**!

### Logische Operatoren

| Operator | Bedeutung | Beispiel |
|----------|-----------|---------|
| `&&` | UND | `alter >= 18 && hatAusweis` |
| `\|\|` | ODER | `istAdmin \|\| istLehrer` |
| `!` | NICHT | `!istGesperrt` |

```java
if (betrag >= preis && bestand > 0) {
    System.out.println("Kauf moeglich!");
}
```

---

## Im Getränkeautomaten anwenden

Wir prüfen, ob der eingeworfene Betrag für das gewählte Getränk reicht:

```java
import java.util.Scanner;

public class Bedingungen {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        double preis = 1.50;   // Preis für Cola

        System.out.print("Wieviel Geld hast du eingeworfen (z.B. 1.50)? ");
        double eingeworfenerBetrag = scanner.nextDouble();

        if (eingeworfenerBetrag >= preis) {                   // NEU ←
            double rueckgeld = eingeworfenerBetrag - preis;
            System.out.println("Getraenk wird ausgegeben!");
            System.out.println("Rueckgeld: " + rueckgeld + " EUR");
        } else if (eingeworfenerBetrag > 0) {                 // NEU ←
            double fehlenderBetrag = preis - eingeworfenerBetrag;
            System.out.println("Nicht genug Geld!");
            System.out.println("Bitte noch " + fehlenderBetrag + " EUR einwerfen.");
        } else {                                              // NEU ←
            System.out.println("Kein Geld eingeworfen.");
        }

        scanner.close();
    }
}
```

Beispiel mit 2.00 EUR eingegeben:

```
Wieviel Geld hast du eingeworfen (z.B. 1.50)? 2.00
Getraenk wird ausgegeben!
Rueckgeld: 0.5 EUR
```

Beispiel mit 1.00 EUR eingegeben:

```
Wieviel Geld hast du eingeworfen (z.B. 1.50)? 1.00
Nicht genug Geld!
Bitte noch 0.5 EUR einwerfen.
```

---

## Aufgabe

Ergänze die Bedingung: Wenn `eingeworfenerBetrag` **genau** gleich `preis` ist, soll eine besondere Nachricht erscheinen:

```
Passend bezahlt – kein Rueckgeld!
```

## Lösung

```java
if (eingeworfenerBetrag == preis) {
    System.out.println("Getraenk wird ausgegeben!");
    System.out.println("Passend bezahlt – kein Rueckgeld!");
} else if (eingeworfenerBetrag > preis) {
    double rueckgeld = eingeworfenerBetrag - preis;
    System.out.println("Getraenk wird ausgegeben!");
    System.out.println("Rueckgeld: " + rueckgeld + " EUR");
} else {
    System.out.println("Nicht genug Geld!");
}
```

---

## Merksätze

1. `if` prüft eine Bedingung – nur wenn sie `true` ist, wird der Block ausgeführt.
2. `else if` wird geprüft wenn alle vorherigen Bedingungen `false` waren.
3. `else` fängt alle verbleibenden Fälle ab.
4. `=` ist Zuweisung, `==` ist Vergleich – Verwechslung ist ein häufiger Fehler!
5. Mehrere Bedingungen kombinieren: `&&` (beide wahr), `||` (mind. eine wahr).
