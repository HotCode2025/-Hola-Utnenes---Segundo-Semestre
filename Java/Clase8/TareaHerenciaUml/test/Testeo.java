package Clase8.TareaHerenciaUml.test;

import Clase8.TareaHerenciaUml.domain.Personaa;
import Clase8.TareaHerenciaUml.domain.Empleadoo;
import Clase8.TareaHerenciaUml.domain.Clientee;
import java.util.Date;

public class Testeo {
    public static void main(String[] args) {
        // Test Persona
        Personaa persona = new Personaa("Oto", 'M', 25, "Mendoza");
        System.out.println("Nombre: " + persona.getNombre());
        System.out.println("Dirección original: " + persona.getDireccion());
        persona.setDireccion("Buenos Aires");
        System.out.println("Dirección actualizada: " + persona.getDireccion());

        // Test Empleado
        Empleadoo empleado = new Empleadoo("Ana", 'F', 30, "Córdoba", 101, 55000.0);
        System.out.println("\nEmpleado: " + empleado.getNombre());
        System.out.println("ID: " + empleado.getIdEmpleado());
        System.out.println("Sueldo original: " + empleado.getSueldo());
        empleado.setSueldo(60000.0);
        System.out.println("Sueldo actualizado: " + empleado.getSueldo());

        // Test Cliente
        Date fecha = new Date();
        Clientee cliente = new Clientee("Luis", 'M', 40, "Rosario", 202, fecha, true);
        System.out.println("\nCliente: " + cliente.getNombre());
        System.out.println("ID: " + cliente.getIdCliente());
        System.out.println("Fecha de registro: " + cliente.getFechaRegistro());
        System.out.println("¿Es VIP?: " + cliente.isVip());
        cliente.setVip(false);
        System.out.println("¿Es VIP ahora?: " + cliente.isVip());
    }
}