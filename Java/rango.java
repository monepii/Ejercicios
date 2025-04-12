import java.util.Scanner;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresa un numoro: ");
        int val1 = sc.nextInt();
        
        if (val1>=0 && val1<=10){
            System.out.println("El valor esta entre 0 y 10");
        } else {
            System.out.println("El valor esta fuera del rango de 0 y 10");
        }
        sc.close();
    }
