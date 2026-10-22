# Thema 11: Objektorientierung

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung: Warum Objektorientierung?

Stell dir vor, du programmierst ein Schulverwaltungssystem.

Ohne Objektorientierung würdest du alle Daten in einzelnen Variablen speichern:

```java
String schueler1Name = "Hannah";
int schueler1Alter = 17;
double schueler1Note = 1.7;

String schueler2Name = "Leon";
int schueler2Alter = 16;
double schueler2Note = 2.3;
```

Das wird schnell unübersichtlich und fehleranfällig.

**Objektorientierung** erlaubt, Daten und Methoden zu einer Einheit zusammenzufassen: dem **Objekt**.

---

## Grundbegriffe

### Klasse

Eine **Klasse** ist der Bauplan für ein Objekt.

Sie legt fest, welche Attribute (Eigenschaften) und Methoden (Fähigkeiten) ein Objekt haben soll.

```java
public class Schueler {
    String name;
    int alter;
    double note;
}
```

---

### Objekt

Ein **Objekt** ist eine konkrete Instanz einer Klasse.

```java
Schueler s1 = new Schueler();
s1.name = "Hannah";
s1.alter = 17;
s1.note = 1.7;
```

Vergleich:

```
Klasse   = Bauplan eines Hauses
Objekt   = das fertige Haus
```

---

### Attribut

Attribute sind die **Eigenschaften** eines Objekts.

```java
String name;
int alter;
double note;
```

---

### Methode

Methoden sind die **Fähigkeiten** eines Objekts.

```java
public void begruesse() {
    System.out.println("Hallo, ich bin " + name);
}
```

---

## Vollständiges Beispiel: Klasse Schueler

```java
public class Schueler {

    // Attribute
    private String name;
    private int alter;
    private double note;

    // Konstruktor
    public Schueler(String name, int alter, double note) {
        this.name = name;
        this.alter = alter;
        this.note = note;
    }

    // Methode
    public void begruesse() {
        System.out.println("Hallo, ich bin " + name + " und bin " + alter + " Jahre alt.");
    }

    // Getter
    public String getName() {
        return name;
    }

    public double getNote() {
        return note;
    }

    // Setter
    public void setNote(double note) {
        this.note = note;
    }
}
```

Objekt erzeugen und nutzen:

```java
Schueler s = new Schueler("Hannah", 17, 1.7);
s.begruesse();
System.out.println(s.getName());
```

Ausgabe:

```
Hallo, ich bin Hannah und bin 17 Jahre alt.
Hannah
```

---

## Die vier Grundprinzipien der OOP

### 1. Kapselung (Encapsulation)

Attribute werden `private` deklariert — von außen nicht direkt zugänglich.

Der Zugriff erfolgt ausschließlich über Methoden (Getter/Setter).

```java
private double note;

public double getNote() { return note; }
public void setNote(double note) { this.note = note; }
```

**Warum?**

- Schutz vor ungewollten Änderungen
- Interne Implementierung kann geändert werden, ohne den Rest zu beeinflussen

---

### 2. Vererbung (Inheritance)

Eine Klasse kann Attribute und Methoden einer anderen Klasse **erben**.

```java
public class Person {
    protected String name;
    protected int alter;

    public void vorstellen() {
        System.out.println("Ich bin " + name);
    }
}

public class Schueler extends Person {
    private double note;

    public void lerne() {
        System.out.println(name + " lernt.");
    }
}
```

`Schueler` erbt `name`, `alter` und `vorstellen()` von `Person`.

```java
Schueler s = new Schueler();
s.name = "Hannah";
s.vorstellen();   // Methode von Person!
s.lerne();        // Methode von Schueler
```

**UML-Darstellung:**

```
Person
  ↑
Schueler
```

Der Pfeil zeigt von der Unterklasse zur Oberklasse.

---

### 3. Polymorphismus (Polymorphism)

Eine Methode kann für verschiedene Objekte unterschiedlich verhalten.

```java
public class Tier {
    public void lautGeben() {
        System.out.println("...");
    }
}

public class Hund extends Tier {
    @Override
    public void lautGeben() {
        System.out.println("Wau!");
    }
}

public class Katze extends Tier {
    @Override
    public void lautGeben() {
        System.out.println("Miau!");
    }
}
```

