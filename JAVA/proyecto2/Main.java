//estructuras iterativas

public class Main {

    public static void main(String[] args) {
        int i = 0;
       
        if (args.length == 1) {
            int interruptor = Integer.parseInt(args[0]);

            while ((interruptor == 1) && (i < 5)) {
                System.out.println("Iteracion");
                i = i + 1;
            }
             
        } else {
            System.out.println("Falta parametro:0 o 1");
        }
    }
}