from shop import Shop
import requests
from bs4 import BeautifulSoup
import json
from constant import *

class Product:
    def __init__(self, index, name, pictureLink, price, rating, status, location):
        self.index = index
        self.name = name
        self.pictureLink = pictureLink
        self.price = price
        self.rating = rating
        self.status = status
        self.location = location

    def __repr__(self):
        return f"Product(\n name:{self.name},\n picture link:{self.pictureLink},\n price:{self.price},\n rating:{self.rating},\n status:{self.status},\n location:{self.location}"
    
    def getJSONFormat(self):
         return {
             "name":self.name,
             "picture link":self.pictureLink,
             "price":self.price,
             "rating":self.rating,
             "status":self.status,
             "location":self.location
             }
    
    def isNone(self):
        if self.name == self.pictureLink == self.price == self.rating == self.status == self.location == None:
            return True

class OutputFormat:
    def __init__(self):
        self.OBJECT_FORMAT = "object"
        self.JSON_FORMAT = "json"

class ProductScrapping(Shop):
    def __init__(self, shopName, productName):
        super().__init__(shopName)
        self.productName = productName
    
    def __str__(self):
        return "Product object with property:" + self.printList([f"name = {self.name}", f"picture link = {self.pictureLink}", f"price = {self.price}", f"location = {self.location}"])
    
    def __repr__(self):
        return f"Product(name:{self.name}, picture link:{self.pictureLink}, price:{self.price}, location:{self.location}"

    # wrap "tag" and "class" in one tupple
    # return [("tag","class"),...,("tag","class")]
    def packetTagAndClass(self, items):
        return [(item["tag"], item["class"]) for item in items]
    
    def structure_section(self):
        return self.getDetail()["structure"][0]

    # structure <section>
    def collectionOfItem_packet(self):
        """get "collectionOfItem" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["collectionOfItem"])

    def eachItem_packet(self):
        """get "eachItem" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["eachItem"])

    # product <section>
    def picture_packet(self):
        """get "picture" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["product"]["picture"])
    def overview_packet(self):
        """get "overview" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["product"]["overview"])
    def name_packet(self):
        """get "name" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["product"]["name"])
    def price_packet(self):
        """get "price" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["product"]["price"])
    def rating_packet(self):
        """get "rating" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["product"]["rating"])
    def status_packet(self):
        """get "status" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["product"]["status"])
    def location_packet(self):
        """get "location" <packet of data>"""
        return self.packetTagAndClass(self.structure_section()["product"]["location"])
    # product </section>

    # structure </section>
    
    def getContent(self, content=None, numberOfProduct=10, outputFormat = "object"):
        self.setSoup()
        eachItem = self.soup.findAll(class_ = self.eachItem_packet()[0][1])[:numberOfProduct]
        self.numberOfProduct = len(eachItem)
        items = []
        for index, item in enumerate(eachItem):                                                                                                                                                                                                
            rating = item.find(class_=self.rating_packet()[0][1])
            if item.find(class_=self.status_packet()[0][1]) is not None:
                status = (item.find(class_=self.status_packet()[0][1])).findAll("p")
                if len(status) < 1:
                    status = None
                elif len(status) == 1:
                    status = status[0].get_text().strip()
                elif len(status) == 2:
                    status = status[1].get_text().strip()
            else:
                status = None
            product = Product(
                    index,
                    item.find(class_=self.name_packet()[0][1]).get_text().strip() if item.find(class_=self.name_packet()[0][1]) is not None else None,
                    item.find("img")['src'] if item.find("img") is not None else None,
                    item.find(class_=self.price_packet()[0][1]).get_text().strip() if item.find(class_=self.price_packet()[0][1]) is not None else None,
                    rating.get_text().strip() if rating is not None else None,
                    status,
                    item.find(class_=self.location_packet()[0][1]).get_text().strip() if item.find(class_=self.location_packet()[0][1]) is not None else None,
                )
            if product.isNone():
                continue
            if outputFormat == "object":
                items.append(product)
            elif outputFormat == "json":
                items.append(vars(product)
            )
        return (self.numberOfProduct, items)
    def setSoup(self):
        self.page = requests.get(self.getLinkFormat(self.productName))
        self.soup = BeautifulSoup(self.page.content, 'html.parser')

if __name__ == "__main__":

    productscrapping = ProductScrapping("Bukalapak", "Samsung A23")
    with open(OUTPUT_FILE, "w") as of:
        totalProductSearch, items = productscrapping.getContent(numberOfProduct = 100, outputFormat="json")
        # print(items.getJSONFormat())
        totalItems = len(items)
        json.dump({"total product search" : totalProductSearch, "total items" : totalItems, "total items with null values" : totalProductSearch - totalItems, "items" : items}, of, indent=2)

    # totalProductSearch, items = productscrapping.getContent(numberOfProduct = 100, outputFormat="object")
    # print(items)