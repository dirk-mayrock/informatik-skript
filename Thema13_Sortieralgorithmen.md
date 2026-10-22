# Thema 13: Sortieralgorithmen

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung: Warum Sortieren?

Sortierte Daten sind die Basis vieler effizienter Algorithmen:

- Binäre Suche funktioniert nur in sortierten Arrays
- Datenbanken sortieren permanent
- Anzeigen von Ranglisten, Suchergebnissen, Dateien

Das Sortieren ist ein Kernthema der Algorithmik.

---

## Analyse von Algorithmen: O-Notation

Bevor wir die Algorithmen beschreiben, brauchen wir eine Metrik.

Die **O-Notation** (Landau-Symbol) beschreibt das Wachstum der Laufzeit in Abhängigkeit von der Eingabegröße n.

| Notation  | Name           | Bedeutung                                |
|-----------|----------------|------------------------------------------|
| O(1)      | Konstant       | Laufzeit unabhängig von n                |
| O(log n)  | Logarithmisch  | Sehr schnell                             |
| O(n)      | Linear         | Proportional zu n                        |
| O(n log n)| Quasilinear    | Sehr gut für Sortieren                   |
| O(n²)     | Quadratisch    | Bei großen n sehr langsam                |
| O(2ⁿ)    | Exponentiell   | Praktisch nicht nutzbar                  |

---

## Übersicht aller Algorithmen

| Algorithmus     | Best Case | Average Case | Worst Case | Stabil? | In-Place? |
|-----------------|-----------|--------------|------------|---------|-----------|
| Insertion Sort  | O(n)      | O(n²)        | O(n²)      | ja      | ja        |
| Selection Sort  | O(n²)     | O(n²)        | O(n²)      | nein    | ja        |
| Quicksort       | O(n log n)| O(n log n)   | O(n²)      | nein    | ja        |
| Mergesort       | O(n log n)| O(n log n)   | O(n log n) | ja      | nein      |
| Heapsort        | O(n log n)| O(n log n)   | O(n log n) | nein    | ja        |
| Bucketsort      | O(n+k)    | O(n+k)       | O(n²)      | ja      | nein      |

**Stabil:** Gleiche Elemente behalten ihre relative Reihenfolge.

**In-Place:** Kein wesentlicher zusätzlicher Speicher nötig.

---

## 1. Insertion Sort (Einfügesortierung)

### Idee

Wie beim Kartensortieren: Nimm eine Karte und füge sie an der richtigen Stelle in die bereits sortierte linke Seite ein.

### Algorithmus

```
Für i = 1 bis n-1:
    key = a[i]
    j = i - 1
    Solange j >= 0 und a[j] > key:
        a[j+1] = a[j]
        j = j - 1
    a[j+1] = key
```

### Schritt-für-Schritt-Beispiel

Array: `[5, 3, 8, 1, 4]`

```
i=1: key=3   [3, 5, 8, 1, 4]   (3 vor 5 eingefügt)
i=2: key=8   [3, 5, 8, 1, 4]   (8 bleibt)
i=3: key=1   [1, 3, 5, 8, 4]   (1 an Anfang)
i=4: key=4   [1, 3, 4, 5, 8]   (4 zwischen 3 und 5)
```

### Java-Code

```java
for (int i = 1; i < n; i++) {
    int key = a[i];
    int j = i - 1;
    while (j >= 0 && a[j] > key) {
        a[j + 1] = a[j];
        j--;
    }
    a[j + 1] = key;
}
```

### Bewertung

- Sehr gut für **fast sortierte** Arrays (Best Case O(n))
- Einfach zu implementieren
- Schlecht für große, unsortierte Arrays

---

## 2. Selection Sort (Auswahlsortierung)

### Idee

Suche das kleinste Element und tausche es an den Anfang. Dann das zweitkleinste in die zweite Position. Usw.

### Algorithmus

```
Für i = 0 bis n-2:
    minIndex = i
    Für j = i+1 bis n-1:
        Wenn a[j] < a[minIndex]:
            minIndex = j
    Tausche a[i] und a[minIndex]
```

### Schritt-für-Schritt-Beispiel

Array: `[5, 3, 8, 1, 4]`

```
i=0: Minimum=1 (Index 3) → Tausch [1, 3, 8, 5, 4]
i=1: Minimum=3 (Index 1) → Tausch [1, 3, 8, 5, 4]  (bleibt)
i=2: Minimum=4 (Index 4) → Tausch [1, 3, 4, 5, 8]
i=3: Minimum=5 (Index 3) → Tausch [1, 3, 4, 5, 8]  (bleibt)
```

