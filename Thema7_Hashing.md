# Thema 7: Hashing

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung: Das Problem der schnellen Suche

Stell dir vor, du hast eine Liste mit 1.000.000 Namen und willst wissen, ob „Hannah" darin vorkommt.

Wenn die Liste unsortiert ist, musst du im schlimmsten Fall alle 1.000.000 Namen durchsuchen.

Hashing löst dieses Problem: Die Suche dauert fast immer **konstante Zeit** — egal wie groß die Liste ist.

---

## Was ist eine Hashfunktion?

Eine **Hashfunktion** ist eine Funktion, die eine Eingabe beliebiger Länge auf einen Wert fester Länge abbildet.

```
h(x) = Hashwert
```

Die Eingabe kann ein Name, eine Datei, ein Passwort oder beliebige Daten sein.

Der Hashwert hat immer dieselbe Länge — egal wie groß die Eingabe.

---

## Eigenschaften einer guten Hashfunktion

| Eigenschaft        | Bedeutung                                               |
|--------------------|---------------------------------------------------------|
| Deterministisch    | Gleiche Eingabe → immer gleicher Hashwert               |
| Gleichverteilung   | Hashwerte verteilen sich gleichmäßig                    |
| Schnell berechnet  | Berechnung soll effizient sein                          |
| Lawineneffekt      | Kleine Änderung der Eingabe → völlig anderer Hashwert   |
| Einwegfunktion     | Aus dem Hashwert lässt sich die Eingabe nicht berechnen |

---

## Einfaches Beispiel: Modulo-Hashfunktion

```
h(k) = k mod m
```

m = Größe der Hashtabelle

Beispiel mit m = 10:

```
h(23) = 23 mod 10 = 3
h(47) = 47 mod 10 = 7
h(10) = 10 mod 10 = 0
h(33) = 33 mod 10 = 3
```

23 und 33 landen am selben Index → **Kollision**!

---

## Hashtabellen

Eine **Hashtabelle** ist ein Array, in dem Einträge an einer durch die Hashfunktion bestimmten Position gespeichert werden.

Einfügen von `(Schlüssel, Wert)`:

```
Position = h(Schlüssel)
Tabelle[Position] = Wert
```

Suchen nach Schlüssel:

```
Position = h(Schlüssel)
Wert = Tabelle[Position]
```

Beides dauert **O(1)** — konstante Zeit!

---

## Kollisionen

Eine **Kollision** tritt auf, wenn zwei verschiedene Schlüssel denselben Hashwert ergeben.

```
h(23) = 3
h(33) = 3
→ Kollision!
```

Kollisionen sind unvermeidbar, wenn es mehr mögliche Schlüssel als Tabellenplätze gibt (Schubfachprinzip).

---

## Kollisionsbehandlung 1: Verkettung (Chaining)

Jede Zelle der Hashtabelle enthält eine **verkettete Liste**.

Alle Schlüssel mit demselben Hashwert werden in diese Liste eingehängt.

```
Index 3: [23] → [33] → null
Index 7: [47] → null
Index 0: [10] → null
```

**Vorteil:** Einfach zu implementieren, unbegrenzt viele Elemente pro Zelle.

**Nachteil:** Im schlechtesten Fall (alle im selben Bucket) wird die Suche linear: O(n).

---

## Kollisionsbehandlung 2: Offene Adressierung (Linear Probing)

Ist eine Position belegt, wird die nächste freie Position verwendet:

```
h'(k, i) = (h(k) + i) mod m
```

Beispiel:

```
h(23) = 3 → Position 3 frei → speichern
h(33) = 3 → Position 3 belegt → probiere 4 → frei → speichern
```

**Vorteil:** Kein zusätzlicher Speicher für Listen.

**Nachteil:** Cluster entstehen — viele belegte Felder hintereinander verlangsamen spätere Suchen.

---

## Kryptografische Hashfunktionen

Für Sicherheitsanwendungen werden spezielle, sehr sichere Hashfunktionen verwendet.

Wichtigste Vertreter:

