public class KinoProgrammOOP {

    public static void main(String[] args) {

        // Film-Array: jedes Element ist ein Film-Objekt mit Metadaten + Verkaufszahlen
        // Statt int[][] programm verwenden wir jetzt Film[] programm
        Film[] programm = {
            new Film("Matrix",      136, "SciFi",    new int[]{120,  85, 200, 175, 300, 410, 380}),
            new Film("Barbie",      114, "Komoedie", new int[]{210, 340, 180, 160, 220, 270, 190}),
            new Film("Oppenheimer", 180, "Drama",    new int[]{200, 190, 210, 205, 450, 380, 420}),
            new Film("Dune",        155, "SciFi",    new int[]{ 50, 140,  55, 170,  90, 150,  80}),
            new Film("Avatar",      192, "SciFi",    new int[]{170, 155, 390, 160, 240, 310, 280})
        };

        // Alle Filme mit Gesamtverkäufen ausgeben
        for (int i = 0; i < programm.length; i++) {
            System.out.println(programm[i].toString());
        }

        System.out.println();

        // Erfolgreichsten Film ermitteln
        int maxIdx = 0;                               // Index 0 ist erster Kandidat
        for (int i = 1; i < programm.length; i++) {  // i=1: alle übrigen prüfen
            if (programm[i].getGesamtverkaufe() > programm[maxIdx].getGesamtverkaufe()) {
                maxIdx = i;
            }
        }
        System.out.println("Erfolgreichster Film: " + programm[maxIdx].getTitel());
    }
}
