import java.util.Scanner;

public class rango {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresa un número:");

        String input = sc.nextLine();
        try {
            double val1 = Double.parseDouble(input);
            if (val1 >= 0 && val1 <= 10) {
                System.out.println("El valor está entre 0 y 10");
            } else {
                System.out.println("El valor está fuera del rango de 0 y 10");
            }
        } catch (NumberFormatException e) {
            System.out.println("Entrada inválida: no es un número.");
        }

        sc.close();
    }
}
