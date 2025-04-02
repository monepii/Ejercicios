import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


    public static void main(String[] args) {
        Map<String, String> agenda = new HashMap<>();
        agenda.put("Juan", "5519204347");
        agenda.put("Kevin", "5582938847");
        agenda.put("Laura", "5592059112");
        agenda.put("Emmanuel", "5592009889");

        
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el nombre de la persona: ");
        String nombre = sc.nextLine();

        
        if (agenda.containsKey(nombre)) {
            System.out.println("El numero de " +nombre+ " es: " + agenda.get(nombre));
        } else {
            System.out.println("No se encontro ningun numero telefónico de ");
        }

        sc.close();
    }
