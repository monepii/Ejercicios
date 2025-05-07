import java.util.Scanner;

public class adivinarNumero {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int val1;
        int numero = (int)(Math.random() * 100 + 1); 
        int cont = 0;

        System.out.println("JUEGO DE ADIVINAR LOS NÚMEROS");
        do {
            System.out.print("Ingresa un número: ");
            while (!sc.hasNextInt()) {
                System.out.println("¡Por favor, ingresa un número válido!");
                sc.next(); 
                System.out.print("Ingresa un número: ");
            }
            val1 = sc.nextInt(); 
            cont++;

            if (val1 < numero) {
                System.out.println("El número es mayor");
            } else if (val1 > numero) {
                System.out.println("El número es menor");
            }
        } while (val1 != numero);

        System.out.println("¡LO LOGRASTE!");
        System.out.println("Número de intentos: " + cont);

        sc.close();
    }
}
