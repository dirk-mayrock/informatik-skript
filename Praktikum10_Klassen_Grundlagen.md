# Praktikum 10: Klassen – Grundlagen

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Den vollständigen prozeduralen Automaten mit Methoden
**Heute lernen wir:** Eigene Klassen mit Attributen und Konstruktor definieren
**Danach können wir:** Ein `Getraenk`-Objekt anlegen – kein Array-Chaos mehr
:::

---

## Neue Syntax

### Klasse definieren

Eine **Klasse** ist ein Bauplan. Sie beschreibt, welche **Attribute** (Eigenschaften) und **Methoden** (Fähigkeiten) ein Objekt haben soll.

```java
public class Getraenk {
    // Attribute
    String name;
    double preis;
    int    bestand;
}
```

### Konstruktor

Ein **Konstruktor** initialisiert ein Objekt beim Erstellen. Er heißt genauso wie die Klasse:

```java
public class Getraenk {
    String name;
    double preis;
    int    bestand;

    // Konstruktor
    public Getraenk(String name, double preis, int bestand) {
        this.name    = name;     // this = dieses Objekt
        this.preis   = preis;
        this.bestand = bestand;
    }
}
```

`this` unterscheidet den **Attribut-Namen** vom **Parameter-Namen**, wenn beide gleich heißen.

### Objekt erzeugen mit `new`

```java
Getraenk cola = new Getraenk("Cola", 1.50, 5);
```

| Teil | Bedeutung |
|------|-----------|
| `Getraenk` | Typ (Klasse) |
| `cola` | Variablenname des Objekts |
| `new Getraenk(...)` | Konstruktor aufrufen → Objekt erstellen |

### Auf Attribute zugreifen

```java
System.out.println(cola.name);     // "Cola"
System.out.println(cola.preis);    // 1.5
cola.bestand = 4;                  // Wert ändern
```

### Methoden in einer Klasse

```java
public class Getraenk {
    String name;
    double preis;
    int bestand;

    public Getraenk(String name, double preis, int bestand) {
        this.name = name; this.preis = preis; this.bestand = bestand;
    }

    public void zeigeInfo() {
        System.out.println(name + "  " + preis + " EUR  (" + bestand + " Dosen)");
    }

    public boolean istVerfuegbar() {
        return bestand > 0;
    }
}
```

Aufruf: `cola.zeigeInfo();`

---

## Im Getränkeautomaten anwenden

Statt drei paralleler Arrays ein Array von `Getraenk`-Objekten:

**Früher (P6–P9):**
```java
String[] namen   = {"Cola", ...};
double[] preise  = {1.50, ...};
int[]    bestand = {5, ...};
// Zugriff: namen[i], preise[i], bestand[i]
```

**Jetzt (P10):**
```java
Getraenk[] automat = new Getraenk[5];
automat[0] = new Getraenk("Cola",         1.50, 5);   // NEU ←
automat[1] = new Getraenk("Apfelschorle", 1.00, 3);
automat[2] = new Getraenk("Wasser",       1.00, 5);
automat[3] = new Getraenk("Eistee",       1.20, 2);
automat[4] = new Getraenk("Limo",         1.30, 4);

// Zugriff: automat[i].name, automat[i].preis, automat[i].bestand
for (int i = 0; i < automat.length; i++) {
    if (automat[i].istVerfuegbar()) {
        System.out.print((i+1) + " - ");
        automat[i].zeigeInfo();
    }
}
```

Vorteile:
- Ein Objekt enthält **alle Informationen eines Getränks** zusammen.
- Methoden wie `istVerfuegbar()` gehören direkt zum Objekt.
- Kein versehentliches Vertauschen von Indizes mehr.

---

## Klasse vs. Objekt – Vergleich

```
Klasse Getraenk        → Bauplan: "Ein Getränk hat Name, Preis, Bestand"
Objekt automat[0]      → konkretes Exemplar: Cola, 1.50 EUR, 5 Dosen
Objekt automat[1]      → konkretes Exemplar: Apfelschorle, 1.00 EUR, 3 Dosen
```

---

## Aufgabe

Füge der Klasse `Getraenk` eine Methode `ausgeben()` hinzu, die den Bestand um 1 reduziert und `true` zurückgibt wenn das möglich war, sonst `false`.

## Lösung

```java
public boolean ausgeben() {
    if (bestand > 0) {
        bestand--;
        return true;
    }
    return false;
}
```

Aufruf:

```java
if (automat[0].ausgeben()) {
    System.out.println("Cola ausgegeben!");
}
```

---

## Merksätze

1. Eine **Klasse** ist ein Bauplan – ein **Objekt** ist ein konkretes Exemplar.
2. Attribute beschreiben die Eigenschaften, Methoden die Fähigkeiten eines Objekts.
3. Der **Konstruktor** heißt wie die Klasse und initialisiert das Objekt.
4. `this` verweist auf das aktuelle Objekt – nötig wenn Parameter und Attribut gleich heißen.
5. `new Klasse(...)` erzeugt ein neues Objekt und ruft den Konstruktor auf.
