import xmltodict

def teste():

    with open("xml/inventory.xml") as xml_file:
        products = xmltodict.parse(xml_file.read())
        xml_file.close()

    print(products)


teste()
