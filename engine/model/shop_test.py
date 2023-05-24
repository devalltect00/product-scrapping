from shop import Shop
import unittest

class TestShopProv(unittest.TestCase):
    def setUp(self):
        self.shop = Shop("Lazada")

    def test_repr(self):
        self.assertEqual(repr(self.shop), "Shop(name:Lazada, index:0, link website:https://www.lazada.co.id)")
    
    def test_setName(self):
        # self.shop.name = "Shopee"
        self.shop.changeName("Shopee")
        self.assertEqual(self.shop.name, "Shopee")
        self.assertEqual(self.shop.index, 1)
        self.assertIsInstance(self.shop.index, int)
        self.assertEqual(self.shop.linkWebsite, "https://shopee.co.id/")

    def test_(self):
        self.shop.changeName("Shopee")
        self.assertEqual(self.shop.getLinkFormat("iphone"), "https://shopee.co.id/search?keyword=iphone")
        self.assertEqual(self.shop.getLinkFormat("samsung"), "https://shopee.co.id/search?keyword=samsung")
        self.assertEqual(self.shop.getLinkFormat("samsung galaxy A23"), "https://shopee.co.id/search?keyword=samsung%20galaxy%20A23")
        self.assertEqual(self.shop.getLinkFormat("iphone 6"), "https://shopee.co.id/search?keyword=iphone%206")

if __name__ == '__main__':
    unittest.main()