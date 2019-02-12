#import libraries
from bs4 import BeautifulSoup
import requests

#specify the url
# url = 'http://schitru.com/description-image.php'

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

#print all soup with prettify
# print(soup.prettify())

#title text of page
# match = soup.title.text
# print(match)

#find item in html tag 'div'
# match = soup.find('div')
# print(match)

#get using class
# match = soup.find('div', class_='footer')
# print(match)

# article = soup.find('div', class_='article')
# print(article)

# headline = article.h2.a.text
# print(headline)

# summary = article.p.text
# print(summary)


#findall
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()