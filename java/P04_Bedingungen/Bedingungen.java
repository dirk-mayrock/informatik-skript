import java.util.Scanner;

/**
 * Praktikum 4 – Bedingungen (if / else if / else)
 *
 * Neue Konzepte:
 *   - if / else if / else
 *   - Vergleichsoperatoren: ==, !=, >, <, >=, <=
 *   - Logische Operatoren: && (UND), || (ODER), ! (NICHT)
 *
 * Getränkeautomat – Schritt 4:
 * Wir prüfen, ob der eingeworfene Betrag für das gewählte Getränk reicht.
 */
public class Bedingungen {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // --- if / else kennenlernen ---
        int punkte = 75;

        if (punkte >= 90) {                                // NEU ←
            System.out.println("Note: sehr gut");
        } else if (punkte >= 75) {                         // NEU ←
            System.out.println("Note: gut");
        } else if (punkte >= 60) {
            System.out.println("Note: befriedigend");
        } else {                                           // NEU ←
            System.out.println("Note: nicht bestanden");
        }

        System.out.println();

        // --- Logische Operatoren ---
        boolean hatAusweis = true;
        int alter = 16;

        if (hatAusweis && alter >= 18) {                   // NEU ← (&&)
            System.out.println("Zugang erlaubt.");
        } else {
            System.out.println("Zugang verweigert.");
        }

        System.out.println();

        // --- Getränkeautomat Schritt 4 ---
        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        System.out.println("  1 - Cola          1.50 EUR");
        System.out.println("  2 - Apfelschorle  1.00 EUR");
        System.out.println("  3 - Wasser        1.00 EUR");
        System.out.println();

        System.out.print("Wieviel Geld hast du eingeworfen (z.B. 1.50)? ");
        double eingeworfenerBetrag = scanner.nextDouble();

        double preis = 1.50;  // Preis fuer Cola

        if (eingeworfenerBetrag >= preis) {                // NEU ←
            double rueckgeld = eingeworfenerBetrag - preis;
            System.out.println("Getraenk wird ausgegeben!");
            System.out.println("Rueckgeld: " + rueckgeld + " EUR");
        } else {                                           // NEU ←
            double fehlenderBetrag = preis - eingeworfenerBetrag;
            System.out.println("Nicht genug Geld!");
            System.out.println("Bitte noch " + fehlenderBetrag + " EUR einwerfen.");
        }

        scanner.close();
    }

}
