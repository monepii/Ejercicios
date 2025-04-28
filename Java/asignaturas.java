import java.util.ArrayList;
import java.util.List;


    public static void main(String[] args) {
        
        List<String> asignaturas = new ArrayList<>();
        asignaturas.add("Matemáticas");
        asignaturas.add("Física");
        asignaturas.add("Química");
        asignaturas.add("Historia");
        asignaturas.add("Geografía");
        asignaturas.add("Español");
        asignaturas.add("Inglés");
        asignaturas.add("Biología");
        asignaturas.add("Educación Física");
        asignaturas.add("Programacion");

        
        System.out.println("Asignaturas de la posición 3 a la 6:");
        for (int i = 2; i < 6; i++) {
            System.out.println(asignaturas.get(i));
        }

    
        System.out.println("\nLista completa de asignaturas:");
        System.out.println(asignaturas);
    }

