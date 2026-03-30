import mysql.connector
from websockets.extensions import ClientExtensionFactory

from gestionale.core.cliente import ClienteRecord
from gestionale.core.prodotto import ProdottoRecord
from gestionale.DAO.dbConnect import DBConnect

#di dafault i metodi del DAO sono static --> posso chiamare i metodi senza chiamare un'istanza del DAO

class DAO:
    @staticmethod
    def getAllProdotti():
        #creo una connessione fisica con il database --> può fallire, va messa in un try-except
        cnx=mysql.connector.connect(host="127.0.0.1",user="root",password="root",database="sw_gestionale")

        cursor=cnx.cursor(dictionary=True) #scorre il risultato delle query
        cursor.execute("select * from sw_gestionale.prodotti where prezzo > 20") #scrivo su DBeaver e quando funziona faccio copia e incolla
        #quando faccio una query che legge dei dati devo sempre usarli, altrimenti mi dà errore!
        row=cursor.fetchall() #salvo i prodotti in prodotti (lista di dizionari)

        res=[]
        for p in row:
            res.append(ProdottoRecord(p["nome"], p["prezzo"])) #nomi del databse

        cursor.close()
        cnx.close()
        return res

    #metodo che scrive nel database
    @staticmethod
    def addProdotto(prodotto):
        cnx=mysql.connector.connect(user="root",password="root",host="127.0.0.1",database="sw_gestionale")
        cursor=cnx.cursor()
        query="""insert into prodotti
                (nome, prezzo) values (%s, %s)"""

        cursor.execute(query, (prodotto.name, prodotto.price)) #query, tupla
        cnx.commit() #si fa quando scrivo
        cursor.close()
        cnx.close()
        return

    @staticmethod
    def getAllClienti():
        # creo una connessione fisica con il database --> può fallire, va messa in un try-except
        cnx = mysql.connector.connect(host="127.0.0.1", user="root", password="root", database="sw_gestionale")
        cursor = cnx.cursor(dictionary=True)  # scorre il risultato delle query
        cursor.execute(
            "select * from sw_gestionale.clienti")  # scrivo su DBeaver e quando funziona faccio copia e incolla
        # quando faccio una query che legge dei dati devo sempre usarli, altrimenti mi dà errore!
        row = cursor.fetchall()  # salvo i prodotti in prodotti (lista di dizionari)

        res = []
        for p in row:
            res.append(ClienteRecord(p["nome"], p["mail"], p["categoria"]))  # nomi del databse

        cursor.close()
        cnx.close()
        return res

    # metodo che scrive nel database
    @staticmethod
    def addCliente(cliente):
        cnx = mysql.connector.connect(user="root", password="root", host="127.0.0.1", database="sw_gestionale")
        cursor = cnx.cursor()
        query = """insert into clienti
            (nome, mail, categoria) values (%s, %s, %s)"""

        cursor.execute(query, (cliente.name, cliente.mail, cliente.categoria)) #(query, tupla)
        cnx.commit()  # si fa quando scrivo
        cursor.close()
        cnx.close()
        return

    def hasCliente(self, cliente): #restituisce True se il cliente esiste, altrimenti False
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from clienti where mail = %s" #selezioni i clienti con la mail cercata (chiave primaria)
        cursor.execute(query, (cliente.mail,))
        row = cursor.fetchall() #se ho una riga con quella mail, il cliente è già registrato

        cursor.close()
        cnx.close()
        return len(row) > 0 #ritorno True se quel cliente esiste già

    def hasProdotto(self, prod):
        # cnx = mysql.connector.connect(
        #     user = "root",
        #     password = "rootroot",
        #     host = "127.0.0.1",
        #     database = "sw_gestionale"
        # )
        cnx = DBConnect.getConnection()

        cursor = cnx.cursor(dictionary=True)
        query = "Select * from prodotti where nome = %s"
        cursor.execute(query, (prod.name,))
        row = cursor.fetchall()

        cursor.close()
        cnx.close()
        return len(row) > 0

#per testare:
if __name__ == "__main__":
    mydao=DAO()
    prodotti=mydao.getAllProdotti()

    print(prodotti)  # prova 1
    for p in prodotti:  # prova 2
        print(p)

