# Thema 12: Struktogramme und Ablaufpläne

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung: Warum Algorithmen visualisieren?

Ein Algorithmus ist eine schrittweise Beschreibung, wie ein Problem gelöst wird.

Bevor man Code schreibt, hilft es, den Algorithmus grafisch darzustellen.

Vorteile:
- Programmiersprachen-unabhängig (funktioniert für Java, Python, C, ...)
- Logikfehler sind leichter zu erkennen
- Kommunikation im Team wird einfacher

Es gibt zwei verbreitete Darstellungsformen:

```
1. Ablaufplan (Flussdiagramm) → DIN 66001
2. Struktogramm (Nassi-Shneiderman-Diagramm) → DIN 66261
```

---

## Teil 1: Ablaufpläne (Flussdiagramme)

### Symbole

| Symbol | Form | Bedeutung |
|--------|------|-----------|
| Start/Ende | Abgerundetes Rechteck | Beginn und Ende des Algorithmus |
| Anweisung | Rechteck | Eine Aktion, Berechnung |
| Entscheidung | Raute | Eine Ja/Nein-Frage |
| Ein-/Ausgabe | Parallelogramm | Einlesen oder Ausgeben |
| Verbindungspfeil | Pfeil | Richtung des Ablaufs |

---

### Beispiel: Ablaufplan „Prüfe ob eine Zahl gerade ist"

```
     ┌─────────┐
     │  Start  │
     └────┬────┘
          │
     ┌────▼────────────┐
     │  Lies Zahl n    │
     └────┬────────────┘
          │
     ┌────▼────────────────┐
     │   n mod 2 = 0?      │
     └────┬──────────┬─────┘
         Ja         Nein
          │          │
  ┌───────▼───┐  ┌───▼───────────┐
  │  Ausgabe: │  │  Ausgabe:     │
  │  "gerade" │  │  "ungerade"   │
  └───────┬───┘  └───────┬───────┘
          └──────┬────────┘
                 │
            ┌────▼────┐
            │  Ende   │
            └─────────┘
```

---

### Schleifen im Ablaufplan

Eine while-Schleife sieht so aus:

```
          │
     ┌────▼────────────────┐
     │   Bedingung?         │◄───────────┐
     └────┬──────────┬─────┘            │
         Ja         Nein                │
          │          │                  │
  ┌───────▼────┐     │           ┌──────┴────────┐
  │  Schleife- │     │           │  Nächster     │
  │  rumpf     │─────────────────►  Durchlauf    │
  └────────────┘                 └───────────────┘
                   │
              ┌────▼────┐
              │  weiter │
              └─────────┘
```

---

## Teil 2: Struktogramme (Nassi-Shneiderman)

Struktogramme wurden 1973 von Nassi und Shneiderman entwickelt.

Im Gegensatz zu Ablaufplänen haben Struktogramme **keine Sprünge** (kein `goto`).

Der Kontrollfluss ist immer von oben nach unten.

---

### Anweisung

```
┌─────────────────────────────┐
│  Anweisung                  │
└─────────────────────────────┘
```

---

### Einfache Verzweigung (if)

```
┌────────────────────────────────────┐
│  Bedingung?                        │
├──────────────────┬─────────────────┤
│  Ja              │  Nein           │
│  Anweisung A     │  Anweisung B    │
└──────────────────┴─────────────────┘
```

---

### Einseitige Verzweigung (if ohne else)

```
┌────────────────────────────────────┐
│  Bedingung?                        │
├──────────────────┬─────────────────┤
│  Ja              │                 │
│  Anweisung A     │                 │
└──────────────────┴─────────────────┘
```

---

### While-Schleife (kopfgesteuert)

```
┌─────────────────────────────────────┐
│  SOLANGE Bedingung                  │
│ ┌───────────────────────────────┐   │
│ │  Schleifenrumpf               │   │
│ └───────────────────────────────┘   │
└─────────────────────────────────────┘
```

---

### Do-While-Schleife (fußgesteuert)

```
┌─────────────────────────────────────┐
│ ┌───────────────────────────────┐   │
│ │  Schleifenrumpf               │   │
│ └───────────────────────────────┘   │
│  SOLANGE Bedingung                  │
└─────────────────────────────────────┘
```

