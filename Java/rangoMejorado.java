import java.util.Scanner;

public class rangoMejorado {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresa un número:");

        String input = sc.nextLine();

        try {
            double val1 = Double.parseDouble(input);

            if (val1 >= 0 && val1 <= 10) {
                System.out.println("El valor está entre 0 y 10");
            } else if (val1 >= 11 && val1 <= 20) {
                System.out.println("El valor está entre 11 y 20");
            } else if (val1 >= 21 && val1 <= 30) {
                System.out.println("El valor está entre 21 y 30");
            } else {
                System.out.println("El valor está fuera del rango");
            }

        } catch (NumberFormatException e) {
            System.out.println("Entrada inválida: no es un número.");
        }

        sc.close();
    }
}
