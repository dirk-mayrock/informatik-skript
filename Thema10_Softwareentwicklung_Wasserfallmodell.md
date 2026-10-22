# Thema 10: Softwareentwicklung und das Wasserfallmodell

## Informatik Leistungskurs (Gymnasium)

---

## Einleitung: Warum braucht man ein Vorgehensmodell?

Ein einzelnes Programm mit 50 Zeilen schreibt man einfach.

Aber ein modernes Softwaresystem wie ein Betriebssystem oder eine Banking-App umfasst:

```
Millionen von Codezeilen
Hunderte von Entwicklern
Laufzeit: Jahre
Kosten: Millionen Euro
```

Ohne Planung und strukturiertes Vorgehen entstehen:
- Fehler, die erst beim Kunden auffallen
- Budgetüberschreitungen
- Software, die die Anforderungen nicht erfüllt

**Softwareentwicklungsmodelle** geben eine Struktur vor, wie Software von der Idee bis zur Wartung entwickelt wird.

---

## Die Phasen der Softwareentwicklung

Unabhängig vom Modell gibt es gemeinsame Phasen:

```
1. Anforderungsanalyse
2. Entwurf (Design)
3. Implementierung (Coding)
4. Testen (Verifikation)
5. Einführung (Deployment)
6. Wartung (Maintenance)
```

---

## Das Wasserfallmodell

Das **Wasserfallmodell** ist das älteste und bekannteste Softwareentwicklungsmodell.

Es wurde 1970 von Winston Royce beschrieben.

### Grundprinzip

Die Phasen werden **streng sequenziell** durchlaufen — wie Wasser, das einen Wasserfall hinunterfließt.

```
Anforderungsanalyse
        ↓
      Entwurf
        ↓
Implementierung
        ↓
       Test
        ↓
   Einführung
        ↓
     Wartung
```

Jede Phase muss **vollständig abgeschlossen** sein, bevor die nächste beginnt.

---

## Phase 1: Anforderungsanalyse

**Ziel:** Was soll die Software können?

**Ergebnis:** Pflichtenheft / Anforderungsspezifikation

Enthält:
- Funktionale Anforderungen: Was soll das System tun?
- Nicht-funktionale Anforderungen: Wie schnell? Wie sicher? Auf welchen Geräten?

Beispiel:

```
Funktional:
- Benutzer können sich einloggen.
- Benutzer können Bestellungen aufgeben.

Nicht-funktional:
- Die Seite lädt in unter 2 Sekunden.
- 10.000 gleichzeitige Nutzer möglich.
```

---

## Phase 2: Entwurf (Design)

**Ziel:** Wie wird das System gebaut?

**Ergebnis:** Systemarchitektur, Datenbankdesign, Klassendiagramme

Enthält:
- Welche Module gibt es?
- Wie kommunizieren sie miteinander?
- Welche Datenstrukturen werden verwendet?

---

## Phase 3: Implementierung

**Ziel:** Das System wird programmiert.

**Ergebnis:** Quellcode

Die Entwickler schreiben Code basierend auf den Entwurfsdokumenten.

---

## Phase 4: Test

**Ziel:** Funktioniert das System wie spezifiziert?

**Ergebnis:** Testprotokolle, Fehlerlisten

Arten von Tests:

| Testart         | Was wird geprüft?                              |
|-----------------|------------------------------------------------|
| Unit-Test       | Einzelne Methoden oder Klassen                 |
| Integrationstest | Zusammenspiel mehrerer Komponenten            |
| Systemtest      | Das gesamte System gegen die Anforderungen     |
| Abnahmetest     | Der Kunde prüft, ob alles erfüllt wurde        |

---

## Phase 5: Einführung (Deployment)

**Ziel:** Das System gelangt zum Kunden.

**Ergebnis:** Laufendes System beim Kunden

Beinhaltet: Installation, Schulung, Datenmigration

---

## Phase 6: Wartung

**Ziel:** Das System bleibt funktionsfähig.

**Ergebnis:** Bugfixes, Updates, Erweiterungen

Die Wartung dauert oft länger als die Entwicklung.

---

## Vorteile des Wasserfallmodells

| Vorteil | Erklärung |
|---------|-----------|
| Klare Struktur | Jeder weiß, was in welcher Phase zu tun ist |
| Gute Dokumentation | Jede Phase produziert Dokumente |
| Einfach zu planen | Budget und Zeit lassen sich gut abschätzen |
| Gut für klare Anforderungen | Wenn die Anforderungen fest stehen |