---

### For-Schleife

```
┌─────────────────────────────────────┐
│  FÜR i VON 0 BIS n-1               │
│ ┌───────────────────────────────┐   │
│ │  Schleifenrumpf               │   │
│ └───────────────────────────────┘   │
└─────────────────────────────────────┘
```

---

## Vollständiges Beispiel: Summe der Zahlen 1 bis n

Algorithmus:

```
1. Lies n ein
2. Setze summe = 0
3. Setze i = 1
4. Solange i <= n:
   4a. summe = summe + i
   4b. i = i + 1
5. Gib summe aus
```

### Struktogramm

```
┌─────────────────────────────────────────┐
│  Lies n                                 │
├─────────────────────────────────────────┤
│  summe = 0                              │
├─────────────────────────────────────────┤
│  i = 1                                  │
├─────────────────────────────────────────┤
│  SOLANGE i <= n                         │
│ ┌───────────────────────────────────┐   │
│ │  summe = summe + i                │   │
│ ├───────────────────────────────────┤   │
│ │  i = i + 1                        │   │
│ └───────────────────────────────────┘   │
├─────────────────────────────────────────┤
│  Ausgabe: summe                         │
└─────────────────────────────────────────┘
```

### Zugehöriger Java-Code

```java
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int summe = 0;
int i = 1;
while (i <= n) {
    summe = summe + i;
    i++;
}
System.out.println(summe);
```

---

## Vergleich: Ablaufplan vs. Struktogramm

| Eigenschaft         | Ablaufplan           | Struktogramm           |
|---------------------|----------------------|------------------------|
| Darstellung         | Grafisch mit Pfeilen | Verschachtelte Kästen  |
| Sprünge möglich?    | Ja (goto)            | Nein                   |
| Lesbarkeit          | Gut für einfache Fälle | Gut für komplexe Fälle |
| Norm                | DIN 66001            | DIN 66261              |
| Schachtelung        | Schwerer erkennbar   | Deutlich sichtbar      |

---

## Verbindung zu anderen Themen

- **Thema 9 (Java):** Struktogramme und Ablaufpläne zeigen, wie Java-Code aufgebaut werden soll.
- **Thema 13 (Sortieralgorithmen):** Sortieralgorithmen werden oft zuerst als Struktogramm beschrieben.
- **Thema 10 (Softwareentwicklung):** In der Entwurfsphase werden Algorithmen grafisch geplant.

---

## Typische Klausuraufgaben

### Aufgabe 1

Zeichne ein Struktogramm für folgenden Java-Code:

```java
int max = a;
if (b > a) {
    max = b;
}
System.out.println(max);
```

#### Lösung

```
┌─────────────────────────────────────────┐
│  max = a                                │
├─────────────────────────────────────────┤
│  b > a ?                                │
├─────────────────────────┬───────────────┤
│  Ja                     │  Nein         │
│  max = b                │               │
└─────────────────────────┴───────────────┘
┌─────────────────────────────────────────┐
│  Ausgabe: max                           │
└─────────────────────────────────────────┘
```

---

### Aufgabe 2

Erstelle ein Struktogramm, das alle geraden Zahlen von 2 bis 20 ausgibt.

#### Lösung

```
┌─────────────────────────────────────────┐
│  i = 2                                  │
├─────────────────────────────────────────┤
│  SOLANGE i <= 20                        │
│ ┌───────────────────────────────────┐   │
│ │  Ausgabe: i                       │   │
│ ├───────────────────────────────────┤   │
│ │  i = i + 2                        │   │
│ └───────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

---

## Merksätze

1. Ablaufpläne verwenden standardisierte Symbole (Raute = Entscheidung).
2. Struktogramme haben keine Sprünge — der Ablauf ist immer von oben nach unten.
3. While-Schleife im Struktogramm: Bedingung steht oben.
4. Do-While-Schleife: Bedingung steht unten — Rumpf wird mindestens einmal ausgeführt.
5. Struktogramme eignen sich besonders gut für die Entwurfsphase.
6. Aus einem Struktogramm lässt sich direkt Java-Code ableiten.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 8/10
**Verständlichkeit:** 9/10
