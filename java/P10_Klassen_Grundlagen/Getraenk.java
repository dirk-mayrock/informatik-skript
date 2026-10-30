/**
 * Praktikum 10 – Klassen Grundlagen
 *
 * Klasse: Getraenk
 *
 * Neue Konzepte:
 *   - Klasse mit Attributen definieren
 *   - Konstruktor: public Getraenk(...)
 *   - this-Schlüsselwort
 *   - Objekt mit new erzeugen
 *   - Auf Attribute zugreifen: objekt.attribut
 *   - Methode in einer Klasse
 *
 * Getränkeautomat – Schritt 10:
 * Die parallelen Arrays aus P6–P9 werden durch ein
 * Array von Getraenk-Objekten ersetzt.
 */
public class Getraenk {                                  // NEU ←

    // --- Attribute ---                                 NEU ←
    String name;
    double preis;
    int    bestand;

    // --- Konstruktor ---                               NEU ←
    public Getraenk(String name, double preis, int bestand) {
        this.name    = name;                             // NEU ← (this)
        this.preis   = preis;
        this.bestand = bestand;
    }

    // --- Methode ---
    public void zeigeInfo() {
        System.out.printf("  %-15s %.2f EUR  (%d Dosen)%n",
            name, preis, bestand);
    }

    public boolean istVerfuegbar() {
        return bestand > 0;
    }

}
