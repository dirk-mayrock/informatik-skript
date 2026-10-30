# Praktikum 7: while und do-while

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Arrays verwalten, Menü per Schleife ausgeben
**Heute lernen wir:** while und do-while – Schleifen ohne feste Anzahl an Durchläufen
**Danach können wir:** Münzen einwerfen bis der Nutzer "fertig" signalisiert, Abbruch ermöglichen
:::

---

## Neue Syntax

### while-Schleife

```java
while (Bedingung) {
    // wird wiederholt solange Bedingung true ist
}
```

```java
int i = 1;
while (i <= 5) {
    System.out.println(i);
    i++;
}
// Ausgabe: 1  2  3  4  5
```

Die Bedingung wird **vor** jedem Durchlauf geprüft. Ist sie von Anfang an `false`, wird der Block **kein einziges Mal** ausgeführt.

### do-while-Schleife

```java
do {
    // wird mindestens einmal ausgeführt
} while (Bedingung);
```

```java
int zahl;
do {
    System.out.print("Gib eine Zahl von 1-10 ein: ");
    zahl = scanner.nextInt();
    scanner.nextLine();
} while (zahl < 1 || zahl > 10);
```

Unterschied zu `while`: Der Block wird **zuerst** ausgeführt, dann wird die Bedingung geprüft.

### Endlosschleife mit break

Manchmal ist unklar, wann die Schleife enden soll – dann wird `while (true)` mit `break` kombiniert:

```java
while (true) {
    String eingabe = scanner.nextLine();
    if (eingabe.equals("ende")) {
        break;   // Schleife verlassen
    }
    System.out.println("Du sagtest: " + eingabe);
}
```

### Akkumulator-Muster

Werte in einer Variablen aufaddieren:

```java
double summe = 0.0;
while (...) {
    double wert = scanner.nextDouble();
    summe += wert;   // entspricht: summe = summe + wert
}
```

---

## Im Getränkeautomaten anwenden

Der Nutzer kann mehrere Münzen nacheinander einwerfen.
Nach jeder Münze wird der aktuelle Betrag angezeigt.
Eingabe `0` = fertig, `-1` = Abbruch.

```java
double gesamtBetrag = 0.0;
boolean abbruch = false;

System.out.println("Muenzen einwerfen (0 = fertig, -1 = Abbruch):");

while (true) {                                          // NEU ←
    System.out.print("  Aktuell: " + gesamtBetrag
        + " EUR  |  Muenze: ");
    double muenze = scanner.nextDouble();
    scanner.nextLine();

    if (muenze == -1) {
        abbruch = true;
        break;                                          // NEU ←
    } else if (muenze == 0) {
        break;
    } else if (muenze > 0) {
        gesamtBetrag += muenze;                         // NEU ← (Akkumulator)
        gesamtBetrag = Math.round(gesamtBetrag * 100) / 100.0;
    }
}

if (abbruch) {
    System.out.println("Abbruch! Rueckgabe: " + gesamtBetrag + " EUR");
} else {
    System.out.println("Gesamtbetrag: " + gesamtBetrag + " EUR");
    // ... weiter zur Getränkewahl
}
```

Beispiel-Sitzung:

```
Muenzen einwerfen (0 = fertig, -1 = Abbruch):
  Aktuell: 0.0 EUR  |  Muenze: 1.00
  Aktuell: 1.0 EUR  |  Muenze: 0.50
  Aktuell: 1.5 EUR  |  Muenze: 0
Gesamtbetrag: 1.5 EUR
```

---

## Aufgabe

Erweitere die Schleife: Nach maximal **5 Münzen** soll die Eingabe automatisch beendet werden, auch wenn der Nutzer noch mehr einwerfen möchte. Gib dann aus:

```
Maximale Muenzanzahl erreicht.
```

## Lösung

```java
int anzahlMuenzen = 0;

while (true) {
    if (anzahlMuenzen >= 5) {
        System.out.println("Maximale Muenzanzahl erreicht.");
        break;
    }
    System.out.print("Muenze: ");
    double muenze = scanner.nextDouble();
    scanner.nextLine();
    if (muenze == 0) break;
    if (muenze > 0) {
        gesamtBetrag += muenze;
        anzahlMuenzen++;
    }
}
```

---

## Merksätze

1. `while` prüft die Bedingung **vor** dem Block – 0 bis ∞ Durchläufe.
2. `do-while` prüft **nach** dem Block – mindestens 1 Durchlauf.
3. `while (true)` mit `break` verwenden, wenn das Abbruchkriterium in der Mitte des Blocks liegt.
4. `break` verlässt sofort die innerste Schleife.
5. Akkumulator-Muster: `summe += wert` – Werte in einer Variablen aufsammeln.