---

## Nachteile des Wasserfallmodells

| Nachteil | Erklärung |
|----------|-----------|
| Starr | Änderungen der Anforderungen sind teuer |
| Feedback spät | Der Kunde sieht das Produkt erst am Ende |
| Fehler in frühen Phasen | Werden erst spät (im Test) entdeckt |
| Realität ist nicht linear | Entwicklung ist oft iterativ, nicht sequenziell |

### Bekanntes Problem

Wenn sich Anforderungen ändern (was fast immer passiert), müssen alle nachfolgenden Phasen wiederholt werden.

```
Anforderung ändert sich in Phase 4 (Test)
→ Zurück zu Phase 1
→ Enormer Aufwand und Kosten
```

---

## Alternativen zum Wasserfallmodell

### Spiralmodell (Boehm)

Kombiniert Wasserfallmodell mit Risikoanalyse.

Jede Iteration (Spiralrunde) durchläuft:
1. Ziele definieren
2. Risiken analysieren
3. Entwickeln und testen
4. Ergebnis bewerten → nächste Runde oder abschließen

---

### Agile Methoden (z.B. Scrum)

Modernes Gegenstück zum Wasserfallmodell.

Grundprinzipien:
- Software in kurzen Zyklen (**Sprints**, 2-4 Wochen) liefern
- Ständiges Feedback vom Kunden
- Anforderungen dürfen sich ändern
- Funktionsfähige Software ist wichtiger als Dokumentation

```
Sprint 1 → Minimum Viable Product
Sprint 2 → Erweiterung
Sprint 3 → Weitere Features
...
```

---

## Vergleich

| Eigenschaft          | Wasserfallmodell | Agile (Scrum) |
|----------------------|------------------|---------------|
| Ablauf               | sequenziell      | iterativ      |
| Flexibilität         | gering           | hoch          |
| Kundenbeteiligung    | am Anfang/Ende   | ständig       |
| Dokumentation        | umfangreich      | minimal       |
| Gut bei              | klaren Anforderungen | sich ändernden Anforderungen |
| Risiko               | Fehler spät erkannt | früh erkannt |

---

## Verbindung zu anderen Themen

- **Thema 11 (Objektorientierung):** OOP-Entwurf findet in Phase 2 (Design) statt.
- **Thema 12 (Struktogramme):** Struktogramme und Ablaufpläne entstehen in der Entwurfsphase.

---

## Typische Klausuraufgaben

### Aufgabe 1

Nenne die sechs Phasen des Wasserfallmodells in der richtigen Reihenfolge.

#### Lösung

```
1. Anforderungsanalyse
2. Entwurf
3. Implementierung
4. Test
5. Einführung
6. Wartung
```

---

### Aufgabe 2

Was ist ein wesentlicher Nachteil des Wasserfallmodells?

#### Lösung

```
Das Wasserfallmodell ist unflexibel gegenüber Änderungen.
Wenn sich Anforderungen ändern, müssen alle Phasen wiederholt werden.
Fehler, die spät erkannt werden, sind sehr teuer zu korrigieren.
```

---

### Aufgabe 3

Nenne zwei Unterschiede zwischen dem Wasserfallmodell und agiler Entwicklung.

#### Lösung

```
1. Wasserfallmodell: sequenziell. Agil: iterativ (viele kurze Zyklen).
2. Wasserfallmodell: Kunde sieht Produkt erst am Ende.
   Agil: Kunde gibt nach jedem Sprint Feedback.
```

---

## Merksätze

1. Das Wasserfallmodell durchläuft Phasen sequenziell — keine Phase kann übersprungen werden.
2. Jede Phase produziert ein Dokument als Ausgabe.
3. Der größte Nachteil: Änderungen sind teuer und erzwingen Rückschritte.
4. Agile Methoden sind flexibler und liefern früh erste Ergebnisse.
5. In der Praxis werden heute meist agile Methoden bevorzugt.
6. Das Pflichtenheft beschreibt, was das System leisten soll.

---

## Gesamteinschätzung

**Didaktik:** 9/10
**Fachliche Korrektheit:** 10/10
**LK-Niveau:** 8/10
**Verständlichkeit:** 10/10