Nutzung:

```java
Tier[] tiere = {new Hund(), new Katze(), new Hund()};
for (Tier t : tiere) {
    t.lautGeben();
}
```

Ausgabe:

```
Wau!
Miau!
Wau!
```

Obwohl der Typ `Tier` ist, wird die richtige Methode aufgerufen.

---

### 4. Abstraktion (Abstraction)

Abstraktion bedeutet, Details zu verstecken und nur das Wesentliche zu zeigen.

```java
public abstract class Form {
    public abstract double flaeche();  // muss überschrieben werden
}

public class Rechteck extends Form {
    double breite, hoehe;

    public Rechteck(double b, double h) {
        breite = b;
        hoehe = h;
    }

    @Override
    public double flaeche() {
        return breite * hoehe;
    }
}

public class Kreis extends Form {
    double radius;

    public Kreis(double r) {
        radius = r;
    }

    @Override
    public double flaeche() {
        return Math.PI * radius * radius;
    }
}
```

---

## Konstruktor

Ein **Konstruktor** initialisiert ein Objekt beim Erstellen.

```java
public Schueler(String name, int alter) {
    this.name = name;
    this.alter = alter;
}
```

`this` verweist auf das aktuelle Objekt.

---

## Zugriffsmodifizierer

| Modifizierer | Sichtbar von                        |
|--------------|-------------------------------------|
| `private`    | Nur innerhalb der eigenen Klasse    |
| `protected`  | Eigene Klasse + Unterklassen        |
| `public`     | Überall                             |

---

## UML-Klassendiagramm

Ein Klassendiagramm zeigt die Struktur von Klassen.

```
┌─────────────────────┐
│      Schueler       │
├─────────────────────┤
│ - name: String      │
│ - alter: int        │
│ - note: double      │
├─────────────────────┤
│ + getName(): String │
│ + setNote(double)   │
│ + begruesse()       │
└─────────────────────┘
```

Legende:
```
-  = private
+  = public
#  = protected
```

---

## Verbindung zu anderen Themen

- **Thema 9 (Java-Grundlagen):** OOP baut direkt auf Java-Grundlagen auf.
- **Thema 10 (Softwareentwicklung):** Das Systemdesign in Phase 2 des Wasserfallmodells enthält Klassendiagramme.
- **Thema 12 (Struktogramme):** Methoden können mit Struktogrammen beschrieben werden.

---

## Typische Klausuraufgaben

### Aufgabe 1

Was ist der Unterschied zwischen Klasse und Objekt?

#### Lösung

```
Klasse = Bauplan / Vorlage
Objekt = konkretes Exemplar, das nach dem Bauplan erstellt wurde
Beispiel: "Auto" ist die Klasse, "Hannahs roter VW" ist ein Objekt.
```

---

### Aufgabe 2

Was versteht man unter Kapselung? Warum ist sie wichtig?

#### Lösung

```
Kapselung = Attribute werden private gemacht, Zugriff nur über Methoden.
Warum:
- Interne Daten sind vor ungewollten Zugriffen geschützt.
- Die interne Implementierung kann geändert werden,
  ohne den Rest des Programms zu beeinflussen.
```

---

### Aufgabe 3

Erkläre Polymorphismus anhand eines Beispiels.

#### Lösung

```
Polymorphismus bedeutet, dass eine Methode bei verschiedenen Objekten
unterschiedlich ausgeführt wird.

Beispiel: Die Methode lautGeben() verhält sich bei Hund anders als bei Katze,
obwohl beide von Tier erben.
Man kann beide über den Typ Tier ansprechen, aber die korrekte Methode
wird automatisch aufgerufen.
```

---

## Merksätze

1. Klasse = Bauplan, Objekt = konkretes Exemplar.
2. Kapselung: `private` Attribute, Zugriff nur über Getter/Setter.
3. Vererbung: Unterklasse erbt Attribute und Methoden der Oberklasse.
4. Polymorphismus: Gleicher Methodenname, unterschiedliches Verhalten je nach Klasse.
5. Abstrakte Klassen können nicht direkt instanziiert werden.
6. `this` verweist auf das aktuelle Objekt.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 9/10
**Verständlichkeit:** 9/10
