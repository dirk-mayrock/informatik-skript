/**
 * Praktikum 2 – Variablen und Datentypen
 *
 * Neue Konzepte:
 *   - Variablen deklarieren und initialisieren
 *   - Datentypen: int, double, String, boolean
 *   - Variablen in Ausgaben einbauen (String-Verkettung mit +)
 *
 * Getränkeautomat – Schritt 2:
 * Wir speichern Namen und Preis eines Getränks in Variablen.
 */
public class Variablen {

    public static void main(String[] args) {

        // --- Datentypen kennenlernen ---

        int alter = 17;                    // Ganzzahl
        double temperatur = 36.8;          // Kommazahl
        String name = "Hannah";            // Text
        boolean istAngemeldet = true;      // Wahrheitswert

        System.out.println("Name:          " + name);
        System.out.println("Alter:         " + alter);
        System.out.println("Temperatur:    " + temperatur);
        System.out.println("Angemeldet:    " + istAngemeldet);

        System.out.println();

        // Wert einer Variablen ändern
        alter = 18;
        System.out.println("Neues Alter:   " + alter);

        // Rechnen mit Variablen
        int a = 10;
        int b = 3;
        System.out.println("10 + 3 = " + (a + b));
        System.out.println("10 / 3 = " + (a / b));       // Ganzzahldivision!
        System.out.println("10 % 3 = " + (a % b));       // Rest

        System.out.println();

        // --- Getränkeautomat Schritt 2 ---
        System.out.println("============================");
        System.out.println(" Willkommen beim");
        System.out.println(" Getraenkeautomaten!");
        System.out.println("============================");

        String getraenk1Name  = "Cola";
        double getraenk1Preis = 1.50;

        String getraenk2Name  = "Apfelschorle";
        double getraenk2Preis = 1.00;

        String getraenk3Name  = "Wasser";
        double getraenk3Preis = 1.00;                    // NEU ←

        System.out.println("Unser Angebot:");
        System.out.println("  " + getraenk1Name + "  " + getraenk1Preis + " EUR");
        System.out.println("  " + getraenk2Name + "  " + getraenk2Preis + " EUR");
        System.out.println("  " + getraenk3Name + "  " + getraenk3Preis + " EUR");

    }

}
