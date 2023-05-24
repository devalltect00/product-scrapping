from product import ProductScrapping
import unittest

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = ProductScrapping("Bukalapak", "Samsung Galaxy")
    
    def test_collectionOfItem_packet(self):
        self.assertEqual(self.product.collectionOfItem_packet(), [("div", "bl-flex-container flex-wrap is-gutter-16")])
    def test_eachItem_packet(self):
        self.assertEqual(self.product.eachItem_packet(), [("div", "bl-flex-item mb-8")])
    def test_picture_packet(self):
        self.assertEqual(self.product.picture_packet(), [(None, None), ("img", None)])
    def test_overview_packet(self):
        self.assertEqual(self.product.overview_packet(), [("div", "bl-product-card__description")])
    def test_name_packet(self):
        self.assertEqual(self.product.name_packet(), [("div", "bl-product-card__description-name")])
    def test_price_packet(self):
        self.assertEqual(self.product.price_packet(), [("div", "bl-product-card__description-price")])
    def test_location_packet(self):
        self.assertEqual(self.product.location_packet(), [("div", "bl-product-card__description-store")])

if __name__ == '__main__':
    unittest.main()