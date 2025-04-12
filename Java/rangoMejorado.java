import java.util.Scanner;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Ingresa un numero: ");
        int val1 = sc.nextInt();
        
        if (val1>=0 && val1<=10){
            System.out.println("El valor esta entre 0 y 10");
        }
        else if (val1>=11 && val1<=20){
            System.out.println("El valor esta entre 11 y 20");
        }
        else if (val1>=21 && val1<=30){
            System.out.println("El valor esta entre 21 y 30");
        }else {
            System.out.println("El valor esta fuera del rango");
        }
        sc.close();
    }

