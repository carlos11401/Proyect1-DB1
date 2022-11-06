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

        query = "SELECT id_cliente, Nombre, Apellido, name_country, SUM(price_product) AS Total FROM db_proyect1.client\n"
        query += "INNER JOIN db_proyect1.order ON db_proyect1.order.idClient_order = db_proyect1.client.id_cliente\n"
        query += "INNER JOIN db_proyect1.product ON db_proyect1.product.id_product = db_proyect1.order.idProduct_order\n"
        query += "INNER JOIN db_proyect1.country ON db_proyect1.client.id_pais = db_proyect1.country.id_country\n"
        query += "GROUP BY id_cliente\n"
        query += "ORDER BY Total DESC\n"
        query += "LIMIT 1;"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print(" - Done.")
            return self.funcs.convertTo_JSON_1consult(records)

        except Exception as e:
            print("Error:", e)
            return -1

    def get_moreAndLessPurchasedProducts(self):
        print(" - Executing consult...")

        query = "SELECT idProduct_order, name_product, cat_name, Amount, Amount * price_product AS Total  FROM(\n"
        query += "SELECT idProduct_order, Amount  FROM(\n"
        query += "SELECT idProduct_order, SUM(amount_order) AS Amount\n"
        query += "FROM db_proyect1.order\n"
        query += "GROUP BY 1\n"
        query += ") Consult\n"
        query += ") Res1\n"
        query += "INNER JOIN(\n" 
        query += "SELECT Id, MAX(Amount2) AS MaxAmount, MIN(Amount2) AS MinAmount FROM(\n"
        query += "SELECT Id, Amount2  FROM(\n"
        query += "SELECT idProduct_order AS Id, SUM(amount_order) AS Amount2\n"
        query += "FROM db_proyect1.order\n"
        query += "GROUP BY idProduct_order\n"
        query += ") Consult\n"
        query += ")Total\n"
        query += ") Res2 ON Res2.MaxAmount = Res1.Amount OR Res2.MinAmount = Res1.Amount\n"
        query += "INNER JOIN  db_proyect1.product ON idProduct_order = db_proyect1.product.id_product\n"
        query += "INNER JOIN  db_proyect1.category ON id_category_product = db_proyect1.category.id\n"
        query += "ORDER BY Amount DESC;\n"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            maxAndMinAmounts = records[:1] + records[len(records)-1:]
            print(" - Done.")
            return self.funcs.convertTo_JSON_2consult(maxAndMinAmounts)

        except Exception as e:
            print("Error:", e)
            return -1
    
    def get_sellerWithMoreSales(self):
        print(" - Executing consult...")

        query = "SELECT idSeller_order, name_seller, SUM(price_product*amount_order) AS Sales FROM db_proyect1.order AS orderT\n"
        query += "INNER JOIN product ON product.id_product = orderT.idProduct_order\n"
        query += "INNER JOIN seller ON id_seller = orderT.idSeller_order\n"
        query += "GROUP BY idSeller_order\n"
        query += "ORDER BY Sales DESC\n"
        query += "LIMIT 1;"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print(" - Done.")
            return self.funcs.convertTo_JSON_3consult(records)

        except Exception as e:
            print("Error:", e)
            return -1