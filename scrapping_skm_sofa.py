from bs4 import BeautifulSoup
import requests
import csv 

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

urls = [
    '',
    'page/2/',
    'page/3/',
    'page/4/',
    'page/5/',
    'page/6/',
    'page/7/',
    'page/8/',
    'page/9/',
    'page/10/',
    'page/11/',
]

with open('skm_sofa.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for url in urls:
        page_link = 'https://skmfurniture.com.au/product-category/sofa-couches/' + url
        page = requests.get(page_link, headers=headers)

        soup = BeautifulSoup(page.text, 'html.parser')

        productSofas = soup.find_all("div", class_="prod-name")
        productPrices = soup.find_all("div", class_="price")

        for productSofa, productPrice in zip(productSofas, productPrices):
            productSofa = productSofa.text.strip()
            productPrice = productPrice.text.strip()
            # print(productBed.text, productPrice.text)

            print('Writing to csv...')
            writer.writerow([productSofa, productPrice])

