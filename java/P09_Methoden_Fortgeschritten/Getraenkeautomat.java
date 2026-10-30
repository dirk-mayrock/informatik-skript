import java.util.Scanner;

/**
 * Praktikum 9 – Methoden Fortgeschritten
 *                → Vollständiger prozeduraler Getränkeautomat
 *
 * Neue Konzepte:
 *   - Methoden-Überladen (Overloading): gleicher Name, verschiedene Parameter
 *   - Konstanten mit final
 *   - Geltungsbereich (Scope) von Variablen
 *   - Wechselgeld-Algorithmus (Münz-Stückelung)
 *
 * Getränkeautomat – Schritt 9:
 * Vollständiges, funktionierendes Programm mit sauber getrennten Methoden.
 * Danach folgt in P10/P11 die OOP-Version.
 */
public class Getraenkeautomat {

    // --- Konstanten ---                                NEU ←
    static final int    ANZAHL_GETRAENKE   = 5;
    static final int    MAX_BESTAND        = 5;
    static final double[] MUENZEN          = {2.00, 1.00, 0.50, 0.20, 0.10};

    static String[] namen  = {"Cola", "Apfelschorle", "Wasser", "Eistee", "Limo"};
    static double[] preise = {1.50, 1.00, 1.00, 1.20, 1.30};
    static int[]    bestand = {5, 3, 5, 2, 4};

    // --------------------------------------------------------
    // Menü anzeigen
    // --------------------------------------------------------
    public static void zeigeMenu() {
        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        System.out.println("Unser Angebot:");
        for (int i = 0; i < namen.length; i++) {
            if (bestand[i] > 0) {
                System.out.printf("  %d - %-15s %.2f EUR  (%d Dosen)%n",
                    (i + 1), namen[i], preise[i], bestand[i]);
            }
        }
        System.out.println("  0 - Abbruch");
        System.out.println();
    }

    // --------------------------------------------------------
    // Münzen einsammeln bis Nutzer "fertig" signalisiert
    // --------------------------------------------------------
    public static double geldEinwerfen(Scanner scanner) {
        double betrag = 0.0;
        System.out.println("Wirf Muenzen ein (0 = fertig, -1 = Abbruch):");
        System.out.println("Moegliche Werte: 0.10  0.20  0.50  1.00  2.00");

        while (true) {
            System.out.printf("  Aktuell: %.2f EUR  |  Muenze: ", betrag);
            double muenze = scanner.nextDouble();
            scanner.nextLine();

            if (muenze == -1) return -1;   // Signal fuer Abbruch
            if (muenze == 0)  break;

            if (muenze == 0.10 || muenze == 0.20 || muenze == 0.50
                    || muenze == 1.00 || muenze == 2.00) {
                betrag += muenze;
                // Rundungsfehler bei double vermeiden
                betrag = Math.round(betrag * 100) / 100.0;
            } else {
                System.out.println("  Unbekannte Muenze – bitte nochmal.");
            }
        }
        return betrag;
    }

    // --------------------------------------------------------
    // Wechselgeld ausgeben (mit Stückelung)               NEU ←
    // --------------------------------------------------------
    public static void gibWechselgeld(double betrag) {
        if (betrag <= 0) return;

        System.out.printf("Wechselgeld: %.2f EUR  →  ", betrag);
        int cents = (int) Math.round(betrag * 100);    // in Cent umrechnen

        for (double muenze : MUENZEN) {                 // NEU ← (for-each über Konstante)
            int muenzCents = (int) Math.round(muenze * 100);
            int anzahl = cents / muenzCents;
            if (anzahl > 0) {
                System.out.print(anzahl + " × " + muenze + " EUR  ");
                cents -= anzahl * muenzCents;
            }
        }
        System.out.println();
    }

    // --------------------------------------------------------
    // Getränk kaufen
    // --------------------------------------------------------
    public static void kaufeGetraenk(int wahl, double betrag) {
        int index = wahl - 1;

        if (index < 0 || index >= ANZAHL_GETRAENKE) {
            System.out.println("Ungueltige Auswahl!");
            gibWechselgeld(betrag);
            return;
        }

        if (bestand[index] == 0) {
            System.out.println(namen[index] + " ist leider ausverkauft.");
            gibWechselgeld(betrag);
            return;
        }

        double preis = preise[index];

        if (betrag >= preis) {
            bestand[index]--;
            System.out.println(">>> " + namen[index] + " wird ausgegeben! <<<");
            gibWechselgeld(betrag - preis);
        } else {
            System.out.printf("Nicht genug Geld! Fehlen: %.2f EUR%n", preis - betrag);
            System.out.println("Rueckgabe: " + betrag + " EUR");
        }
    }

    // --------------------------------------------------------
    // Überladen (Overloading): kaufeGetraenk mit String-Name NEU ←
    // --------------------------------------------------------
    public static void kaufeGetraenk(String getraenkName, double betrag) {
        for (int i = 0; i < namen.length; i++) {
            if (namen[i].equalsIgnoreCase(getraenkName)) {
                kaufeGetraenk(i + 1, betrag);
                return;
            }
        }
        System.out.println("Getraenk '" + getraenkName + "' nicht gefunden.");
        gibWechselgeld(betrag);
    }

    // --------------------------------------------------------
    // Hauptprogramm – alles zusammen
    // --------------------------------------------------------
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        boolean weiter = true;

        while (weiter) {
            zeigeMenu();

            double betrag = geldEinwerfen(scanner);

            if (betrag == -1) {
                System.out.println("Abbruch. Kein Geld eingeworfen.");
            } else {
                System.out.printf("Gesamtbetrag: %.2f EUR%n", betrag);
                System.out.print("Deine Wahl (1-5, 0 = Abbruch): ");
                int wahl = scanner.nextInt();
                scanner.nextLine();

                if (wahl == 0) {
                    System.out.println("Abbruch.");
                    gibWechselgeld(betrag);
                } else {
                    kaufeGetraenk(wahl, betrag);
                }
            }

            System.out.println();
            System.out.print("Nochmal? (j/n): ");
            String antwort = scanner.nextLine();
            weiter = antwort.equalsIgnoreCase("j");
        }

        System.out.println("Auf Wiedersehen!");
        scanner.close();
    }

}
