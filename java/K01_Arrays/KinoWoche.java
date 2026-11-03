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
        int maxIndex = 0;                             // starte mit Index 0
        for (int i = 1; i < verkaufe.length; i++) {  // ab Index 1 vergleichen
            if (verkaufe[i] > verkaufe[maxIndex]) {
                maxIndex = i;                         // neuen Besttag merken
            }
        }
        System.out.println("Bester Tag: Index " + maxIndex
                           + " mit " + verkaufe[maxIndex] + " Tickets");
    }
}
