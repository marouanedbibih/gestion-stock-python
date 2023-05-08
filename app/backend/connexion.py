import mysql.connector as msc

# Class MySqlDataBase pour connecter au MySql Base de donnee
class Connexion:

    # Function inisialiser base de donnee
    def __init__(self):
        self.host = "localhost"
        self.username = "root"
        self.password = ""
        self.database = "stock"
        self.port = 3306
        self.conn=None
        self.cursor=None

    # Function Connexion au base de donnee
    def connect(self):
        try:
            self.connection = msc.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
                port = self.port
            )
            print("Connexion in your database success")
        except msc.Error as er:
            print(er)
        self.cursor = self.connection.cursor()
    
    # Function pour fermer base de donnee
    def close(self):
        if self.connection is not None:
            self.connection.close()

    # Function pour executer des requetes SQL
    def execute_query(self, query, params=None):
        if self.cursor is None:
            self.connect()
        self.cursor.execute(query, params)
    
    # Function pour recuperer resultat de execute_query
    def fetch_all(self):
        if self.cursor is None:
            self.connect()
        return self.cursor.fetchall()

    

