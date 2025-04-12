import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresa 10 valores separados por comas: ");
        
        String cadena = sc.nextLine();
        
        String[] valores = cadena.split(",");

        if (valores.length != 10) {
            System.out.println("Asegúrate de ingresar los 10 valores.");
        } else {
            List<Integer> lista = new ArrayList<>();
            for (String val : valores) {
                lista.add(Integer.parseInt(val.trim()));
            }

            System.out.println("Lista de valores: " + lista);
        }

        sc.close();
    }

