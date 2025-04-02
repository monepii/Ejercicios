import java.util.Scanner;


    
    public static double iva (double x){
        if (x >= 1500 && x <=2000){
          return (x * .02) + x;
       } 
       else if (x > 2000){
           return (x * .05) + x;
       }
       else if (x < 1500){
            return (x * .01) + x;
       }
       return 0;
}

 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Ingresa la cantidad: ");
        double val1 = sc.nextDouble();
        
       double tot= iva (val1); 
       
           System.out.println("Cantidad con IVA: " + tot);
           sc.close();
    
}

