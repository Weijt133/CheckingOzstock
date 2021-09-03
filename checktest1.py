from bs4 import BeautifulSoup
import requests
import urllib
import sys

#This program is used to check if the product in Ozstock website is sold out.
url = input("Please enter the product's link from Ozstock:")
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
images = soup.findAll('img',{"src":True})
for image in images:
    #Check whether the product is in stock or not
    if str(image['src']) == "/images/soldout_bt.gif":
        print('\n\nThis product has been sold out.\n\n')
        break

else:
    print('\n\nThis product in stock.\n\n')

#TO keep the exe program doesn't close automaticly.
input('Please enter any key.')