import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class listas {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresa 10 valores (pueden ser palabras o frases) separados por comas: ");
        
        String cadena = sc.nextLine();
        String[] valores = cadena.split(",");

        if (valores.length != 10) {
            System.out.println("Asegúrate de ingresar exactamente 10 valores.");
        } else {
            List<String> lista = new ArrayList<>();
            for (String val : valores) {
                lista.add(val.trim()); 
            }

            System.out.println("Lista de valores: " + lista);
        }

        sc.close();
    }
}
