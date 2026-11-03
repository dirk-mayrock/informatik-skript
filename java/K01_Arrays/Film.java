public class Film {

    // Attribute (private – nur über Getter zugänglich)
    private String titel;
    private int    dauer;       // Laufzeit in Minuten
    private String genre;
    private int[]  verkaufe;    // Ticketverkäufe Mo bis So (7 Werte)

    // Konstruktor
    public Film(String titel, int dauer, String genre, int[] verkaufe) {
        this.titel    = titel;
        this.dauer    = dauer;
        this.genre    = genre;
        this.verkaufe = verkaufe;
    }

    // Getter
    public String getTitel()    { return titel; }
    public int    getDauer()    { return dauer; }
    public String getGenre()    { return genre; }
    public int[]  getVerkaufe() { return verkaufe; }

    // Hilfsmethode: Gesamtverkäufe über alle 7 Tage
    public int getGesamtverkaufe() {
        int summe = 0;
        for (int i = 0; i < verkaufe.length; i++) {
            summe = summe + verkaufe[i];
        }
        return summe;
    }

    // Textdarstellung des Films
    public String toString() {
        return titel + " (" + genre + ", " + dauer + " min)"
               + " - " + getGesamtverkaufe() + " Tickets";
    }
}
