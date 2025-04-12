let no1 = Number(prompt("Ingresa un numero: "));
let no2 = Number(prompt("Ingresa otro numero: "));

let op = prompt("Escribe lo que deesees (+, -, * o /): ", 0);

let resultado;

if (!Number.isNaN(no1) && !Number.isNaN(no2)){
    switch(op){
        case "+": resulado = no1 + no2;
        break

        case "-": resulado = no1 - no2;
        break

        case "*": resulado = no1 * no2;
        break

        case "/": resulado = no1 / no2;
        break
        
    }
}else{
    resultado = "Error: Revisa que los valores sean numeros."
}
alert(resultado)