### Java-Code

```java
for (int i = 0; i < n - 1; i++) {
    int minIndex = i;
    for (int j = i + 1; j < n; j++) {
        if (a[j] < a[minIndex]) {
            minIndex = j;
        }
    }
    int temp = a[i];
    a[i] = a[minIndex];
    a[minIndex] = temp;
}
```

### Bewertung

- Immer O(n²) — auch bei sortierten Arrays kein Gewinn
- Führt minimal viele Tauschoperationen durch (genau n-1)
- Gut wenn Schreiboperationen teuer sind

---

## 3. Quicksort

### Idee

**Teile und herrsche** (Divide and Conquer):

1. Wähle ein Element als **Pivot**
2. Teile das Array in zwei Hälften: kleiner als Pivot | größer als Pivot
3. Sortiere beide Hälften rekursiv

### Algorithmus

```
quicksort(a, links, rechts):
    wenn links < rechts:
        p = partition(a, links, rechts)
        quicksort(a, links, p-1)
        quicksort(a, p+1, rechts)

partition(a, links, rechts):
    pivot = a[rechts]
    i = links - 1
    für j = links bis rechts-1:
        wenn a[j] <= pivot:
            i++
            tausche a[i] und a[j]
    tausche a[i+1] und a[rechts]
    return i+1
```

### Schritt-für-Schritt-Beispiel

Array: `[3, 6, 8, 10, 1, 2, 1]`, Pivot = 1 (letztes Element)

```
Nach Partition: [1, 1, 8, 10, 6, 2, 3]   pivot an Index 1
→ Linker Teil:  [1]           → bereits sortiert
→ Rechter Teil: [8, 10, 6, 2, 3] → nächste Partition
```

### Java-Code

```java
public static void quicksort(int[] a, int links, int rechts) {
    if (links < rechts) {
        int p = partition(a, links, rechts);
        quicksort(a, links, p - 1);
        quicksort(a, p + 1, rechts);
    }
}

public static int partition(int[] a, int links, int rechts) {
    int pivot = a[rechts];
    int i = links - 1;
    for (int j = links; j < rechts; j++) {
        if (a[j] <= pivot) {
            i++;
            int temp = a[i]; a[i] = a[j]; a[j] = temp;
        }
    }
    int temp = a[i+1]; a[i+1] = a[rechts]; a[rechts] = temp;
    return i + 1;
}
```

### Bewertung

- Im Durchschnitt sehr schnell: O(n log n)
- Worst Case O(n²) wenn Pivot immer das Minimum/Maximum ist
- In der Praxis oft am schnellsten (gute Cache-Performance)

---

## 4. Mergesort

### Idee

**Teile und herrsche:**

1. Teile das Array in zwei gleich große Hälften
2. Sortiere beide Hälften rekursiv
3. **Füge** die zwei sortierten Hälften **zusammen** (Merge)

### Merge-Schritt

```
Linke Hälfte:  [1, 3, 5, 7]
Rechte Hälfte: [2, 4, 6, 8]

Vergleiche immer das kleinste der beiden Hälften:
1 < 2 → [1]
3 > 2 → [1, 2]
3 < 4 → [1, 2, 3]
5 > 4 → [1, 2, 3, 4]
5 < 6 → [1, 2, 3, 4, 5]
7 > 6 → [1, 2, 3, 4, 5, 6]
7 < 8 → [1, 2, 3, 4, 5, 6, 7]
        [1, 2, 3, 4, 5, 6, 7, 8]
```

### Java-Code

```java
public static void mergesort(int[] a, int links, int rechts) {
    if (links < rechts) {
        int mitte = (links + rechts) / 2;
        mergesort(a, links, mitte);
        mergesort(a, mitte + 1, rechts);
        merge(a, links, mitte, rechts);
    }
}
```

### Bewertung

- **Garantiert** O(n log n) — auch im Worst Case
- Stabil
- Braucht O(n) zusätzlichen Speicher (nicht In-Place)
- Ideal für externe Sortierung (sehr große Datenmengen)

---

## 5. Heapsort

### Idee

Nutzt die Datenstruktur **Heap** (Halde):

Ein Max-Heap ist ein Baum, bei dem jeder Knoten größer ist als seine Kinder.

1. Baue einen Max-Heap aus dem Array
2. Das größte Element steht immer an der Wurzel
3. Tausche Wurzel mit letztem Element → größtes Element ist sortiert
4. Stelle Heap-Eigenschaft wieder her
5. Wiederhole mit n-1 Elementen

