import java.util.Scanner;

/**
 * Praktikum 5 – switch
 *
 * Neue Konzepte:
 *   - switch / case / break / default
 *   - Wann switch statt if-else? → bei festen Einzelwerten
 *
 * Getränkeautomat – Schritt 5:
 * Der Nutzer wählt eine Nummer (1–5). Per switch wird das
 * passende Getränk mit seinem Preis ausgewählt.
 */
public class SwitchBeispiel {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // --- switch kennenlernen ---
        int tag = 3;

        switch (tag) {                                    // NEU ←
            case 1:                                       // NEU ←
                System.out.println("Montag");
                break;                                    // NEU ← (verhindert Durchfallen)
            case 2:
                System.out.println("Dienstag");
                break;
            case 3:
                System.out.println("Mittwoch");
                break;
            default:                                      // NEU ← (alle anderen Werte)
                System.out.println("Ein anderer Tag");
        }

        System.out.println();

        // --- Getränkeautomat Schritt 5 ---
        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        System.out.println("  1 - Cola          1.50 EUR");
        System.out.println("  2 - Apfelschorle  1.00 EUR");
        System.out.println("  3 - Wasser        1.00 EUR");
        System.out.println("  4 - Eistee        1.20 EUR");
        System.out.println("  5 - Limo          1.30 EUR");
        System.out.println();

        System.out.print("Deine Wahl (1-5): ");
        int wahl = scanner.nextInt();

        String gewaehltesGetraenk;
        double gewaehlterPreis;

        switch (wahl) {                                   // NEU ←
            case 1:
                gewaehltesGetraenk = "Cola";
                gewaehlterPreis    = 1.50;
                break;
            case 2:
                gewaehltesGetraenk = "Apfelschorle";
                gewaehlterPreis    = 1.00;
                break;
            case 3:
                gewaehltesGetraenk = "Wasser";
                gewaehlterPreis    = 1.00;
                break;
            case 4:
                gewaehltesGetraenk = "Eistee";
                gewaehlterPreis    = 1.20;
                break;
            case 5:
                gewaehltesGetraenk = "Limo";
                gewaehlterPreis    = 1.30;
                break;
            default:
                gewaehltesGetraenk = "Unbekannt";
                gewaehlterPreis    = 0.00;
                System.out.println("Ungueltige Auswahl!");
        }

        if (!gewaehltesGetraenk.equals("Unbekannt")) {
            System.out.println("Du hast gewaehlt: " + gewaehltesGetraenk);
            System.out.println("Preis: " + gewaehlterPreis + " EUR");
        }

        scanner.close();
    }

}
