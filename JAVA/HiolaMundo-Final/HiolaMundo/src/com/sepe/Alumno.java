package com.sepe;

import java.util.ArrayList;
import java.util.List;

public class Alumno extends Persona {

    private float notaFinal;
    private List<Asignatura> asignaturas;
    private Tematica tematicaEstudio;
    private float[] expedienteAcademico = new float[]{6.5f,8.9f,3.7f,8.5f};
    private boolean admitido;

    public float[] getExpedienteAcademico() {
        return expedienteAcademico;
    }

    //getter
    public float getNotaFinal() {
        return notaFinal;
    }

    //setter
    public void setNotaFinal(float notaFinal) {
        this.notaFinal = notaFinal;
    }

    public Tematica getTematicaEstudio() {
        return tematicaEstudio;
    }

    public boolean isAdmitido() {
        return admitido;
    }

    public void setAdmitido(boolean admitido) {
        this.admitido = admitido;
    }

    //constructor
    public Alumno(String nombre, String apellido, String dni, Tematica tem) {
        super(nombre, apellido, dni); //la invocacion a super siempre es la primera linea
        this.tematicaEstudio = tem;
        this.admitido = false;
    }

    public void crearAsignaturas(/*Tematica tematica*/) {
        //TODO:realizar el codigo de creacion de asignatura
        List<Asignatura> asigs = new ArrayList<>();
        switch (this.tematicaEstudio) {
            case BIG_DATA:
                asigs.add(new Asignatura("Spark"));
                asigs.add(new Asignatura("Algebra"));
                break;
            case PYTHON:
                asigs.add(new Asignatura("POO"));
                asigs.add(new Asignatura("Variables y Funciones"));
                break;
            case CIENCIA_DATOS:
                break;
            case CIBERSEGURIDAD:
                break;
            case CLOUD:
                break;
            default:
        }
        this.asignaturas = asigs;
    }

    //sobre-escritura
    @Override
    public String toString() {

        return super.toString() + "Alumno{" +
                "asignaturas=" + asignaturas +
                ", tematicaEstudio=" + tematicaEstudio +
                '}';
    }

    private class Asignatura {
        private String nombre;
        private float nota;

        public String getNombre() {
            return nombre;
        }

        public float getNota() {
            return nota;
        }

        public Asignatura(String nombre) {
            this.nombre = nombre;
        }

        public void setNota(float nota) {
            this.nota = nota;
        }
    }
}
