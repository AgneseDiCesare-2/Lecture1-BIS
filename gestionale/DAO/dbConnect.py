import pathlib

import mysql.connector
#questa classe permette di automatizzare l'apertura della connessione,
#così non devo scriverla ogni volta.

class DBConnect:
    _myPool=None #attributo della classe --> posso chiamarla in ogni momento dalla classe

    def __int__(self):
        #per implementare il patter singletone e impedire all'utente di creare istanze di classe
        raise RuntimeError("Non devi creare un'istanza di questa classe! Usa i metodi di classe")

    @classmethod
    def getConnection(cls):
        if cls._myPool is None:  #verifico se la connessione esiste
            try:
               # cnx = mysql.connector.connect(
                #    user = "root",
                #    password = "root",
                 #   host = "127.0.0.1",
                  #  database = "sw_gestionale"
                #)
               # implementiamo il connection pooling
                cls._myPool = mysql.connector.pooling.MySQLConnectionPool(pool_size=3, pool_name="myPool", option_files=f"{pathlib.Path(__file__).resolve().parent}/connector.cfg")
                return cls._myPool.get_connection()

            except mysql.connector.Error as err:
                print("Non riesco a collegarmi al db")
                print(err)
                return None

        #se la connessione esiste già
        else:
            return cls._myPool.get_connection()



