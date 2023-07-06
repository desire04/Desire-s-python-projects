from bs4 import BeautifulSoup
import requests
from csv import writer

"""request website url from which the required information is needed"""
url = "https://www.pararius.com/apartments/amsterdam"
page = requests.get(url)

"""parse the website's content as a html file using the BeautifulSoup library"""
sam = BeautifulSoup(page.content, 'html.parser')
lyst = sam.find_all('section', class_ = "listing-search-item")

"""Create the file that will store the information obtained"""
with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    thewriter.writerow(header)

"""iterate through the contents in the url, locate appropriate information, and store
it under the appropriate sub-headings in the housing.csv file"""

    for element in lyst:
        title = element.find('h2', class_="listing-search-item__title").text.replace('\n', '')
        location = element.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
        price = element.find('div', class_="listing-search-item__price").text.replace('\n', '')
        area = element.find('li', class_="illustrated-features__item--surface-area").text.replace('\n', '')

        info = [title, location, price, area]
        thewriter.writerow(info)


