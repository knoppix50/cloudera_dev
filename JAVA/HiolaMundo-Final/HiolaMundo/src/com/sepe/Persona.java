package com.sepe;

public class Persona extends Object{

    private String nombre;
    //atributos: apellido, dni
    private String apellido;
    private String dni;

    public String getApellido() {
        return apellido;
    }

    public String getDni() {
        return dni;
    }



    public String getNombre() {
        return nombre;
    }

    public Persona(String nombre, String apellido, String dni) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.dni = dni;
    }

    //comportamiento
    protected void saludar() {
        System.out.println("Buenos dias!!");
    }

    @Override
    public String toString() {
        return "Persona{" +
                "nombre='" + nombre + '\'' +
                ", apellido='" + apellido + '\'' +
                ", dni='" + dni + '\'' +
                '}';
    }
}
