import unittest
import checkStockStatus

class TestStringMethods(unittest.TestCase):

    def test_checkOzstock(self):
        urlOOS = "https://www.ozstock.com.au/26793/Multifunctional-Fashion-Alarm-Clock-with-USB-Charger,-Wireless-Charging-with-Date-Time-Temperature.html"
        urlIS = "https://www.ozstock.com.au/21814/Saddle-Salon-PU-Leather-Swivel-Stool-Chair.html"
        self.assertEqual(checkStockStatus.checkOzstock(urlOOS), "Out of stock")
        # check about item out of stock
        self.assertEqual(checkStockStatus.checkOzstock(urlIS), "In stock")
        # check about item in stock

if __name__ == '__main__':
    unittest.main()