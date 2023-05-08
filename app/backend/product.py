from backend.connexion import Connexion
class Product:
    def __init__(self, db):
        self.db = db
        self.db.connect()

    def add(self, id_user, product_name, product_description, product_price, product_quantity, alert_threshold, last_entry_date, last_exit_date):
        query = "INSERT INTO product (id_user,product_name, product_description, product_price, product_quantity, alert_threshold, last_entry_date, last_exit_date) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
        values = ( id_user,product_name, product_description, product_price, product_quantity, alert_threshold, last_entry_date, last_exit_date)
        self.db.execute_query(query, values)
        return True

    def update(self, id_product,product_name, product_description, product_price, product_quantity, alert_threshold, last_entry_date, last_exit_date):
        query = "UPDATE product SET product_name=%s, product_description=%s, product_price=%s, product_quantity=%s, alert_threshold=%s, last_entry_date=%s, last_exit_date=%s WHERE id_product=%s"
        values = ( product_name, product_description, product_price, product_quantity, alert_threshold, last_entry_date, last_exit_date, id_product)
        self.db.execute_query(query, values)
        return True


    def delete(self, id_product):
        query = "DELETE FROM product WHERE id_product=%s"
        values = (id_product,)
        self.db.execute_query(query, values)
        return True


    def display(self):
        query = "SELECT product.id_product,admin.username, product.product_name,product.product_description,product.product_price,product.product_quantity,product.alert_threshold,product.last_entry_date,product.last_exit_date FROM product JOIN admin ON product.id_user = admin.id_user; "
        self.db.execute_query(query)
        result = self.db.fetch_all()
        return result
    

    