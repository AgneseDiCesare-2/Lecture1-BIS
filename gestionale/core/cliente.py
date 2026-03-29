from dataclasses import dataclass
#devo sempre avere una classe associata a ciò che leggo nel database
#funzioni minime da associare per ogni tabella

@dataclass
class ClienteRecord:
    nome: str
    mail: str
    categoria: str

    #è bene associare una funzione di hash --> due oggetti sono uguali se hanno la stessa chiave primaria
    def __hash__(self):
        return hash(self.mail) #mail=chiave primaria, se due istanze hanno la stessa mail sono lo stesso oggetto

    #e di eq
    def __eq__(self, other):
        return self.mail == other.mail

    #e di str
    def __str__(self):
        return f"{self.nome}--{self.mail} ({self.categoria})"