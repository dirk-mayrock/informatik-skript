/**
 * Praktikum 11 – OOP Getränkeautomat
 *
 * Klasse: Geldfach
 *
 * Verwaltet den aktuell eingeworfenen Geldbetrag
 * und berechnet die Münz-Stückelung für Wechselgeld.
 */
public class Geldfach {

    private double betrag;
    private static final double[] MUENZEN = {2.00, 1.00, 0.50, 0.20, 0.10};

    // --- Konstruktor ---
    public Geldfach() {
        this.betrag = 0.0;
    }

    // --- Getter ---
    public double getBetrag() { return betrag; }

    // --- Münze einwerfen ---
    public boolean einwerfen(double muenze) {
        // Nur gültige Münzen annehmen
        for (double m : MUENZEN) {
            if (Math.abs(muenze - m) < 0.001) {
                betrag += muenze;
                betrag = Math.round(betrag * 100) / 100.0;
                return true;
            }
        }
        return false;  // ungültige Münze
    }

    // --- Betrag abziehen (nach Kauf) ---
    public void abziehen(double preis) {
        betrag -= preis;
        betrag = Math.round(betrag * 100) / 100.0;
        if (betrag < 0) betrag = 0;
    }

    // --- Alles zurückgeben ---
    public double zurueckgeben() {
        double r = betrag;
        betrag   = 0.0;
        return r;
    }

    // --- Stückelung des Wechselgelds berechnen ---
    public String wechselgeldAlsText() {
        if (betrag <= 0) return "kein Wechselgeld";

        StringBuilder sb = new StringBuilder();
        int cents = (int) Math.round(betrag * 100);

        for (double muenze : MUENZEN) {
            int muenzCents = (int) Math.round(muenze * 100);
            int anzahl     = cents / muenzCents;
            if (anzahl > 0) {
                sb.append(anzahl).append(" × ")
                  .append(String.format("%.2f", muenze))
                  .append(" EUR  ");
                cents -= anzahl * muenzCents;
            }
        }
        return sb.toString().trim();
    }

    @Override
    public String toString() {
        return String.format("%.2f EUR", betrag);
    }

}
