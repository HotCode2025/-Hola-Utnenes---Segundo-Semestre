package Clase8.TareaHerenciaUml.domain;

import java.util.Date;

public class Clientee extends Personaa {
    private int idCliente;
    private Date fechaRegistro;
    private boolean vip;

    public Clientee(String nombre, char genero, int edad, String direccion, int idCliente, Date fechaRegistro, boolean vip) {
        super(nombre, genero, edad, direccion);
        this.idCliente = idCliente;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public Date getFechaRegistro() {
        return fechaRegistro;
    }

    public void setFechaRegistro(Date fechaRegistro) {
        this.fechaRegistro = fechaRegistro;
    }

    public boolean isVip() {
        return vip;
    }

    public void setVip(boolean vip) {
        this.vip = vip;
    }
}
