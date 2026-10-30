import java.util.Scanner;

/**
 * Praktikum 7 – while und do-while
 *
 * Neue Konzepte:
 *   - while-Schleife: läuft solange Bedingung wahr
 *   - do-while-Schleife: läuft mindestens einmal
 *   - break: Schleife sofort verlassen
 *   - Schleifen-Akkumulator (Summe aufaddieren)
 *
 * Getränkeautomat – Schritt 7:
 * Der Nutzer kann mehrere Münzen einwerfen.
 * Nach jeder Münze wird gefragt: "Mehr Geld? (j/n)"
 * Wenn nein → Betrag steht fest, weiter zur Auswahl.
 * Bei 'a' → Abbruch, gesamtes Geld zurück.
 */
public class GeldEinwerfen {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // --- while kennenlernen ---
        System.out.println("Countdown:");
        int i = 5;
        while (i > 0) {                                  // NEU ←
            System.out.println("  " + i);
            i--;
        }
        System.out.println("  Los!");

        System.out.println();

        // --- do-while: mindestens einmal ---
        int zahl;
        do {                                             // NEU ←
            System.out.print("Gib eine Zahl zwischen 1 und 10 ein: ");
            zahl = scanner.nextInt();
            scanner.nextLine();
        } while (zahl < 1 || zahl > 10);                // NEU ←
        System.out.println("Danke! Du hast " + zahl + " eingegeben.");

        System.out.println();

        // --- Getränkeautomat Schritt 7 ---
        String[] namen  = {"Cola", "Apfelschorle", "Wasser", "Eistee", "Limo"};
        double[] preise = {1.50, 1.00, 1.00, 1.20, 1.30};
        int[]    bestand = {5, 3, 5, 2, 4};

        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");

        // Menü anzeigen
        System.out.println("Unser Angebot:");
        for (int idx = 0; idx < namen.length; idx++) {
            if (bestand[idx] > 0) {
                System.out.println("  " + (idx + 1) + " - "
                    + namen[idx] + "  " + preise[idx] + " EUR");
            }
        }
        System.out.println();

        // Münzen einwerfen – while-Schleife                NEU ↓
        double gesamtBetrag = 0.0;
        boolean abbruch = false;

        System.out.println("Wirf Geld ein. Moegliche Muenzen: 0.10, 0.20, 0.50, 1.00, 2.00");

        while (true) {                                   // NEU ←
            System.out.print("Betrag einwerfen (oder 0 fuer fertig, -1 fuer Abbruch): ");
            double muenze = scanner.nextDouble();
            scanner.nextLine();

            if (muenze == -1) {                          // Abbruch
                abbruch = true;
                break;                                   // NEU ←
            } else if (muenze == 0) {                   // Fertig
                break;
            } else if (muenze > 0) {
                gesamtBetrag += muenze;                  // Aufaddieren
                System.out.println("  Eingeworfen: " + muenze
                    + " EUR  |  Aktuell: " + gesamtBetrag + " EUR");
            }
        }

        if (abbruch) {
            System.out.println("Abbruch! Rueckgabe: " + gesamtBetrag + " EUR");
        } else {
            System.out.println("Gesamtbetrag: " + gesamtBetrag + " EUR");
            System.out.print("Deine Wahl (1-5): ");
            int wahl = scanner.nextInt();
            int index = wahl - 1;

            if (index >= 0 && index < namen.length && bestand[index] > 0) {
                double preis = preise[index];
                if (gesamtBetrag >= preis) {
                    double rueckgeld = gesamtBetrag - preis;
                    bestand[index]--;
                    System.out.println("Getraenk ausgegeben: " + namen[index]);
                    System.out.println("Rueckgeld: " + rueckgeld + " EUR");
                } else {
                    System.out.println("Nicht genug Geld! Rueckgabe: " + gesamtBetrag + " EUR");
                }
            } else {
                System.out.println("Ungueltige Wahl. Rueckgabe: " + gesamtBetrag + " EUR");
            }
        }

        scanner.close();
    }

}
