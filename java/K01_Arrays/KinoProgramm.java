public class KinoProgramm {

    public static void main(String[] args) {

        // 5 Filme x 7 Tage  (Zeile = Film, Spalte = Tag)
        // Index:  Mo   Di   Mi   Do   Fr   Sa   So
        int[][] programm = {
            {120,  85, 200, 175, 300, 410, 380},  // Film 0
            { 95, 110, 130, 160, 220, 370, 340},  // Film 1
            {200, 190, 210, 205, 280, 450, 420},  // Film 2
            { 50,  60,  55,  70,  90, 150, 140},  // Film 3
            {170, 155, 180, 160, 240, 390, 360}   // Film 4
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