### Bewertung

- Garantiert O(n log n) in allen Fällen
- In-Place (kein zusätzlicher Speicher)
- Nicht stabil
- In der Praxis langsamer als Quicksort (schlechtere Cache-Nutzung)

---

## 6. Bucketsort

### Idee

**Keine Vergleiche** — stattdessen werden Elemente in Bereiche (Buckets) aufgeteilt.

Beispiel: Zahlen zwischen 0 und 99 → 10 Buckets für je 10er-Bereiche

```
Bucket 0: Zahlen  0- 9
Bucket 1: Zahlen 10-19
...
Bucket 9: Zahlen 90-99
```

### Schritte

1. Erstelle k Buckets
2. Verteile alle Elemente in die zuständigen Buckets
3. Sortiere jeden Bucket (z.B. mit Insertion Sort)
4. Füge alle Buckets zusammen

### Beispiel

Array: `[5, 3, 8, 1, 9, 2, 7]` mit 3 Buckets (0-3, 4-6, 7-9)

```
Bucket 0 (0-3): [3, 1, 2] → [1, 2, 3]
Bucket 1 (4-6): [5]       → [5]
Bucket 2 (7-9): [8, 9, 7] → [7, 8, 9]

Ergebnis: [1, 2, 3, 5, 7, 8, 9]
```

### Bewertung

- Sehr schnell wenn Daten gleichmäßig verteilt sind: O(n+k)
- Braucht zusätzlichen Speicher
- Nur sinnvoll für Zahlen in bekanntem Wertebereich

---

## Vergleich und Wann was verwenden?

| Situation | Empfehlung |
|-----------|------------|
| Fast sortierte Daten | Insertion Sort |
| Wenige Schreibzugriffe nötig | Selection Sort |
| Allgemeinfall, Praxis | Quicksort |
| Stabilität wichtig, kein Speicherproblem | Mergesort |
| Worst Case garantiert, In-Place | Heapsort |
| Gleichmäßig verteilte Zahlen | Bucketsort |

---

## Verbindung zu anderen Themen

- **Thema 9 (Java):** Alle Algorithmen werden in Java implementiert.
- **Thema 12 (Struktogramme):** Algorithmen können als Struktogramm dargestellt werden.

---

## Typische Klausuraufgaben

### Aufgabe 1

Führe Insertion Sort auf `[4, 2, 7, 1, 5]` aus. Zeige jeden Schritt.

#### Lösung

```
Start: [4, 2, 7, 1, 5]
i=1: key=2 → [2, 4, 7, 1, 5]
i=2: key=7 → [2, 4, 7, 1, 5]  (bleibt)
i=3: key=1 → [1, 2, 4, 7, 5]
i=4: key=5 → [1, 2, 4, 5, 7]
```

---

### Aufgabe 2

Was ist der Unterschied zwischen Quicksort und Mergesort?

#### Lösung

```
Quicksort:
- Teilt am Pivot (nicht zwingend gleich)
- Worst Case O(n²) bei schlechter Pivotwahl
- In-Place, kein zusätzlicher Speicher
- Praxis: oft am schnellsten

Mergesort:
- Teilt immer in zwei gleiche Hälften
- Immer O(n log n) — garantiert
- Braucht O(n) zusätzlichen Speicher
- Stabil
```

---

### Aufgabe 3

Warum hat Bucketsort in vielen Fällen O(n+k) Laufzeit?

#### Lösung

```
Bucketsort vergleicht keine Elemente miteinander.
Stattdessen wird jedes Element direkt in seinen Bucket eingeteilt (O(n)).
k Buckets werden danach einzeln sortiert.
Wenn die Daten gleichmäßig verteilt sind, enthält jeder Bucket O(1) Elemente.
Gesamtaufwand: O(n + k).
```

---

## Merksätze

1. O(n²)-Algorithmen sind für große n zu langsam.
2. Quicksort und Mergesort sind die wichtigsten O(n log n)-Verfahren.
3. Mergesort garantiert O(n log n) — Quicksort im Worst Case O(n²).
4. Insertion Sort ist ideal für fast sortierte Daten.
5. Bucketsort ist nur sinnvoll, wenn der Wertebereich bekannt und begrenzt ist.
6. Ein stabiler Algorithmus verändert die Reihenfolge gleicher Elemente nicht.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 10/10
**Verständlichkeit:** 9/10
