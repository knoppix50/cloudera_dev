package com.sepe.admision;

import com.sepe.Alumno;

public class ControlAdmision {

    private static  boolean cumplirRequisitosPrevios(Alumno al) {
        /*
        if (al.getNotaFinal() > 6.5) {
            return true;
        } else {
            return false;
        }
        */
        //obtener expediente academico para calcular la media
        float[] expediente = al.getExpedienteAcademico();
        float mediaExpediente = 0.0f;
        float sumatorio = 0.0f;
        for (int i = 0; i < expediente.length; i++) {
            sumatorio += expediente[i];
        }
        mediaExpediente = sumatorio / expediente.length;

        return (mediaExpediente > 6.5);
    }

    private static  boolean examenSuperado() {
        int nota = (int)(Math.random() * 11);
        return (nota >= 7);
    }
    public static boolean esAdmitido(Alumno al) {
           return cumplirRequisitosPrevios(al) && examenSuperado();
    }

}
