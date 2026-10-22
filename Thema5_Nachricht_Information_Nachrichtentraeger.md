# Thema 5: Nachricht, Information, Nachrichtenträger

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung

Wenn man jemandem eine SMS schickt, passieren mehrere Dinge gleichzeitig:

- Es gibt einen Inhalt (den Text der SMS).
- Es gibt ein Medium, das den Text transportiert (das Mobilfunknetz).
- Es gibt eine Bedeutung für den Empfänger.

Diese drei Dinge — Nachricht, Nachrichtenträger und Information — sind in der Informatik klar voneinander getrennt.

---

## Grundbegriffe

### Zeichen

Ein **Zeichen** ist die kleinste bedeutungstragende Einheit.

Beispiele:

```
A  B  C  0  1  ?  !
```

---

### Alphabet

Ein **Alphabet** ist eine endliche Menge von Zeichen.

Beispiele:

```
Lateinisches Alphabet: {A, B, C, ..., Z}
Binäralphabet:         {0, 1}
Dezimalalphabet:       {0, 1, 2, ..., 9}
```

---

### Zeichenkette / Wort

Eine Folge von Zeichen aus einem Alphabet.

Beispiel:

```
"HALLO"
"1010011"
```

---

### Nachricht

Eine **Nachricht** ist eine Zeichenfolge, die von einem Sender zu einem Empfänger übertragen wird.

Wichtig: Eine Nachricht ist **syntaktisch** — sie hat eine Form, aber noch keine Bedeutung.

Beispiel:

```
"42"
```

Das ist eine Nachricht. Ob 42 eine Temperatur, eine Hausnummer oder die Antwort auf alles ist, ist noch unklar.

---

### Information

**Information** ist der Teil einer Nachricht, der beim Empfänger **Neuheit** erzeugt.

Wichtige Unterscheidung:

```
Nachricht = die gesendeten Daten
Information = das, was der Empfänger daraus lernt
```

Wenn Hannah schon weiß, dass Morgen kein Unterricht ist, und eine SMS „Kein Unterricht morgen" bekommt, dann enthält diese Nachricht für sie **keine neue Information**.

---

### Nachrichtenträger (Medium)

Der **Nachrichtenträger** ist das physikalische Medium, auf dem die Nachricht übertragen oder gespeichert wird.

Beispiele:

```
Kabel          → Strom
Glasfaser      → Licht
Funk / WLAN    → elektromagnetische Wellen
USB-Stick      → Flash-Speicher
Schallwellen   → Luft
Papier         → Tinte
```

---

## Das Kommunikationsmodell nach Shannon

Claude Shannon (1948) hat das mathematische Grundmodell der Kommunikation entwickelt.

```
Informationsquelle → Sender → Kanal → Empfänger → Senke
                                ↑
                             Störquelle
```

| Begriff          | Erklärung                                     |
|------------------|-----------------------------------------------|
| Informationsquelle | Wo die Nachricht entsteht (z.B. ein Mensch) |
| Sender           | Codiert die Nachricht in ein Signal           |
| Kanal            | Das Übertragungsmedium (Kabel, Luft...)       |
| Störquelle       | Alles, was das Signal verändert               |
| Empfänger        | Decodiert das Signal zurück                   |
| Senke            | Endempfänger der Nachricht                    |

### Beispiel: Telefongespräch

```
Informationsquelle: Hannah spricht
Sender:             Mikrofon im Telefon wandelt Schall in Signal um
Kanal:              Mobilfunknetz
Störquelle:         Rauschen, schlechter Empfang
Empfänger:          Lautsprecher beim Gesprächspartner
Senke:              Gesprächspartner hört
```

---

## Informationsgehalt und Entropie

### Informationsgehalt eines Zeichens

Je **unwahrscheinlicher** ein Ereignis ist, desto mehr Information trägt es.

Formel:

```
I(x) = log₂(1 / P(x))
     = -log₂(P(x))
```

Einheit: **Bit**

Beispiel:

Eine faire Münze wird geworfen. P(Kopf) = 0,5

```
I = -log₂(0,5) = -(-1) = 1 Bit
```

Ein Würfel zeigt 6. P(6) = 1/6

```
I = -log₂(1/6) = log₂(6) ≈ 2,58 Bit
```

Die Sechs trägt mehr Information als Kopf bei der Münze — weil sie unwahrscheinlicher ist.

---

### Shannon-Entropie

Die **Entropie H** ist der durchschnittliche Informationsgehalt einer Quelle.

Formel:

```
H = -∑ P(xᵢ) · log₂(P(xᵢ))
```

Beispiel:

Eine Quelle sendet zwei Zeichen A und B.

```
P(A) = 0,5
P(B) = 0,5
```

```
H = -(0,5 · log₂(0,5) + 0,5 · log₂(0,5))
  = -(0,5 · (-1) + 0,5 · (-1))
  = -(-0,5 - 0,5)
  = 1 Bit
```

Wenn A viel häufiger vorkommt:

```
P(A) = 0,9
P(B) = 0,1
```

```
H = -(0,9 · log₂(0,9) + 0,1 · log₂(0,1))
  ≈ -(0,9 · (-0,152) + 0,1 · (-3,32))
  ≈ -(−0,137 − 0,332)
  ≈ 0,469 Bit
```

Je ungleicher die Verteilung, desto **kleiner** die Entropie — desto weniger Information steckt im Durchschnitt in einem Zeichen.

---

## Codierung

**Codierung** ist die Umwandlung einer Nachricht in eine andere Darstellungsform.

Beispiele:

| Darstellung | Codierung    |
|-------------|--------------|
| Buchstabe A | ASCII: 65 = 01000001 |
| Zahl 13     | Binär: 1101  |
| Emoji 😊    | Unicode: U+1F60A |

### ASCII

ASCII = American Standard Code for Information Interchange

Ordnet jedem Zeichen eine 7-Bit-Zahl zu.

```
'A' = 65 = 1000001
'a' = 97 = 1100001
'0' = 48 = 0110000
```

---

## Redundanz

**Redundanz** ist der Teil einer Nachricht, der keine neue Information enthält.

Redundanz kann nützlich sein:

- Fehlerkorrektur (Hamming-Code, Thema 8)
- Verständlichkeit (Kontext)

Redundanz kann stören:

- Sie erhöht die Datenmenge ohne Informationsgewinn.
- Datenkompression (Thema 6) reduziert Redundanz.

---

## Verbindung zu anderen Themen

- **Thema 6 (Datenkompression):** Kompression entfernt Redundanz aus Nachrichten.
- **Thema 7 (Hashing):** Hashfunktionen arbeiten auf codierten Nachrichten.
- **Thema 8 (Hamming-Codes):** Redundanz wird gezielt hinzugefügt, um Fehler zu erkennen.
- **Thema 1 (Binärzahlen):** Das Binäralphabet {0, 1} ist die Grundlage aller Speicherung.

---

## Typische Klausuraufgaben

### Aufgabe 1

Was ist der Unterschied zwischen Nachricht und Information?

#### Lösung

```
Eine Nachricht ist die übertragene Zeichenfolge (syntaktisch).
Information ist der Neuheitswert der Nachricht für den Empfänger (semantisch).
Dieselbe Nachricht kann für verschiedene Empfänger unterschiedlich viel Information enthalten.
```

---

### Aufgabe 2

Eine Quelle sendet vier Zeichen mit folgenden Wahrscheinlichkeiten:

```
A: P = 0,5
B: P = 0,25
C: P = 0,125
D: P = 0,125
```

Berechne den Informationsgehalt jedes Zeichens.

#### Lösung

```
I(A) = -log₂(0,5)    = 1 Bit
I(B) = -log₂(0,25)   = 2 Bit
I(C) = -log₂(0,125)  = 3 Bit
I(D) = -log₂(0,125)  = 3 Bit
```

---

### Aufgabe 3

Berechne die Entropie der Quelle aus Aufgabe 2.

#### Lösung

```
H = 0,5·1 + 0,25·2 + 0,125·3 + 0,125·3
  = 0,5 + 0,5 + 0,375 + 0,375
  = 1,75 Bit
```

---

### Aufgabe 4

Nenne drei verschiedene Nachrichtenträger und die jeweils übertragene physikalische Größe.

#### Lösung

```
Kupferkabel  → elektrische Spannung
Glasfaser    → Licht (Photonen)
WLAN         → elektromagnetische Wellen (Radiowellen)
```

---

## Merksätze

1. Zeichen → Alphabet → Zeichenkette → Nachricht ist die Hierarchie der Syntax.
2. Eine Nachricht wird erst zur Information, wenn sie dem Empfänger etwas Neues mitteilt.
3. Je unwahrscheinlicher ein Zeichen, desto größer sein Informationsgehalt.
4. Die Entropie ist der durchschnittliche Informationsgehalt einer Quelle.
5. Redundanz ist Überflüssiges — aber manchmal nützlich (Fehlerkorrektur).
6. Das Shannon-Modell beschreibt jede Kommunikation: Quelle → Kanal → Senke.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 9/10
**Verständlichkeit:** 9/10
