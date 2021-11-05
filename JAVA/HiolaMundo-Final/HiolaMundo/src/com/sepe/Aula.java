package com.sepe;

import com.sepe.calculadora.Calculadora;

import java.util.ArrayList;
import java.util.List;

public class Aula {

    //atributos :: estado
    private List<Alumno> alumnos = new ArrayList<>();
    private Tematica tematica;

    public List<Alumno> getAlumnos() {
        return alumnos;
    }

    public Tematica getTematica() {
        return tematica;
    }

    public void setTematica(Tematica tematica) {
        this.tematica = tematica;
    }


    public Aula() {
        this.tematica = Tematica.PYTHON;
    }
    public Aula(Tematica tematica) {
        this.tematica = tematica;
    }

    //comportamiento
    public void anyadirAlumno(Alumno al) {
        al.setNotaFinal(7.5f);
        alumnos.add(al);
    }

    public void mostrarAlumnos() {
        String datosCompletos = null;

        for(Alumno al: alumnos) {
            datosCompletos = String.format("%s %s - %s",al.getNombre(),al.getApellido(),al.getDni());
            System.out.println(datosCompletos);
        }
    }

    public float obtenerNotaMedia() {
        Calculadora calc = new Calculadora();
        //1.- recorrer la lista de alumnos
        //2.- sumar todas sus notas
        //3.- Divir el resultado de la suma entre el num. de alumnos
        //4.- devolver resultado
        float sumatorio = 0.0f;
        float media = -1;
        for (Alumno al: alumnos) {
            //sumatorio = sumatorio + al.getNotaFinal();
            //sumatorio += al.getNotaFinal();
            sumatorio = calc.sumar(sumatorio, al.getNotaFinal());
        }

        /*
        media = sumatorio / alumnos.size();
        return media;
        */
        //return sumatorio / alumnos.size();
        return calc.dividir(sumatorio, alumnos.size());


    }
}
