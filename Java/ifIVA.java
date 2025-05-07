import java.util.Scanner;

public class ifIVA {
    
    public static double iva(double x) {
        if (x >= 1500 && x <= 2000) {
            return (x * 0.02) + x;
        } else if (x > 2000) {
            return (x * 0.05) + x;
        } else if (x < 1500) {
            return (x * 0.01) + x;
        }
        return 0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double val1 = 0;
        boolean validInput = false;
        while (!validInput) {
            System.out.println("Ingresa la cantidad: ");
            try {
                val1 = sc.nextDouble(); 
                validInput = true;  
            } catch (Exception e) {
            
                System.out.println("Por favor, ingresa un valor numérico válido.");
                sc.nextLine();  
            }
        }
        
        double tot = iva(val1); 
        System.out.println("Cantidad con IVA: " + tot);
        sc.close();
    }
}
