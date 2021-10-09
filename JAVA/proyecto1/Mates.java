public class Mates {

    //punto de entrada

    //captura de los dos argumentos del programa
    //progranacion defensiva. Asegurar que son dos los argumentos 
    public static void main(String[] args) {
        int num1, num2;
        
        if (args.length == 2) {

            try {
                
                num1 = Integer.parseInt(args[0]);
                num2 = Integer.parseInt(args[1]);

                int numeroMaximo = Math.max(num1, num2);
                System.out.println("El mayor de los numeros introducidos es " + numeroMaximo);

                //control de casos para numeroMaximo (if de multiple rama)
                
                /* if (numeroMaximo == 4) {
                    System.out.println("Abortar proceso");
                } else if (numeroMaximo == 5) {
                    System.out.println("Suspender proceso");
                } else if (numeroMaximo == 7) {
                    System.out.println("Activar subproceso");
                } else {
                    System.out.println("Proceso en marcha");
                } */

                switch (numeroMaximo) {
                    case 4:
                    case 5:
                        System.out.println("Suspender proceso");
                        break;
                    case 7:
                         System.out.println("Activar subproceso");
                         break;
                    case 9:
                        System.out.println("Parar proceso");
                        break;
                    case 12:
                         System.out.println("Reactivar proceso");
                         break;
                    default:
                         System.out.println("Proceso en marcha");
                }
                


            } catch (NumberFormatException ex) {

                System.out.println("Formato de entrada invalido");
            } finally {

            }
            

        } else {
            System.out.println("Num. argumentos invalido");
        }
        
        

    }

}