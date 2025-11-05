package test;

import domain.Empleado;
import domain.Cliente;
import java.util.Date;

public class TestHerencia {
    public static void main(String[] args) {

        // Prueba Empleado (como en el video 4)
        Empleado empleado1 = new Empleado("Ariel", 57000.0);
        System.out.println("empleado1 = " + empleado1);

        // Prueba Cliente (video 5)
        Cliente cliente1 = new Cliente(
                new Date(),           // fechaRegistro
                true,                 // vip
                "Bety",               // nombre
                'F',                  // genero
                32,                   // edad
                "9 de julio 1413"     // direccion
        );
        System.out.println("cliente1 = " + cliente1);
    }
}
