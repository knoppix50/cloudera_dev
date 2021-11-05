package com.sepe;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Main {

    //atributos
    //declarar aula; inicializar aula
    private Aula aula = new Aula(Tematica.BIG_DATA);

    //getter
    public Aula getAula() {
        return aula;
    }

    public static void main(String[] args) {
        String[] nombres = {"Miguel", "Sonia", "Berta", "Juan", "Jaime", "Clara"};
        String[] apellidos = {"Lopez", "Barberan", "Fernandez", "Echanove", "Labordeta", "Del Rio"};
        String[] dnis = {"111H", "222H", "333H", "444H", "555H", "666H"};

        //proceso equivalente pero con HashMap (Diccionario)
        HashMap<String,String> datosCandidatos = new HashMap<>();
        datosCandidatos.put("111H","Miguel Lopez");
        datosCandidatos.put("222H","Sonia Barberan");
        datosCandidatos.put("333H","Berta Echanove");
        datosCandidatos.put("444H","Juan Lopez");
        datosCandidatos.put("555H","Jaime Del Rio");


        System.out.println("Gestion Academica");
        Main app = new Main(); //instanciar un objeto llamado app de la clase Main

        //anyadir varios alumnos y alumnas
        //app.cargarAlumnos(nombres, apellidos, dnis); //1a forma nyapa
        app.cargarAlumnos(datosCandidatos);

        //listar alumnos
        app.mostrarAlumnos(app.getAula());

        //mostrar nota media del aula
        System.out.println("Media aula:" + app.obtenerMediaAula());

        //creacion del centro educativo (solo una instancia)
        CentroEducativo pue = new CentroEducativo("Proyecto Universidad Empresa", TipoCentro.TECNOLOGICO);
        //test de un alumno
        //Alumno miguel = app.getAula().getAlumnos().get(0);
        List<Alumno> candidatos = app.getAula().getAlumnos();
        for(Alumno candidato: candidatos) {
            if (pue.admitirAlumno(candidato)) {
                System.out.println("Alumno admitido con DNI:" + candidato.getDni());
                candidato.setAdmitido(true);
                System.out.println(candidato);
                pue.asignarAlumno(candidato);

            } else {
                System.out.println("Lo sentimos pero el alumno con DNI " + candidato.getDni()+ " no ha sido admitido.");
            }
        }
    }
    private boolean cargarAlumnos(HashMap<String, String> candidatos) {
        String nombreYApellido, nombre, apellido, dni;

        try {
            for (String clave : candidatos.keySet()) {
                nombreYApellido = candidatos.get(clave);
                nombre = nombreYApellido.split(" ")[0];
                apellido = nombreYApellido.split(" ")[1];
                Alumno al = new Alumno(nombre, apellido, clave,Tematica.PYTHON);
                anyadirAlumno(al, aula);
            }
            return true;

        } catch (Exception ex) {
            return false;
        }
    }

    private boolean cargarAlumnos(String[] listaNombres, String[] listaApellidos, String[] listaDnis) {
        try {
            for (int i = 0; i < listaNombres.length; i++) {
                Alumno al = new Alumno(listaNombres[i], listaApellidos[i], listaDnis[i], Tematica.PYTHON);
                anyadirAlumno(al, aula);
            }
            return true;
        } catch (Exception ex) {
            return false;
        }

    }

    //metodo no estatico para anyadir un alumno
    private void anyadirAlumno(Alumno al, Aula a) {
        a.anyadirAlumno(al);
    }

    private void mostrarAlumnos(Aula aula) {
        aula.mostrarAlumnos();


    }

    public float obtenerMediaAula() {
        //llamadas delegadas
        return this.aula.obtenerNotaMedia();
    }

}
