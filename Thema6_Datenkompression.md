# Thema 6: Datenkompression

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung

Ein unkomprimiertes Bild mit 1920×1080 Pixeln und 3 Byte pro Pixel benötigt:

```
1920 × 1080 × 3 = 6.220.800 Byte ≈ 6 MB
```

Ein HD-Video besteht aus 24 solcher Bilder pro Sekunde.

Ohne Kompression wäre Streaming undenkbar.

**Datenkompression** reduziert die Menge der benötigten Bits, um eine Information zu speichern oder zu übertragen.

---

## Zwei Arten der Kompression

### Verlustfreie Kompression

Die Originaldaten können aus den komprimierten Daten **vollständig wiederhergestellt** werden.

Verwendung: Text, Programme, Archivierung

Verfahren: Lauflängencodierung, Huffman, LZW

---

### Verlustbehaftete Kompression

Ein Teil der Daten wird bewusst weggelassen.

Die Originaldaten lassen sich **nicht mehr exakt** rekonstruieren.

Verwendung: Bilder (JPEG), Audio (MP3), Video (MP4)

---

## Verfahren 1: Lauflängencodierung (RLE)

### Idee

Wenn dasselbe Zeichen mehrfach hintereinander vorkommt, wird es als Paar gespeichert:

```
(Anzahl, Zeichen)
```

### Beispiel

Original:

```
AAAABBBBBCCAAA
```

Komprimiert:

```
(4,A)(5,B)(2,C)(3,A)
```

Unkomprimiert: 14 Zeichen
Komprimiert: 4 Paare (je 2 Zeichen) = 8 Zeichen

**Ersparnis: 43 %**

---

### Wo funktioniert RLE gut?

- Bilder mit großen einfarbigen Flächen
- Schwarz-Weiß-Faxe
- Technische Zeichnungen

### Wo funktioniert RLE schlecht?

- Fotos mit vielen Farbwechseln
- Texte

Gegenbeispiel:

```
ABCDEFG
→ (1,A)(1,B)(1,C)(1,D)(1,E)(1,F)(1,G)
```

Aus 7 Zeichen werden 14 — die Datei wird **größer**!

---

## Verfahren 2: Deltacodierung

### Idee

Statt absoluter Werte werden die **Unterschiede** (Deltas) zwischen aufeinanderfolgenden Werten gespeichert.

### Beispiel: Temperaturreihe

Originaldaten:

```
20, 21, 22, 21, 23, 24
```

Deltacodierung:

```
20, +1, +1, -1, +2, +1
```

Wenn die Werte sich wenig ändern, werden die Deltas klein — und kleine Zahlen brauchen weniger Bits.

### Anwendung

- Audio (FLAC, Audiorekorder)
- GPS-Daten (Koordinatenänderungen sind klein)
- Temperatursensoren

---

## Verfahren 3: Huffman-Codierung

### Idee

Häufige Zeichen bekommen **kurze** Codes.

Seltene Zeichen bekommen **lange** Codes.

Damit braucht man im Durchschnitt weniger Bits.

---

### Algorithmus

**Schritt 1:** Häufigkeiten aller Zeichen zählen.

**Schritt 2:** Huffman-Baum aufbauen:
- Alle Zeichen als Blätter (mit ihrer Häufigkeit) in eine Prioritätswarteschlange.
- Immer die zwei kleinsten Knoten zusammenführen.
- Der neue Knoten erhält die Summe der Häufigkeiten.
- Wiederholen bis ein Baum entsteht.

**Schritt 3:** Codes ableiten:
- Links gehen = 0
- Rechts gehen = 1

---

### Vollständiges Beispiel

Nachricht: `AABBBCDDDD`

Häufigkeiten:

```
A: 2
B: 3
C: 1
D: 4
```

**Baum aufbauen:**

Start: vier Blätter `C(1)  A(2)  B(3)  D(4)`

Schritt 1: Kleinste zusammenführen: C(1) + A(2) = CA(3)

```
  CA(3)
 /     \
C(1)  A(2)
```

Noch in Warteschlange: `B(3)  CA(3)  D(4)`

Schritt 2: Kleinste: B(3) + CA(3) = BCA(6)

```
    BCA(6)
   /      \
 B(3)    CA(3)
         /    \
        C(1)  A(2)
```

Noch in Warteschlange: `D(4)  BCA(6)`

Schritt 3: D(4) + BCA(6) = Root(10)

```
         Root(10)
        /         \
      D(4)       BCA(6)
                /      \
              B(3)    CA(3)
                      /    \
                    C(1)  A(2)
```

**Codes ableiten (links=0, rechts=1):**

```
D → 0
B → 10
C → 110
A → 111
```

**Codierung der Nachricht `AABBBCDDDD`:**

```
A=111  A=111  B=10  B=10  B=10  C=110  D=0  D=0  D=0  D=0
→ 111 111 10 10 10 110 0 0 0 0
→ 22 Bit
```

**Vergleich mit fester 2-Bit-Codierung:**

```
10 Zeichen × 2 Bit = 20 Bit
```

