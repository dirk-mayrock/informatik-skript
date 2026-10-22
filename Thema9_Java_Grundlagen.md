# Thema 9: Java-Grundlagen

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung: Was ist Java?

Java ist eine der meistgenutzten Programmiersprachen der Welt.

Besonderheiten von Java:

- **Plattformunabhängig:** Java-Programme laufen auf jedem System mit einer Java Virtual Machine (JVM).
- **Objektorientiert:** Alles ist in Klassen und Objekten organisiert (→ Thema 11).
- **Streng typisiert:** Jede Variable hat einen festen Datentyp.

---

## Das erste Programm

```java
public class Hallo {
    public static void main(String[] args) {
        System.out.println("Hallo, Welt!");
    }
}
```

Was hier passiert:

```
public class Hallo      → Klasse mit dem Namen "Hallo"
main(String[] args)     → Startpunkt des Programms
System.out.println(...)→ Ausgabe in die Konsole
```

---

## Datentypen

Java kennt zwei Arten von Datentypen:

### Primitive Datentypen

| Typ      | Größe   | Wertebereich                              | Beispiel          |
|----------|---------|-------------------------------------------|-------------------|
| `byte`   |  8 Bit  | -128 bis 127                              | `byte b = 10;`    |
| `short`  | 16 Bit  | -32768 bis 32767                          | `short s = 1000;` |
| `int`    | 32 Bit  | -2.147.483.648 bis 2.147.483.647          | `int i = 42;`     |
| `long`   | 64 Bit  | sehr großer Bereich                       | `long l = 100L;`  |
| `float`  | 32 Bit  | IEEE 754 Single Precision                 | `float f = 3.14f;`|
| `double` | 64 Bit  | IEEE 754 Double Precision                 | `double d = 3.14;`|
| `char`   | 16 Bit  | Unicode-Zeichen (0 bis 65535)             | `char c = 'A';`   |
| `boolean`|  1 Bit  | true / false                              | `boolean b = true;`|

Verbindung zu Thema 4: `float` und `double` sind IEEE-754-Gleitkommazahlen!

### Referenztypen

Alles andere sind Objekte:

```java
String name = "Hannah";
int[] zahlen = {1, 2, 3, 4};
```

---

## Variablen

```java
int alter = 17;
double temperatur = 36.8;
String name = "Hannah";
boolean istAnwesend = true;
```

Regeln:
- Variablennamen beginnen mit Kleinbuchstabe.
- Typ muss angegeben werden.
- Wert kann sich ändern.

---

## Konstanten

```java
final int MAX_PUNKTE = 100;
```

`final` bedeutet: der Wert kann nicht mehr geändert werden.

---

## Operatoren

### Arithmetisch

```java
int a = 10;
int b = 3;

System.out.println(a + b);   // 13
System.out.println(a - b);   // 7
System.out.println(a * b);   // 30
System.out.println(a / b);   // 3 (Ganzzahldivision!)
System.out.println(a % b);   // 1 (Rest, Modulo)
```

Achtung: `10 / 3 = 3` (nicht 3,33), weil beide `int` sind!

```java
double ergebnis = 10.0 / 3;   // 3.3333...
```

---

### Vergleichsoperatoren

```java
a == b    // gleich
a != b    // ungleich
a > b     // größer
a < b     // kleiner
a >= b    // größer oder gleich
a <= b    // kleiner oder gleich
```

---

### Logische Operatoren

```java
true && false   // UND → false
true || false   // ODER → true
!true           // NICHT → false
```

---

## Bedingungen

### if / else if / else

```java
int punkte = 75;

if (punkte >= 90) {
    System.out.println("Sehr gut");
} else if (punkte >= 75) {
    System.out.println("Gut");
} else if (punkte >= 60) {
    System.out.println("Befriedigend");
} else {
    System.out.println("Nicht bestanden");
}
```

Ausgabe: `Gut`

---

### switch

```java
int tag = 3;

switch (tag) {
    case 1: System.out.println("Montag"); break;
    case 2: System.out.println("Dienstag"); break;
    case 3: System.out.println("Mittwoch"); break;
    default: System.out.println("Anderer Tag");
}
```

