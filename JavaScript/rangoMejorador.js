let a; 

do {
    try {
        a = parseFloat(prompt("Ingresa un número entre 0 y 30: "));
        
        if (isNaN(a)) {
            throw new Error("El valor ingresado no es un número válido.");
        }
        
        else if (a >= 0 && a <= 10) {
            console.log("El número está dentro de 0 y 10");
            break;
        }
        else if (a >= 11 && a <= 20) {
            console.log("El número está dentro de 11 y 20");
            break;
        } 
        else if (a >= 21 && a <= 30) {
            console.log("El número está dentro de 21 y 30");
            break;
        } 
        
        else {
            console.log("El valor está fuera de los rangos");
        }
    } catch (error) {
        console.log(error.message);
    }
} while (true);