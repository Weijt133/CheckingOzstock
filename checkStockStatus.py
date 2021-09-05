from bs4 import BeautifulSoup
import requests
import urllib
import sys

""""This method is used to check the stock status in Ozstock."""
def checkOzstock(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    images = soup.findAll('img', {"src": True})
    for image in images:
        # Check whether the product is in stock or not
        if str(image['src']) == "/images/soldout_bt.gif":
            return "Out of stock"
            break

    else:
        return "In stock"


#This program is used to check if the product in Ozstock website is sold out.
url1 = input("Please enter the product's link from Ozstock:")
print(checkOzstock(url1))
#TO keep the exe program doesn't close automaticly.
input('Please enter any key.')
