import java.util.Scanner;

/**
 * Praktikum 3 – Konsoleneingabe mit Scanner
 *
 * Neue Konzepte:
 *   - import java.util.Scanner
 *   - Scanner-Objekt anlegen
 *   - nextLine()   → liest eine Textzeile (String)
 *   - nextInt()    → liest eine Ganzzahl
 *   - nextDouble() → liest eine Kommazahl
 *   - System.out.print() ohne Zeilenumbruch
 *
 * Getränkeautomat – Schritt 3:
 * Der Nutzer tippt seinen Namen und wählt ein Getränk.
 */
public class Konsoleneingabe {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);  // NEU ←

        // --- Einfache Eingabe: Text ---
        System.out.print("Wie heisst du? ");        // print ohne ln → kein Umbruch
        String nutzername = scanner.nextLine();     // NEU ←
        System.out.println("Hallo, " + nutzername + "!");

        System.out.println();

        // --- Eingabe: Ganzzahl ---
        System.out.print("Wie alt bist du? ");
        int alter = scanner.nextInt();              // NEU ←
        System.out.println("Du bist " + alter + " Jahre alt.");

        // Wichtig: Nach nextInt() muss nextLine() aufgerufen werden,
        // um den Zeilenumbruch zu "schlucken"
        scanner.nextLine();                         // NEU ← (Pufferbereinigung)

        System.out.println();

        // --- Getränkeautomat Schritt 3 ---
        System.out.println("============================");
        System.out.println(" Willkommen beim");
        System.out.println(" Getraenkeautomaten!");
        System.out.println("============================");
        System.out.println("Unser Angebot:");
        System.out.println("  1 - Cola          1.50 EUR");
        System.out.println("  2 - Apfelschorle  1.00 EUR");
        System.out.println("  3 - Wasser        1.00 EUR");
        System.out.println();

        System.out.print("Welches Getraenk moechtest du? (Nummer eingeben): ");
        int wahl = scanner.nextInt();               // NEU ←
        System.out.println("Du hast Getraenk Nr. " + wahl + " gewaehlt.");

        scanner.close();
    }

}
