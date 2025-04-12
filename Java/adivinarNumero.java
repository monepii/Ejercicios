import java.util.Scanner;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
    
        int val1;
        int numero = (int)(Math.random()*100+1);
        int cont = 0;
        System.out.println("JUEGO DE ADIVINAR LOS NUMEROS");
        System.out.println(" " + numero);
       do{
            
            System.out.println("Ingresa la cantidad: ");
            val1 = sc.nextInt();
            cont = cont+1;
            if (val1 <numero)
            {
                System.out.println("El numero es mayor");
            } else if(val1 >numero){
                System.out.println("El numero es menor");
            } 
       }
       while(val1 != numero);
       System.out.println("LO LOGRASTE!");
        System.out.println("Número de intentos: " + cont);
        sc.close();
    } 

 