import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class asignaturas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<String> asignaturas = new ArrayList<>();

        System.out.println("Ingresa 10 asignaturas:");

        for (int i = 0; i < 10; i++) {
            System.out.print("Asignatura " + (i + 1) + ": ");
            String asignatura = sc.nextLine().trim();

            if (asignatura.isEmpty()) {
                System.out.println("La asignatura no puede estar vacía. Intenta de nuevo.");
                i--;
            } else {
                asignaturas.add(asignatura);
            }
        }

        System.out.println("\nAsignaturas de la posición 3 a la 6:");
        for (int i = 2; i < 6; i++) {
            System.out.println(asignaturas.get(i));
        }

        System.out.println("\nLista completa de asignaturas:");
        System.out.println(asignaturas);

        sc.close();
    }
}
