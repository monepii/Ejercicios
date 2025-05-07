import java.util.Scanner;
public class precioIVAentrada{
public static double iva (double x){
    return (x * .16) + x;
}
 
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        System.out.println("Ingresa la cantidad: ");
        double val1 = sc.nextDouble();
        
       double tot= iva (val1);
        System.out.println("Cantidad con IVA: " + tot);
        sc.close();
    } 
}