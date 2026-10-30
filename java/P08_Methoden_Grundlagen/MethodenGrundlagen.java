/**
 * Praktikum 8 – Methoden Grundlagen
 *
 * Neue Konzepte:
 *   - Methode deklarieren: public static void name()
 *   - Methode mit Parameter: public static void name(int x)
 *   - Methode mit Rückgabewert: public static int name(int x)
 *   - return-Anweisung
 *   - Methode aufrufen
 *   - Warum Methoden? → kein Code-Copy-Paste, bessere Lesbarkeit
 *
 * Getränkeautomat – Schritt 8:
 * Wir lagern wiederkehrende Code-Teile in eigene Methoden aus:
 *   zeigeMenu()     → gibt das Menü aus
 *   berechneBetrag() → addiert Münzen
 */
public class MethodenGrundlagen {

    // --- Methode ohne Parameter, ohne Rückgabewert ---
    public static void sagHallo() {                      // NEU ←
        System.out.println("Hallo aus einer Methode!");
    }

    // --- Methode mit Parameter ---
    public static void begruesse(String name) {          // NEU ←
        System.out.println("Hallo, " + name + "!");
    }

    // --- Methode mit Rückgabewert ---
    public static int addiere(int a, int b) {            // NEU ←
        return a + b;                                    // NEU ←
    }

    // --- Methode: max von zwei Zahlen ---
    public static double maximum(double x, double y) {
        if (x >= y) {
            return x;
        } else {
            return y;
        }
    }

    // --- Getränkeautomat: Menü ausgeben ---
    public static void zeigeMenu(String[] namen, double[] preise, int[] bestand) {  // NEU ←
        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        System.out.println("Unser Angebot:");
        for (int i = 0; i < namen.length; i++) {
            if (bestand[i] > 0) {
                System.out.println("  " + (i + 1) + " - "
                    + namen[i] + "  " + preise[i] + " EUR"
                    + "  (noch " + bestand[i] + ")");
            }
        }
        System.out.println();
    }

    // --- Getränkeautomat: Betrag addieren ---
    public static double addiereMuenze(double gesamtBetrag, double muenze) {  // NEU ←
        return gesamtBetrag + muenze;
    }

    // --------------------------------------------------------
    public static void main(String[] args) {

        // Methoden aufrufen
        sagHallo();                                      // NEU ←
        begruesse("Hannah");                             // NEU ←

        int summe = addiere(3, 4);                       // NEU ←
        System.out.println("3 + 4 = " + summe);

        System.out.println("Max(2.5, 7.1) = " + maximum(2.5, 7.1));

        System.out.println();

        // Getränkeautomat – Methoden einsetzen
        String[] namen  = {"Cola", "Apfelschorle", "Wasser", "Eistee", "Limo"};
        double[] preise = {1.50, 1.00, 1.00, 1.20, 1.30};
        int[]    bestand = {5, 3, 5, 2, 4};

        zeigeMenu(namen, preise, bestand);               // Einzeiler statt 8 Zeilen!

        double betrag = 0.0;
        betrag = addiereMuenze(betrag, 1.00);
        betrag = addiereMuenze(betrag, 0.50);
        System.out.println("Eingeworfener Betrag: " + betrag + " EUR");
    }

}
