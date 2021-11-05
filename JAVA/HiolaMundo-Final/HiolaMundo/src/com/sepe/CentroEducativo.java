package com.sepe;

import com.sepe.admision.ControlAdmision;

import java.util.List;

public class CentroEducativo {
    //atributos (privados)
    private String nombre;
    private TipoCentro tipo;
    private Aula[] aulario;

    public String getNombre() {
        return nombre;
    }

    public TipoCentro getTipo() {
        return tipo;
    }

    public CentroEducativo(String nombre, TipoCentro tipo) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.aulario = new Aula[]{
                    new Aula(Tematica.BIG_DATA),
                    new Aula(), //tematica Python por defecto
                    new Aula(Tematica.CIENCIA_DATOS)
                    };

    }

    public CentroEducativo(String nombre) {
        /*
        this.nombre = nombre;
        this.tipo = 0;
        */
        this(nombre, TipoCentro.GENERALISTA);
    }

    //comportamiento
    public boolean admitirAlumno(Alumno al) {
        //1.- cumpla requisitos academicos previos
        //2.- hacer una prueba de nivel (test)
        //3.- En funcion de la nota (0..100), pasa o no (score es 70)

        return ControlAdmision.esAdmitido(al);
    }

    public void asignarAlumno(Alumno al) {
        //asignar el alumno 'al' una admitido a un aula especfica
        al.crearAsignaturas();
        Aula aula = obtenerAulaPorTematica(al.getTematicaEstudio());
        if (aula != null) {
            aula.anyadirAlumno(al);
        }

    }

    //metodos privados
    private Aula obtenerAulaPorTematica(Tematica tem) {
        Aula aulaBuscada = null;

        for (Aula a: this.aulario) {
            if (a.getTematica() == tem) {
                aulaBuscada = a;
                break;
            }
        }

        return aulaBuscada;
    }
}
