public class KinoProgramm {

    public static void main(String[] args) {

        // 5 Filme x 7 Tage  (Zeile = Film, Spalte = Tag)
        // Index:  Mo   Di   Mi   Do   Fr   Sa   So
        int[][] programm = {
            {120,  85, 200, 175, 300, 410, 380},  // Film 0 – bester Tag: Sa
            {210, 340, 180, 160, 220, 270, 190},  // Film 1 – bester Tag: Di
            {200, 190, 210, 205, 450, 380, 420},  // Film 2 – bester Tag: Fr
            { 50, 140,  55, 170,  90, 150,  80},  // Film 3 – bester Tag: Do
            {170, 155, 390, 160, 240, 310, 280}   // Film 4 – bester Tag: Mi
        };

        // Gesamtverkäufe pro Film berechnen
        for (int film = 0; film < programm.length; film++) {

            int summe = 0;

            // alle Tage dieses Films aufsummieren
            for (int tag = 0; tag < programm[film].length; tag++) {
                summe = summe + programm[film][tag];
            }

            System.out.println("Film " + film + ": " + summe + " Tickets");
        }
    }
}
