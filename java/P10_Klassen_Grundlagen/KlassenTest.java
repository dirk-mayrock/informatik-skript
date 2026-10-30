import java.util.Scanner;

/**
 * Praktikum 10 – Klassen Grundlagen
 *
 * Testklasse: KlassenTest
 *
 * Hier verwenden wir die Klasse Getraenk.
 * Statt drei paralleler Arrays haben wir jetzt ein
 * Array von Getraenk-Objekten.
 *
 * Starte das Programm hier über die main()-Methode.
 */
public class KlassenTest {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        // --- Einzelnes Objekt erzeugen ---             NEU ←
        Getraenk cola = new Getraenk("Cola", 1.50, 5);  // NEU ←
        System.out.println("Objekt cola:");
        System.out.println("  Name:    " + cola.name);
        System.out.println("  Preis:   " + cola.preis + " EUR");
        System.out.println("  Bestand: " + cola.bestand);
        System.out.println("  Verfuegbar: " + cola.istVerfuegbar());

        System.out.println();

        // --- Array von Objekten ---                    NEU ←
        Getraenk[] automat = new Getraenk[5];
        automat[0] = new Getraenk("Cola",         1.50, 5);
        automat[1] = new Getraenk("Apfelschorle", 1.00, 3);
        automat[2] = new Getraenk("Wasser",       1.00, 5);
        automat[3] = new Getraenk("Eistee",       1.20, 2);
        automat[4] = new Getraenk("Limo",         1.30, 4);

        System.out.println("============================");
        System.out.println(" Getraenkeautomat");
        System.out.println("============================");
        System.out.println("Unser Angebot:");

        for (int i = 0; i < automat.length; i++) {
            if (automat[i].istVerfuegbar()) {
                System.out.print("  " + (i + 1) + " - ");
                automat[i].zeigeInfo();
            }
        }

        System.out.println();
        System.out.print("Deine Wahl (1-5): ");
        int wahl = scanner.nextInt();
        int index = wahl - 1;

        if (index >= 0 && index < automat.length && automat[index].istVerfuegbar()) {
            System.out.println("Du hast gewaehlt: " + automat[index].name);
            System.out.println("Preis: " + automat[index].preis + " EUR");
        } else {
            System.out.println("Ungueltige Wahl oder ausverkauft.");
        }

        scanner.close();
    }

}
