public class KinoWoche {

    public static void main(String[] args) {

        // Ticketverkäufe Mo bis So (Index 0 = Montag, Index 6 = Sonntag)
        int[] verkaufe = {120, 85, 200, 175, 300, 410, 380};

        // --- Gesamtverkäufe berechnen ---
        int summe = 0;
        for (int i = 0; i < verkaufe.length; i++) {
            summe = summe + verkaufe[i];  // jeden Wert addieren
        }
        System.out.println("Gesamt: " + summe + " Tickets");

        // --- Besten Tag ermitteln ---
        int maxIndex = 0;                             // Index 0 ist erster Kandidat
        for (int i = 1; i < verkaufe.length; i++) {  // i=1: alle übrigen dagegen prüfen
            if (verkaufe[i] > verkaufe[maxIndex]) {
                maxIndex = i;                         // besseren Tag merken
            }
        }
        System.out.println("Bester Tag: Index " + maxIndex
                           + " mit " + verkaufe[maxIndex] + " Tickets");
    }
}
