import time 
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request


def get_X_picture():

    # file savename 
    picture_filename = 'x_picture2.jpg'

    # open firefox browser 
    driver = webdriver.Firefox()

    # open url 
    driver.get('https://x.com/FabrizioRomano/status/1825513124918677856/photo/1')

    # wati enough time 
    time.sleep(20)

    # Using beautifulsoup to find the image 

    soup = BeautifulSoup(driver.page_source , features="lxml")
    images = soup.find_all('img')

    images = [img['src'] for img in images if '/media/' in img['src']]

    for image in images : 
        urllib.request.urlretrieve(image , picture_filename)
        

if __name__ == '__main__':
    get_X_picture()