let contacts = [{
    name: "Maxwell Wright",
    phone: "(0191) 719 6495",
    email: "Curabitur.egestas.nunc@nonummyac.co.uk"
    }, {
    name: "Raja Villarreal",
    phone: "0866 398 2895",
    email: "posuere.vulputate@sed.com"
    }, {
    name: "Helen Richards",
    phone: "0800 1111",
    email: "libero@convallis.edu"
    }];
    
    // write your code here
    
    let nombre = prompt("Ingresa el nombre: ", 0);
    let tel = prompt("Ingresa tu numero de telefono:", 0);
    let mail = prompt("Ingresa tu correo electronico: ", 0);

    
    contacts[3] = {
        name: nombre,
        phone: tel,
        email: mail
    };

    
    let last = contacts.length - 1;
    
    console.log(`${contacts[0].name} / ${contacts[0].phone} / ${contacts[0].email}`);
    console.log(`${contacts[last].name} / ${contacts[last].phone} / ${contacts[last].email}`);
