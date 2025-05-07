import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class agenda {
    public static void main(String[] args) {
        // Mapa original con nombres formateados correctamente
        Map<String, String> agendaOriginal = new HashMap<>();
        agendaOriginal.put("Juan", "5519204347");
        agendaOriginal.put("Kevin", "5582938847");
        agendaOriginal.put("Laura", "5592059112");
        agendaOriginal.put("Emmanuel", "5592009889");

        Map<String, String> agenda = new HashMap<>();
        for (Map.Entry<String, String> entry : agendaOriginal.entrySet()) {
            agenda.put(entry.getKey().toLowerCase(), entry.getValue());
        }

        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el nombre de la persona: ");
        String nombre = sc.nextLine().toLowerCase(); 

        if (agenda.containsKey(nombre)) {
    
            for (String key : agendaOriginal.keySet()) {
                if (key.equalsIgnoreCase(nombre)) {
                    System.out.println("El número de " + key + " es: " + agenda.get(nombre));
                    break;
                }
            }
        } else {
            System.out.println("No se encontró ningún número telefónico para ese nombre.");
        }

        sc.close();
    }
}
