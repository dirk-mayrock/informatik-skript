import java.util.Scanner;

/**
 * Praktikum 6 – Arrays, for-Schleife, for-each
 *
 * Neue Konzepte:
 *   - Array deklarieren und initialisieren: String[] namen = {...}
 *   - Array-Index: namen[0], namen[1] ...
 *   - .length → Anzahl der Elemente
 *   - for-Schleife mit Index: for (int i = 0; i < n; i++)
 *   - for-each-Schleife: for (String s : namen)
 *
 * Getränkeautomat – Schritt 6:
 * Alle 5 Getränke werden in Arrays gespeichert.
 * Das Menü wird automatisch per Schleife ausgegeben.
 */
public class GetraenkeListe {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // --- Arrays kennenlernen ---
        int[] zahlen = {10, 20, 30, 40, 50};           // NEU ←

        System.out.println("Array-Elemente:");
        for (int i = 0; i < zahlen.length; i++) {       // NEU ← (for mit Index)
            System.out.println("  zahlen[" + i + "] = " + zahlen[i]);
        }

        System.out.println();

        // for-each: eleganter, wenn kein Index gebraucht wird
        System.out.println("Dasselbe mit for-each:");
        for (int z : zahlen) {                          // NEU ← (for-each)
            System.out.println("  " + z);
        }

        System.out.println();

        // --- Getränkeautomat Schritt 6 ---
        // Alle 5 Getränke in Arrays speichern
        String[] namen  = {"Cola", "Apfelschorle", "Wasser", "Eistee", "Limo"};  // NEU ←
        double[] preise = {1.50,   1.00,           1.00,     1.20,     1.30};     // NEU ←
        int[]    bestand = {5,     3,               5,        2,        4};        // NEU ←

        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        System.out.println("Unser Angebot:");

        // Menü per Schleife ausgeben – kein Copy-Paste mehr!
        for (int i = 0; i < namen.length; i++) {        // NEU ←
            if (bestand[i] > 0) {
                System.out.println("  " + (i + 1) + " - "
                    + namen[i] + "  " + preise[i] + " EUR"
                    + "  (noch " + bestand[i] + " Dosen)");
            }
        }

        System.out.println();
        System.out.print("Deine Wahl (1-5): ");
        int wahl = scanner.nextInt();
        int index = wahl - 1;  // Array ist 0-basiert!

        if (index >= 0 && index < namen.length && bestand[index] > 0) {
            System.out.println("Du hast gewaehlt: " + namen[index]);
            System.out.println("Preis: " + preise[index] + " EUR");
        } else {
            System.out.println("Ungueltige Wahl oder ausverkauft.");
        }

        scanner.close();
    }

}
