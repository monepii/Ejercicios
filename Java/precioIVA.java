public class precioIVA{
    public static void main(String[] args) {
        double val1 = 100;
        double iva = .21; 
        
        
        double tIva = val1 * iva; 
        double total = tIva + val1;
        
        System.out.println("Total de IVA: "+ tIva);
        System.out.println("Costo total: "+ total);
        
    }
}