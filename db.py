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
        query += "GROUP BY idProduct_order\n"
        query += "ORDER BY Amount DESC\n"
        query += "LIMIT 1\n"
        query += ") MaxAmount\n"
        query += "UNION ALL\n"
        query += "SELECT idProduct_order, Amount  FROM(\n"
        query += "SELECT idProduct_order, SUM(amount_order) AS Amount\n"
        query += "FROM db_proyect1.order\n"
        query += "GROUP BY idProduct_order\n"
        query += "ORDER BY Amount ASC\n"
        query += "LIMIT 1\n"
        query += ") MixAmoun\n"
        query += ") Res\n"
        query += "INNER JOIN  db_proyect1.product ON idProduct_order = db_proyect1.product.id_product\n"
        query += "INNER JOIN  db_proyect1.category ON id_category_product = db_proyect1.category.id\n"
        query += "ORDER BY Amount DESC;\n"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            print(" - Done.")
            return self.funcs.convertTo_JSON_2consult(records)

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

    def get_contryWithMoreAndLessSales(self):
        print(" - Executing consult...")
        
        query = "SELECT nameC, Total FROM(\n"
        query += "SELECT name_country AS nameC, SUM(amount_order * price_product) AS Total\n"
        query += "FROM db_proyect1.order AS orderT\n"
        query += "INNER JOIN seller ON id_seller = orderT.idSeller_order\n"
        query += "INNER JOIN product ON id_product = idProduct_order\n"
        query += "INNER JOIN country ON id_country = id_country_seller\n"
        query += "GROUP BY name_country\n"
        query += "ORDER BY Total DESC\n"
        query += "LIMIT 1\n" 
        query += ") AS Max\n"
        query += "UNION ALL\n"
        query += "SELECT nameC, Total FROM(\n"
        query += "SELECT name_country AS nameC, SUM(amount_order * price_product) AS Total\n"
        query += "FROM db_proyect1.order AS orderT\n"
        query += "INNER JOIN seller ON id_seller = orderT.idSeller_order\n"
        query += "INNER JOIN product ON id_product = idProduct_order\n"
        query += "INNER JOIN country ON id_country = id_country_seller\n"
        query += "GROUP BY name_country\n"
        query += "ORDER BY Total ASC\n"
        query += "LIMIT 1\n" 
        query += ") AS Min;"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print(" - Done.")
            return self.funcs.convertTo_JSON_4consult(records)

        except Exception as e:
            print("Error:", e)
            return -1

    def get_topContriesWithMorePurchases(self):
        print(" - Executing consult...")

        query = "SELECT id_country ,name_country AS nameC, SUM(amount_order * price_product) AS Total\n" 
        query += "FROM db_proyect1.order AS orderT\n"
        query += "INNER JOIN seller ON id_seller = orderT.idSeller_order\n"
        query += "INNER JOIN product ON id_product = idProduct_order\n"
        query += "INNER JOIN country ON id_country = id_country_seller\n"
        query += "GROUP BY name_country\n"
        query += "ORDER BY Total ASC\n"
        query += "LIMIT 5;"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print(" - Done.")
            return self.funcs.convertTo_JSON_5consult(records)

        except Exception as e:
            print("Error:", e)
            return -1

    def get_categoryMoreAndLessAmounts(self):
        print(" - Executing consult...")

        query = "SELECT nameC, Total FROM(\n"
        query += "SELECT cat_name AS nameC, SUM(amount_order) AS Total\n"
        query += "FROM db_proyect1.order AS orderT\n"
        query += "INNER JOIN product ON id_product = idProduct_order\n"
        query += "INNER JOIN category ON category.id = id_category_product\n"
        query += "GROUP BY id_category_product\n"
        query += "ORDER BY Total DESC\n"
        query += "LIMIT 1\n"
        query += ") AS Max\n"
        query += "UNION ALL\n"
        query += "SELECT nameC, Total FROM(\n"
        query += "SELECT cat_name AS nameC, SUM(amount_order) AS Total \n"
        query += "FROM db_proyect1.order AS orderT\n"
        query += "INNER JOIN product ON id_product = idProduct_order\n"
        query += "INNER JOIN category ON category.id = id_category_product\n"
        query += "GROUP BY id_category_product\n"
        query += "ORDER BY Total ASC\n"
        query += "LIMIT 1\n" 
        query += ") AS Min;\n"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print(" - Done.")
            return self.funcs.convertTo_JSON_6consult(records)

        except Exception as e:
            print("Error:", e)
            return -1

    def get_categoryMorePurchasesByCountry(self):
        print(" - Executing consult...")

        query = "SELECT CountryName, CategoryName, Maxi FROM(\n"
        query += "SELECT CountryName, CategoryName, MAX(Amount) AS Maxi FROM(\n"
        query += "SELECT  name_country AS CountryName, cat_name AS CategoryName, SUM(amount_order) AS Amount\n" 
        query += "FROM client\n"
        query += "INNER JOIN db_proyect1.order ON id_cliente = idClient_order\n"
        query += "INNER JOIN country ON id_country = id_pais\n"
        query += "INNER JOIN product ON id_product = idProduct_order\n"
        query += "INNER JOIN category ON category.id = id_category_product\n"
        query += "GROUP BY id_country ,id_category_product\n"
        query += ") AS Sum\n"
        query += "GROUP BY CountryName\n"
        query += "ORDER BY CountryName\n"
        query += ")AS Res\n"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print(" - Done.")
            return self.funcs.convertTo_JSON_7consult(records)

        except Exception as e:
            print("Error:", e)
            return -1

    def get_englandPurchasesByMonth(self):
        print(" - Executing consult...")

        query = "SELECT DateOrder, Total\n"
        query += "FROM(\n"
        query += "SELECT name_country AS CountryName, MONTH(date_order) AS DateOrder, SUM(amount_order * price_product) AS Total\n" 
        query += "FROM db_proyect1.order\n"
        query += "INNER JOIN seller ON id_seller = idSeller_order\n"
        query += "INNER JOIN product ON id_product = idProduct_order\n"
        query += "INNER JOIN country ON id_country = id_country_seller\n"
        query += "GROUP BY id_country_seller, DateOrder\n"
        query += "ORDER BY DateOrder ASC\n"
        query += ") AS Res WHERE CountryName = \"Australia\";"

        try:
            self.cursor.execute(query)
            records = self.cursor.fetchall()

            print(" - Done.")
            return self.funcs.convertTo_JSON_8consult(records)

        except Exception as e:
            print("Error:", e)
            return -1