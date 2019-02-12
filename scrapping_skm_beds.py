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
]

with open('skm_beds.csv', 'a') as csv_file:
    writer = csv.writer(csv_file)
    for url in urls:
        page_link = 'https://skmfurniture.com.au/product-category/modern-beds/' + url
        page = requests.get(page_link, headers=headers)

        soup = BeautifulSoup(page.text, 'html.parser')

        productBeds = soup.find_all("div", class_="prod-name")
        productPrices = soup.find_all("div", class_="price")

        for productBed, productPrice in zip(productBeds, productPrices):
            productBed = productBed.text
            productPrice = productPrice.text
            # print(productBed.text, productPrice.text)

            print('Writing Beds to csv...')
            writer.writerow([productBed, productPrice])

