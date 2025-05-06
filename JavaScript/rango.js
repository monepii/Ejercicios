let a;

do {
    try {
        a = parseFloat(prompt("Ingresa un número entre 0 y 10: "));
        
        if (isNaN(a)) {
            throw new Error("El valor ingresado no es un número válido.");
        }
        
        if (a >= 0 && a <= 10) {
            console.log("El número está dentro del rango");
            break;
        } else {
            console.log("El valor está fuera del rango");
        }
    } catch (error) {
        console.log(error.message);
    }
} while (true);
