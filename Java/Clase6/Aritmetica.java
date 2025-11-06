

public class Aritmetica {
    int a;
    int b;

    public Aritmetica (){
        System.out.println("Se esta ejecutando este constructor numero uno");

}

public Aritmetica(int a, int b){
    this.a = a;
    this.b = b;
    System.out.println("Se esta ejecutando este constructor numero dos");

}

public void sumarNumeros(){
    int resultado = a + b;
    System.out.println("resultado = " + resultado);

}

public int sumarConRetorno(){
return a + b;
}

public int sumarConArgumentos(int a, int b){
    this.a = a;
    this.b = b;
    return this .sumarConRetorno();
}}