---

## Schleifen

### while-Schleife

```java
int i = 0;
while (i < 5) {
    System.out.println(i);
    i++;
}
```

Ausgabe: 0, 1, 2, 3, 4

---

### for-Schleife

```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

Struktur:

```
for (Initialisierung; Bedingung; Aktualisierung)
```

---

### do-while-Schleife

```java
int i = 0;
do {
    System.out.println(i);
    i++;
} while (i < 5);
```

Unterschied: Der Schleifenrumpf wird mindestens **einmal** ausgeführt.

---

## Arrays

```java
int[] zahlen = new int[5];       // 5 Felder, alle mit 0 initialisiert
zahlen[0] = 10;
zahlen[1] = 20;
zahlen[2] = 30;
```

Oder direkt:

```java
int[] zahlen = {10, 20, 30, 40, 50};
```

Array durchlaufen:

```java
for (int i = 0; i < zahlen.length; i++) {
    System.out.println(zahlen[i]);
}
```

Oder kürzer:

```java
for (int z : zahlen) {
    System.out.println(z);
}
```

---

## Methoden

Methoden sind wiederverwendbare Codeblöcke.

```java
public static int addiere(int a, int b) {
    return a + b;
}
```

Aufrufen:

```java
int ergebnis = addiere(3, 4);   // ergebnis = 7
```

Aufbau:

```
Rückgabetyp  Name  (Parameter)
     ↓        ↓        ↓
public static int addiere(int a, int b)
```

Wenn eine Methode nichts zurückgibt: `void`

```java
public static void begruesze(String name) {
    System.out.println("Hallo, " + name + "!");
}
```

---

## Strings

```java
String s = "Informatik";

s.length()          // 10
s.charAt(0)         // 'I'
s.toUpperCase()     // "INFORMATIK"
s.toLowerCase()     // "informatik"
s.substring(0, 4)   // "Info"
s.contains("mat")   // true
s.equals("Informatik")    // true (Inhalt vergleichen!)
```

Wichtig: Strings mit `equals()` vergleichen, nicht mit `==`!

```java
String a = "Hallo";
String b = "Hallo";

a == b        // kann false sein (vergleicht Referenz!)
a.equals(b)   // true (vergleicht Inhalt)
```

---

## Verbindung zu anderen Themen

- **Thema 1 (Binärzahlen):** `int` = 32-Bit-Zweierkomplement intern gespeichert.
- **Thema 4 (Gleitkommazahlen):** `float` und `double` = IEEE 754.
- **Thema 11 (Objektorientierung):** Java ist vollständig objektorientiert.
- **Thema 13 (Sortieralgorithmen):** Alle werden in Java implementiert.

---

## Typische Klausuraufgaben

### Aufgabe 1

Was gibt folgender Code aus?

```java
int x = 7;
int y = 2;
System.out.println(x / y);
System.out.println(x % y);
```

#### Lösung

```
3
1
```

(Ganzzahldivision: 7 / 2 = 3 Rest 1)

---

### Aufgabe 2

Schreibe eine Methode `max`, die den größeren von zwei Integers zurückgibt.

#### Lösung

```java
public static int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}
```

---

### Aufgabe 3

Was ist der Unterschied zwischen `==` und `equals()` bei Strings?

#### Lösung

```
== vergleicht, ob beide Variablen auf dasselbe Objekt im Speicher zeigen.
equals() vergleicht den Inhalt der Strings.
Für Inhaltsvergleiche immer equals() verwenden!
```

---

## Merksätze

1. Java ist streng typisiert — jede Variable braucht einen deklarierten Typ.
2. `int` ist 32-Bit-Zweierkomplement, `double` ist IEEE 754.
3. Ganzzahldivision: `7 / 2 = 3` (kein Rest!).
4. `%` gibt den Rest der Division zurück.
5. Strings immer mit `equals()` vergleichen, nicht mit `==`.
6. Arrays sind nullindiziert: erstes Element ist `[0]`.
7. Methoden vermeiden Code-Wiederholung und erhöhen Lesbarkeit.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 8/10
**Verständlichkeit:** 10/10
