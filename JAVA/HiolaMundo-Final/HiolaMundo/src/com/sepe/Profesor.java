package com.sepe;

public class Profesor extends Persona {

    private Tematica tematica;

    public Profesor(String nombre, String apellido, String dni, Tematica tem) {
        super(nombre, apellido, dni); //invocando al constructor del padre (Persona)
        this.tematica = tem;
    }

    //comportamiento
    public void corregir() {

    }
}
