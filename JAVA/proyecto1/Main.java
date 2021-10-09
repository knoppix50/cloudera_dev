
public class Main {
	public static void main(String[] args) {
		String nombre = null;
		//System.out.println("Hola " + args[0]);
		//tipos de variables
		if ((args.length > 0) && (args.length < 2)) { //estructura condicional - bloque de codigo
			nombre = args[0]; //declaracion de variable y asignacion de valor
			String nombreMinuscula = nombre.toLowerCase();
			System.out.println("El nombre en minuscula es " + nombreMinuscula);
		} else {
			System.out.println("Te has olvidado el argumento(s) o bien has utilizado mas de un argumento");
		}

		if (!(nombre == null)) {
			System.out.println(nombre);
		}

		//otro tipo de variables
		int edad = 34; //tipo primitivo
		float nota = 4.56f;
		double notaCorte = 4.67;
		boolean casado = true; //true o false
		char letra = 'a';
		Integer altura = 123;

		int resultado = 11 + 8; //-, *, /, %
		System.out.println("El resultado de la suma es " + resultado);

		float resDivision = resultado / 3f;
		System.out.println("El resultado de la division es " + resDivision);

		if (resultado % 4 == 0) { //divisible entre 4
			System.out.println("El resultdo es divisible entre 4");
		} else {
			System.out.println("El resultdo NO es divisible entre 4");
		}
		
		
		

	}
}  
