import json
# from multipledispatch import dispatch
# from typing import overload
import requests
from bs4 import BeautifulSoup
from constant import *

class Shop:
    def __init__(self, name):
        with open(INGREDIENTS) as i:
            self.ingredients = json.load(i)
        self.name = name
        self.index = self.getIndexShopType()
        self.linkWebsite = self.getLink()
        # self.setSoup()

    # readable
    def __str__(self):
        return "Shop object with property:" + self.printList([f"name = {self.name}", f"index = {self.index}", f"link website = {self.linkWebsite}"])
    
    # unambiguous representation
    def __repr__(self):
        return f"Shop(name:{self.name}, index:{self.index}, link website:{self.linkWebsite})"
    
    # getter and setter
    # @property
    # def name(self):
    #     return self._name
    
    # @name.setter
    # def name(self, value, isSet=True):
    #     self._name = value
    #     self.index = self.getIndexShopType()
    #     self.linkWebsite = self.getLink()

    def changeName(self, name):
        # self._name = name
        self.name = name
        self.index = self.getIndexShopType()
        self.linkWebsite = self.getLink()

    # get shopList item list <section>
    def shopList_section(self):
        return self.ingredients["shopList"]
    
    # get detail item list <section>
    def detailList_section(self):
        return self.ingredients["detail"]
    
    # get index based on shop type
    def getIndexShopType(self):
        return self.shopList_section().index(self.name)
    

    # get detail for specific shop
    def getDetail(self):
        return self.detailList_section()[self.getIndexShopType()]
    
    # get link website for specific shop
    def getLink(self):
        return self.getDetail()["link"]
    
    def getLinkFormat(self, itemSearch):
        itemSearch = itemSearch.replace(" ", self.getSpaceLinkFormat())
        return self.getDetail()["linkSearchItem"]["format"].replace("{...}", itemSearch)
    
    def getSpaceLinkFormat(self):
        return self.getDetail()["linkSearchItem"]["spaceFormat"]["to"]
    
    @staticmethod
    def printList(items): 
        s=""
        for i in items:
            s+="\n* "+i
        return s

# print("Hi this is from python")
# sys.stdout.flush()

if __name__ == '__main__':
    # print("Hi this is from python")
    shop = Shop("Lazada")
    print(shop.name)
    print(shop.index)
    print(shop.linkWebsite)
    print(repr(shop))
    shop.name = "Shopee"
    print(shop.name)
    print(shop.index)
    print(shop.linkWebsite)