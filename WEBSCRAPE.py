
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from requests import get
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
myurl = "https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Hyderabad"
response = get(myurl, headers=headers)
page_soup = soup(response.text, 'html.parser')
containers = page_soup.findAll('div',{'class':'flex relative clearfix m-srp-card__container'})
container = containers[0]

for container in containers:
    bhk_container = container.findAll('span',{'class':'m-srp-card__title__bhk'})
    bhk = bhk_container[0].text
    
    price_container = container. findAll('span',{'class':'m-srp-card__price'})
    price = price_container[0].text
    
    socity_container = container.findAll('a',{'class':'m-srp-card__link'})
    socity = socity_container[0].text
    
    print(bhk)
    print(price)
    print(socity)


