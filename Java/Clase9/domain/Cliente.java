package Clase9.domain;
import java.util.Date;

public class Cliente extends Persona {
    private int idCliente;
    private static int contadorCliente;
    private Date fechaRegistro;
    private boolean vip;
    
    public Cliente (String nombre , Date fechaRegistro , boolean vip){
        super(nombre);
        this.idCliente = ++contadorCliente;
        this.fechaRegistro = fechaRegistro;
        this.vip=vip;
    }

    public Date getFechaRegistro() {
        return this.fechaRegistro;
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

    public int getIdCliente() {
        return this.idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

}