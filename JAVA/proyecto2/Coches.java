public class Coches {

    static String[] coches = {"Audi", "Mercedes", "Seat", "FOrd", "Volvo"}; //variable global a la clase

    public static void main(String[] args) {

        for (int i = 0; i < 5; i++) {
            if ((i == 3) || (i == 4)) continue;            
            System.out.println("Iteracion-" + i + "-For");
        }

        //ver coches
        verCoches(coches);

    }

    public static void verCoches(String[] listaCoches) {
        
        String nombre = "maria"; //variable local

        //for each
        for (String coche : listaCoches) {
            /* if ((coche.contains("o")) || (coche.contains("O"))) {
                System.out.println(coche);
            } */
            if (coche.toLowerCase().contains("o")) {
                System.out.println(coche);
            }

        }
    }

}