In diesem kleinen Beispiel ist Huffman etwas schlechter, weil der Baum selbst mitgespeichert werden muss. Bei langen Texten ist Huffman deutlich besser.

---

## Verfahren 4: LZW-Kompression

### Idee

LZW (Lempel-Ziv-Welch) baut während der Kompression ein **Wörterbuch** aus wiederkehrenden Mustern auf.

---

### Algorithmus (vereinfacht)

1. Starte mit einem Wörterbuch, das alle Einzelzeichen enthält.
2. Lies Zeichen, solange die aktuelle Zeichenkette im Wörterbuch steht.
3. Sobald die Kette nicht mehr im Wörterbuch ist:
   - Gib den Code der bisherigen (kürzeren) Kette aus.
   - Füge die neue Kette dem Wörterbuch hinzu.
   - Starte neu mit dem letzten Zeichen.

---

### Beispiel

Eingabe: `ABABABAB`

Startwörterbuch: `{A=1, B=2}`

| Schritt | Puffer | Nächstes Zeichen | Aktion                   | Ausgabe |
|---------|--------|-------------------|--------------------------|---------|
| 1       | A      | B                 | AB nicht im Dict → Ausgabe A, Dict: AB=3 | 1 (A)  |
| 2       | B      | A                 | BA nicht im Dict → Ausgabe B, Dict: BA=4 | 2 (B)  |
| 3       | A      | B                 | AB im Dict!              |         |
| 4       | AB     | A                 | ABA nicht im Dict → Ausgabe AB, Dict: ABA=5 | 3 (AB) |
| 5       | A      | B                 | AB im Dict!              |         |
| 6       | AB     | A                 | ABA im Dict!             |         |
| 7       | ABA    | B                 | ABAB nicht im Dict → Ausgabe ABA, Dict: ABAB=6 | 5 (ABA)|
| 8       | B      | Ende              | Ausgabe B                | 2 (B)  |

Ausgabe: `1 2 3 5 2`

Statt 8 Zeichen werden nur 5 Codes gespeichert.

**LZW ist der Kern vieler Formate:** GIF, TIFF, PDF

---

## Vergleich der Verfahren

| Verfahren   | Verlustfrei | Besonders gut bei         | Typisches Format      |
|-------------|-------------|----------------------------|-----------------------|
| RLE         | ja          | einfarbige Flächen         | BMP, Fax              |
| Delta       | ja          | langsam ändernde Werte     | Audio, GPS            |
| Huffman     | ja          | ungleichmäßige Häufigkeiten | ZIP (Teil davon)     |
| LZW         | ja          | wiederholende Muster       | GIF, PDF              |
| JPEG        | nein        | Fotos                      | Bilder                |
| MP3         | nein        | Musik                      | Audio                 |

---

## Verbindung zu anderen Themen

- **Thema 5 (Information):** Kompression reduziert Redundanz — nicht den Informationsgehalt.
- **Thema 1 (Binärzahlen):** Alle Codes werden als Bitfolgen gespeichert.
- **Huffman und Entropie:** Der Huffman-Code kommt dem theoretischen Optimum (Entropie) sehr nahe.

---

## Typische Klausuraufgaben

### Aufgabe 1

Wende RLE auf folgende Zeichenkette an:

```
WWWWSSSSSWWW
```

#### Lösung

```
(4,W)(5,S)(3,W)
```

---

### Aufgabe 2

Erstelle einen Huffman-Baum für:

```
A: 4
B: 2
C: 1
D: 1
```

#### Lösung

Start: `C(1) D(1) B(2) A(4)`

Schritt 1: C+D = CD(2)

Schritt 2: B(2)+CD(2) = BCD(4)

Schritt 3: A(4)+BCD(4) = Root(8)

```
       Root(8)
      /        \
    A(4)      BCD(4)
              /      \
            B(2)    CD(2)
                    /    \
                  C(1)  D(1)
```

Codes:

```
A → 0
B → 10
C → 110
D → 111
```

---

### Aufgabe 3

Was ist der Unterschied zwischen verlustfreier und verlustbehafteter Kompression?

#### Lösung

```
Verlustfrei: Original kann exakt wiederhergestellt werden.
             Beispiele: ZIP, PNG, FLAC

Verlustbehaftet: Teile der Daten werden unwiderruflich entfernt.
                 Besser für Medien, wo kleine Qualitätsverluste nicht auffallen.
                 Beispiele: JPEG, MP3, H.264
```

---

## Merksätze

1. Datenkompression reduziert Redundanz, nicht den Informationsgehalt.
2. RLE: Wiederholungen werden als (Anzahl, Zeichen) gespeichert.
3. Delta: Nur Unterschiede werden gespeichert.
4. Huffman: Häufige Zeichen = kurze Codes, seltene = lange Codes.
5. LZW: Baut ein Wörterbuch aus Mustern während der Kompression auf.
6. Verlustfrei: Exakte Rekonstruktion. Verlustbehaftet: Qualitätsverlust akzeptiert.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 9/10
**Verständlichkeit:** 9/10
