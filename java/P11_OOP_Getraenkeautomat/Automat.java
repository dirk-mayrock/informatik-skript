import java.util.Scanner;

/**
 * Praktikum 11 – OOP Getränkeautomat
 *
 * Klasse: Automat  (Startklasse – enthält main)
 *
 * Orchestriert Getraenk[] und Geldfach.
 * Kapselt alle Automat-Logik in Methoden.
 *
 * UML-Übersicht:
 *
 *   Automat
 *     - getraenke : Getraenk[]
 *     - geldfach  : Geldfach
 *     + zeigeMenu()
 *     + geldPhase()
 *     + kaufPhase()
 *     + start()
 *     + main()
 *
 *   Getraenk                Geldfach
 *     - name : String         - betrag : double
 *     - preis : double        + einwerfen(double)
 *     - bestand : int         + abziehen(double)
 *     + ausgeben()            + zurueckgeben()
 *     + toString()            + wechselgeldAlsText()
 */
public class Automat {

    // --- Attribute ---
    private Getraenk[] getraenke;
    private Geldfach   geldfach;
    private Scanner    scanner;

    // --- Konstruktor ---
    public Automat() {
        geldfach = new Geldfach();
        scanner  = new Scanner(System.in);

        // Getränke befüllen
        getraenke = new Getraenk[5];
        getraenke[0] = new Getraenk("Cola",         1.50, 5);
        getraenke[1] = new Getraenk("Apfelschorle", 1.00, 3);
        getraenke[2] = new Getraenk("Wasser",       1.00, 5);
        getraenke[3] = new Getraenk("Eistee",       1.20, 2);
        getraenke[4] = new Getraenk("Limo",         1.30, 4);
    }

    // --- Menü ausgeben ---
    public void zeigeMenu() {
        System.out.println("============================");
        System.out.println(" Getraenkeautomat  v2.0");
        System.out.println("============================");
        System.out.println("Unser Angebot:");
        for (int i = 0; i < getraenke.length; i++) {
            if (getraenke[i].istVerfuegbar()) {
                System.out.println("  " + (i + 1) + " - " + getraenke[i]);
            }
        }
        System.out.println("  0 - Abbruch");
        System.out.println();
    }

    // --- Geld-Phase: Münzen einwerfen ---
    public boolean geldPhase() {
        System.out.println("Muenzen einwerfen:");
        System.out.println("  Gueltige Werte: 0.10  0.20  0.50  1.00  2.00");
        System.out.println("  0    = fertig");
        System.out.println("  -1   = Abbruch");

        while (true) {
            System.out.printf("  Aktuell: %s  |  Muenze: ", geldfach);
            double eingabe = scanner.nextDouble();
            scanner.nextLine();

            if (eingabe == -1) {
                double zurueck = geldfach.zurueckgeben();
                System.out.printf("Abbruch. Rueckgabe: %.2f EUR%n", zurueck);
                return false;
            }
            if (eingabe == 0) {
                break;
            }
            if (!geldfach.einwerfen(eingabe)) {
                System.out.println("  Ungueltige Muenze – bitte nochmal.");
            }
        }
        return true;
    }

    // --- Kauf-Phase: Getränk wählen und ausgeben ---
    public void kaufPhase() {
        System.out.printf("Gesamtbetrag: %s%n", geldfach);
        System.out.print("Deine Wahl (1-5, 0 = Abbruch): ");
        int wahl = scanner.nextInt();
        scanner.nextLine();

        if (wahl == 0) {
            double r = geldfach.zurueckgeben();
            System.out.printf("Abbruch. Rueckgabe: %.2f EUR%n", r);
            return;
        }

        int index = wahl - 1;
        if (index < 0 || index >= getraenke.length) {
            System.out.println("Ungueltige Auswahl.");
            System.out.println("Rueckgabe: " + geldfach.wechselgeldAlsText());
            geldfach.zurueckgeben();
            return;
        }

        Getraenk g = getraenke[index];

        if (!g.istVerfuegbar()) {
            System.out.println(g.getName() + " ist ausverkauft.");
            System.out.println("Rueckgabe: " + geldfach.wechselgeldAlsText());
            geldfach.zurueckgeben();
            return;
        }

        if (geldfach.getBetrag() < g.getPreis()) {
            System.out.printf("Nicht genug Geld! Fehlen: %.2f EUR%n",
                g.getPreis() - geldfach.getBetrag());
            System.out.println("Rueckgabe: " + geldfach.wechselgeldAlsText());
            geldfach.zurueckgeben();
            return;
        }

        // Kauf erfolgreich
        geldfach.abziehen(g.getPreis());
        g.ausgeben();
        System.out.println(">>> " + g.getName() + " wird ausgegeben! <<<");

        if (geldfach.getBetrag() > 0) {
            System.out.println("Wechselgeld: " + geldfach.wechselgeldAlsText());
            geldfach.zurueckgeben();
        }
    }

    // --- Hauptschleife ---
    public void start() {
        System.out.println("Willkommen beim Getraenkeautomaten!");
        boolean weiter = true;

        while (weiter) {
            zeigeMenu();

            boolean geldOk = geldPhase();
            if (geldOk) {
                kaufPhase();
            }

            System.out.println();
            System.out.print("Nochmal? (j/n): ");
            String antwort = scanner.nextLine();
            weiter = antwort.equalsIgnoreCase("j");
        }

        System.out.println("Auf Wiedersehen!");
        scanner.close();
    }

    // --- main ---
    public static void main(String[] args) {
        Automat a = new Automat();
        a.start();
    }

}
