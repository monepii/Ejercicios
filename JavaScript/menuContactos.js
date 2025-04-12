let contacts = [
    {
      name: "Maxwell Wright",
      phone: "(0191) 719 6495",
      email: "Curabitur.egestas.nunc@nonummyac.co.uk"
    },
    {
      name: "Raja Villarreal",
      phone: "0866 398 2895",
      email: "posuere.vulputate@sed.com"
    },
    {
      name: "Helen Richards",
      phone: "0800 1111",
      email: "libero@convallis.edu"
    }
  ];
  
  let opc;
  
  do {
    opc = Number(prompt(
      "Elige una opción:\n" +
      "1. Agregar contacto\n" +
      "2. Ver primer contacto\n" +
      "3. Ver último contacto\n" +
      "0. Salir"
    ));
  
    switch (opc) {
      case 1:
        let nombre = prompt("Ingresa el nombre:");
        let tel = prompt("Ingresa número de teléfono:");
        let mail = prompt("Ingresa correo electrónico:");
  
        if (nombre && tel && mail) {
          contacts.push({
            name: nombre,
            phone: tel,
            email: mail
          });
          alert("Contacto agregado con éxito");
        } else {
          alert("Revisa que estén ingresados todos los datos solicitados");
        }
        break;
  
      case 2:
        alert(
          contacts[0].name + ", " +
          contacts[0].phone + ", " +
          contacts[0].email
        );
        break;
  
      case 3:
        let ultimo = contacts[contacts.length - 1];
        alert(
          ultimo.name + ", " +
          ultimo.phone + ", " +
          ultimo.email
        );
        break;
  
      case 0:
        alert("Fin");
        break;
  
      default:
        alert("Opción no válida. Intenta de nuevo.");
        break;
    }
  
  } while (opc !== 0);
  