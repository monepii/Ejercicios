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
    
    
    contacts[3] = {
      name: "Maisie Haley",
      phone: "0913 531 3030",
      email: "risus.Quisque@urna.ca"
    };
    
    console.log(contacts[0].name +", "+contacts[0].phone +", "+ contacts[0].email);
    console.log(contacts[1].name +", "+contacts[1].phone +", "+ contacts[1].email);
    console.log(contacts[2].name +", "+contacts[2].phone +", "+ contacts[2].email);
    console.log(contacts[3].name +", "+contacts[3].phone +", "+ contacts[3].email);
    
    console.log(contacts.length)