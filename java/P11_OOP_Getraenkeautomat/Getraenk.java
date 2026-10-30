/**
 * Praktikum 11 – OOP Getränkeautomat
 *
 * Klasse: Getraenk
 *
 * Kapselt alle Informationen eines Getränks.
 * Attribute sind private → Zugriff nur über Getter/Setter.
 */
public class Getraenk {

    // --- private Attribute ---                         NEU ← (Kapselung)
    private String name;
    private double preis;
    private int    bestand;
    private static final int MAX_BESTAND = 5;

    // --- Konstruktor ---
    public Getraenk(String name, double preis, int bestand) {
        this.name    = name;
        this.preis   = preis;
        this.bestand = Math.min(bestand, MAX_BESTAND);
    }

    // --- Getter ---                                    NEU ←
    public String getName()    { return name; }
    public double getPreis()   { return preis; }
    public int    getBestand() { return bestand; }

    // --- Methoden ---
    public boolean istVerfuegbar() {
        return bestand > 0;
    }

    /**
     * Gibt eine Dose aus (reduziert Bestand um 1).
     * @return true wenn Ausgabe erfolgreich
     */
    public boolean ausgeben() {                          // NEU ←
        if (bestand > 0) {
            bestand--;
            return true;
        }
        return false;
    }

    /**
     * Bestand auffüllen (bis MAX_BESTAND).
     */
    public void auffuellen() {
        bestand = MAX_BESTAND;
    }

    // --- toString ---                                  NEU ←
    @Override
    public String toString() {
        return String.format("%-15s %.2f EUR  (%d Dosen)", name, preis, bestand);
    }

}
