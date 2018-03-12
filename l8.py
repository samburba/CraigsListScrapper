#!/usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen

city = "chico"
#num_listings = 360
item = "xbox"
page_url = "http://%s.craigslist.org/search/sss?query=%s" % (city, item)

sauce = urlopen(page_url)
soup = BeautifulSoup(sauce, 'lxml')

num_listings = int(soup.find('span', class_='totalcount').text)

counter = 0
while counter < num_listings:
    for listing in soup.find_all('p'):
        a = listing.find('a', class_='result-title hdrlnk') 
        post_title = a.text.replace(',', '')
        post_link = a['href']
        post_price = listing.find('span', class_='result-price')
        if post_price is not None:
            post_price = post_price.text
        post_city = listing.find('span', class_='result-hood')
        if post_city is not None:
            post_city = post_city.text[2:-1].upper().replace(',','')
        post_date = listing.find('time', class_='result-date')['datetime']
        print("%s,%s,%s,posted:%s,%s" % (post_title, post_price, post_city,
            post_date, post_link))
        counter += 120
    page_url = "http://%s.craigslist.org/search/sss?s=%d&query=%s" % (city,
                counter, item)
    sauce = urlopen(page_url)
    soup = BeautifulSoup(sauce, 'lxml')
