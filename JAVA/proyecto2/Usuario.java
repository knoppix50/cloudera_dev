import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;


public class Usuario {

    private static List<String> usuarios = new ArrayList<String>(); 

    public static void main(String[] args) {
         Usuario user = new Usuario();
         user.iniciarProceso();
         //new Usuario().iniciarProceso();
         obtenerUsuarios();
    }

    private static void obtenerUsuarios() {

        //recoger alias de usuario
        Scanner reader = new Scanner(System.in);
        
        /* //primera peticion
        System.out.println("Introduzca alias:");
        String alias = reader.next();
        
        //resto de peticiones
        while (!alias.equals("*")) {
            System.out.println("Introduzca alias:");
            alias = reader.next();
            System.out.println(alias);
        } */
        
        String alias;
        do {

            System.out.println("Introduzca alias:");
            alias = reader.next();
            //System.out.println(alias);
            if (!alias.equals("*")) {
                usuarios.add(alias);
            }
            
            
        } while(!alias.equals("*"));

        
        if (usuarios.size() > 0) {
            mostrarAlias(usuarios);
        }
        
        

    }

    private static void mostrarAlias(List<String> lista) {
        
        System.out.println("******Mostrar alias************");
        for (String alias:lista) {
            System.out.println(alias);
        }
    }

    public void iniciarProceso() {
        System.out.println("_____Iniciando proceso______");
    }
}