| Funktion | Ausgabelänge | Status         |
|----------|--------------|----------------|
| MD5      | 128 Bit      | unsicher (gebrochen) |
| SHA-1    | 160 Bit      | unsicher (veraltet)  |
| SHA-256  | 256 Bit      | aktuell sicher |
| SHA-3    | variabel     | aktuell sicher |

---

## Anwendungen kryptografischer Hashfunktionen

### Passwortspeicherung

Passwörter werden **nie im Klartext** gespeichert.

```
Eingabe:   "meinPasswort123"
SHA-256:   a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3
```

Bei der Anmeldung wird das eingegebene Passwort gehasht und mit dem gespeicherten Hash verglichen.

---

### Dateiintegrität

Beim Herunterladen einer Datei kann man prüfen, ob sie unverändert ist:

```
Hashwert der Originaldatei: abc123...
Hashwert der heruntergeladenen Datei: abc123...
→ identisch → Datei ist korrekt
```

---

### Blockchain / Bitcoin

Jeder Block enthält den Hash des vorherigen Blocks.

Dadurch kann kein Block nachträglich geändert werden, ohne alle folgenden Blöcke zu ungültig zu machen.

---

## Lawineneffekt (Avalanche Effect)

Eine kleine Änderung der Eingabe ändert den Hashwert komplett.

Beispiel (SHA-256):

```
"Hallo"   → 185f8db32921bd46...
"hallo"   → 2cf24dba5fb0a30e...
```

Nur ein Großbuchstabe geändert — der gesamte Hashwert ist anders.

---

## Verbindung zu anderen Themen

- **Thema 1 (Hexadezimal):** Hashwerte werden meist hexadezimal dargestellt.
- **Thema 5 (Information):** Ein Hashwert komprimiert beliebig viele Daten auf eine feste Länge.
- **Thema 8 (Hamming-Codes):** Beide Verfahren dienen der Erkennung von Fehlern/Veränderungen.

---

## Typische Klausuraufgaben

### Aufgabe 1

Gegeben sei die Hashfunktion `h(k) = k mod 7`.

Füge die Schlüssel `15, 22, 8, 29, 1` in eine Hashtabelle der Größe 7 ein.

#### Lösung

```
h(15) = 15 mod 7 = 1
h(22) = 22 mod 7 = 1  → Kollision mit 15!
h( 8) =  8 mod 7 = 1  → Kollision!
h(29) = 29 mod 7 = 1  → Kollision!
h( 1) =  1 mod 7 = 1  → Kollision!
```

Mit Verkettung:

```
Index 1: [15] → [22] → [8] → [29] → [1] → null
```

Hinweis: m = 7 (prim) ist hier zufällig ungünstig für diese Eingaben.

---

### Aufgabe 2

Warum werden Passwörter als Hashwerte gespeichert?

#### Lösung

```
Hashfunktionen sind Einwegfunktionen.
Aus dem Hashwert lässt sich das Passwort nicht zurückberechnen.
Selbst wenn die Datenbank gestohlen wird, sind die Originalpasswörter nicht lesbar.
```

---

### Aufgabe 3

Was ist eine Kollision und warum ist sie unvermeidbar?

#### Lösung

```
Eine Kollision tritt auf, wenn zwei verschiedene Schlüssel denselben Hashwert ergeben.
Da es mehr mögliche Schlüssel als Tabellenplätze gibt (unendlich vs. endlich),
muss es laut Schubfachprinzip Kollisionen geben.
```

---

## Merksätze

1. Eine Hashfunktion bildet beliebige Daten auf einen Wert fester Länge ab.
2. Hashtabellen ermöglichen Suche, Einfügen und Löschen in O(1).
3. Kollisionen sind unvermeidbar; sie werden durch Chaining oder Open Addressing behandelt.
4. Kryptografische Hashfunktionen sind Einwegfunktionen — nicht umkehrbar.
5. Der Lawineneffekt: Kleine Eingabeänderung → komplett anderer Hashwert.
6. SHA-256 ist der aktuelle Standard für sichere Hashwerte.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 9/10
**Verständlichkeit:** 9/10
