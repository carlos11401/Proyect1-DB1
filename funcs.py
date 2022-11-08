class Funcs:
    def __init__(self):
        pass

    def calculate_customerWithMorePuchases(self, records):
        id_biggesCustomer = -1
        higherTotalPrice = 0
        totalPrice = 0
        previousId = 0
        counter = 0
        for record in records:
            amount = record[4]
            idClient = record[0]
            priceProduct = record[5]
            if idClient == previousId or counter == 0:
                totalPrice += priceProduct * amount
            elif totalPrice > higherTotalPrice:
                id_biggesCustomer = idClient
                higherTotalPrice = totalPrice
                totalPrice = priceProduct * amount
            else:
                totalPrice = priceProduct * amount

            previousId = idClient
            counter += 1

        return id_biggesCustomer, higherTotalPrice

    def convertTo_JSON_1consult(self, tuple):
        customer = tuple[0]
        dict = {
            "Id": customer[0],
            "Name": customer[1],
            "Last Name": customer[2],
            "Country": customer[3],
            "Purchase": str(customer[4])
            }
        return dict

    def convertTo_JSON_2consult(self, records):
        maxRecord = records[0]
        minRecord = records[1]
        dict = {
                "MAX":{
                    "Id": maxRecord[0],
                    "Product": maxRecord[1],
                    "Category": maxRecord[2],
                    "Amount": str(maxRecord[3]),
                    "Total": str(maxRecord[4])
                },
                "MIN":{
                    "Id": minRecord[0],
                    "Product": minRecord[1],
                    "Category": minRecord[2],
                    "Amount": str(minRecord[3]),
                    "Total": str(minRecord[4])
                }
            }
        return dict

    def convertTo_JSON_3consult(self, tuple):
        seller = tuple[0]
        dict = {
            "Id": seller[0],
            "Name": seller[1],
            "Sales": str(seller[2])
            }
        return dict

    def convertTo_JSON_4consult(self, tuple):
        seller = tuple[0]
        dict = {
            "Country": seller[0],
            "Sales": str(seller[1])
            }
        return dict

    def convertTo_JSON_5consult(self, tuple):
        dict = {}
        counter = 0
        for country in tuple:
            strg = str(counter+1)
            aux = {
                    strg: {
                        "Id": country[0],
                        "Country": country[1],
                        "Purchase": str(country[2])
                    }
                }
            

            dict.update(aux)
            counter += 1

        return dict

    def convertTo_JSON_6consult(self, tuple):
        maxRecord = tuple[0]
        minRecord = tuple[1]
        dict = {
                "MAX":{
                    "Category": maxRecord[0],
                    "Amount": str(maxRecord[1]),
                },
                "MIN":{
                    "Category": minRecord[0],
                    "Amount": str(minRecord[1]),
                }
            }
        return dict

    def convertTo_JSON_7consult(self, tuple):
        dict = {}
        counter = 0
        for country in tuple:
            strg = str(counter+1)
            aux = {
                    strg: {
                        "Country": country[0],
                        "Category": country[1],
                        "Amount": str(country[2])
                    }
                }
            

            dict.update(aux)
            counter += 1

        return dict