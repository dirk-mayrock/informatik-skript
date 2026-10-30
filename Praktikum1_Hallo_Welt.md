# Praktikum 1: Hallo Welt

## Informatik Leistungskurs – Praktikum

---

:::progress-box
**Bisher können wir:** Theorie über Java lesen (Thema 9)
**Heute lernen wir:** Ein Java-Programm schreiben und starten
**Danach können wir:** Text auf der Konsole ausgeben
:::

---

## Neue Syntax

### Programmstruktur

Jedes Java-Programm besteht aus mindestens einer **Klasse** mit einer **main-Methode**:

```java
public class HalloWelt {
    public static void main(String[] args) {
        // Hier steht der Code
    }
}
```

| Teil | Bedeutung |
|------|-----------|
| `public class HalloWelt` | Klasse mit dem Namen `HalloWelt` |
| `public static void main(String[] args)` | Startpunkt – hier beginnt das Programm |
| `{ }` | Geschweifte Klammern umschließen einen Block |
| `// ...` | Kommentar – wird vom Computer ignoriert |

### Ausgabe auf der Konsole

```java
System.out.println("Hallo, Welt!");   // mit Zeilenumbruch
System.out.print("Hallo ");           // ohne Zeilenumbruch
System.out.println();                  // leere Zeile
```

`println` = **print** + **l**i**n**e → Ausgabe mit Zeilenumbruch danach.

### Wichtige Regeln

- Jede Anweisung endet mit einem **Semikolon** `;`
- Groß-/Kleinschreibung wird unterschieden: `System` ≠ `system`
- Dateiname = Klassenname: Klasse `HalloWelt` → Datei `HalloWelt.java`

---

## Im Getränkeautomaten anwenden

Unser Ziel am Ende aller Schritte ist ein vollständiger Getränkeautomat.
In diesem ersten Schritt geben wir einen **Willkommenstext** aus.

```java
public class HalloWelt {
    public static void main(String[] args) {
        System.out.println("============================");
        System.out.println(" Willkommen beim");
        System.out.println(" Getraenkeautomaten!");
        System.out.println("============================");
        System.out.println("Wir haben leckere Getraenke.");
    }
}
```

Konsolenausgabe:

```
============================
 Willkommen beim
 Getraenkeautomaten!
============================
Wir haben leckere Getraenke.
```

---

## BlueJ – So startest du das Programm

1. Ordner `java/P01_Hallo_Welt` in BlueJ öffnen (**Project → Open Project**)
2. Auf das Klassen-Symbol `HalloWelt` rechtsklicken
3. **Compile** wählen (oder den Kompilierknopf oben)
4. Rechtsklick → `void main(String[] args)` → **OK**
5. Ausgabe erscheint im Terminal-Fenster unten

---

## Aufgabe

Ändere das Programm so, dass es zusätzlich deinen Namen ausgibt:

```
============================
 Willkommen beim
 Getraenkeautomaten!
 Bedient von: [dein Name]
============================
```

## Lösung

```java
System.out.println("============================");
System.out.println(" Willkommen beim");
System.out.println(" Getraenkeautomaten!");
System.out.println(" Bedient von: Hannah");
System.out.println("============================");
```

---

## Merksätze

1. Jedes Java-Programm braucht eine Klasse und eine `main`-Methode.
2. `System.out.println(...)` gibt Text aus und springt in die nächste Zeile.
3. Jede Anweisung endet mit `;`.
4. Kommentare (`//`) werden nicht ausgeführt – sie erklären den Code.
5. Dateiname und Klassenname müssen identisch sein.
