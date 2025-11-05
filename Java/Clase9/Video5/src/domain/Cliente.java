package domain;

import java.util.Date;

public class Cliente extends Persona {

    // Atributos
    private int idCliente;
    private Date fechaRegistro;
    private boolean vip; // Very Important Person
    private static int contadorClientes; // autoincremental

    // Constructor (mismo orden que en el video: fecha, vip, y luego datos Persona)
    public Cliente(Date fechaRegistro, boolean vip,
                   String nombre, char genero, int edad, String direccion) {
        super(nombre, genero, edad, direccion);
        this.idCliente = ++Cliente.contadorClientes;
        this.fechaRegistro = fechaRegistro;
        this.vip = vip;
    }

    // Getters / Setters
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

    // toString sobrescrito
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Cliente{idCliente=").append(idCliente);
        sb.append(", fechaRegistro=").append(fechaRegistro);
        sb.append(", vip=").append(vip);
        sb.append(", ").append(super.toString());
        sb.append('}');
        return sb.toString();
    }
}
