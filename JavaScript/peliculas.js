let peliculas = [];

let continuar = true;

do {
  let nom = prompt("Ingresa el nombre de la película:");
  let cal = Number.parseFloat(prompt("Ingresa la calificación:"));

  if (nom && cal) {
    peliculas.push({
      nombre: nom,
      calificacion: cal,
    });
    alert("Película agregada con éxito");
  } else {
    alert("Revisa que estén ingresados todos los datos solicitados");
  }

  continuar = confirm("¿Deseas agregar otra película?");
} while (continuar);

for (let pelicula of peliculas) {
    if (pelicula.calificacion < 7) {
        console.log(pelicula);
    }
}

for (let pelicula of peliculas) {
    if (pelicula.calificacion >= 7) {
        console.log(pelicula.nombre +"("+pelicula.calificacion+")");
    }
}