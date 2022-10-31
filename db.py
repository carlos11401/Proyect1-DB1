from funcs import Funcs
import pymysql

class DataBase:
    def __init__(self):
        self.funcs = Funcs()
        
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'cjcg2000',
            db = 'db_proyect1'
        )

        self.cursor = self.connection.cursor()
        print("  - Databse Connected")

    def get_customerWithMorePurchases(self):
        print(" - Executing consult...")

        query = "SELECT id_cliente, Nombre, Apellido, name_country, amount_order, price_product  FROM db_proyect1.client\n"
        query += "INNER JOIN db_proyect1.order ON db_proyect1.order.idClient_order = db_proyect1.client.id_cliente\n"
        query += "INNER JOIN db_proyect1.product ON db_proyect1.product.id_product = db_proyect1.order.idProduct_order\n"
        query += "INNER JOIN db_proyect1.country ON db_proyect1.client.id_pais = db_proyect1.country.id_country\n"
        query += "ORDER BY id_cliente;"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            idCustomer, totalPurchase = self.funcs.calculate_customerWithMorePuchases(records)
            customerWithMorePurchases = records[idCustomer] + (totalPurchase,)
            print(" - Done.")
            return self.funcs.convertTo_JSONCustomer(customerWithMorePurchases)

        except Exception as e:
            print("Error:", e)
            return -1