from backend.connexion import Connexion

class User():
    def __init__(self,db):
        self.db = db
        self.db.connect()

    def displayUser(self):
        query = "SELECT id_user,username FROM admin"
        self.db.execute_query(query)
        result = self.db.fetch_all()
        return result
    
    def addUser(self,user,password):
        query = "INSERT INTO admin (username, password) VALUES ( %s, %s)"
        values =(user,password)
        self.db.execute_query(query, values)
        return True

    def deleteUser(self,id):
        query = "DELETE FROM admin WHERE id_user = %s"
        values = (id,)
        self.db.execute_query(query,values)
        return True

    def updateUser(self,new_user,new_password ,id):
        query ="UPDATE admin SET username = %s ,password = %s  WHERE id_user = %s"
        values =(new_user,new_password ,id)
        self.db.execute_query(query, values)
        return True
    
    def checkUsername(self,username):
            query_check = "SELECT * FROM admin Where username = %s"
            params = (username,)
            self.db.execute_query(query_check,params)
            resultat = self.db.fetch_all()
            return resultat
    
    def ckeckUserExsist(self,username,password):
            # query for select username & password from admin table
            query = "SELECT * FROM admin WHERE username = %s and password = %s"
            # exuxte the query
            self.db.execute_query(query,(username,password))
            # return the data in list
            resultat = self.db.fetch_all()
            return resultat


