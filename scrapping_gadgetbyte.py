from bs4 import BeautifulSoup
import requests
import csv

source = 'https://www.gadgetbytenepal.com/category/mobile-price-in-nepal/'

#the page rejects GET requests that do not identify a  User-Agent
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

# soup = BeautifulSoup(source, 'lxml')
try:
    url = requests.get(source, headers=headers)
except requests.exceptions.RequestException as e:
    print(e)
    exit()

#entire html
soup = BeautifulSoup(url.text, "html.parser")
# print(soup.prettify())

#filtering / parsing the needed sections
# m_name = soup.find('div', class_='td-category-description')

#getting mobile names from site
# name = soup.find('table')
# mobile_name = name.a.text

#getting price
# name = soup.find('table', attrs={'class': 'td:last-child'})
# name = soup('tr')[-1]
# mobile_price = name.text

mobiles = soup.find('div', class_='td-category-description')

csv_file = open('gadgetbyte.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Mobile Name', 'Price'])

for mobile in mobiles.find_all('td'):
    # print(mobile.text) 
    # print(mobile.next_sibling)
    mobile_name = mobile.text
    mobile_price = mobile.next_sibling

    print(mobile_name)
    print(mobile_price)
    
    csv_writer.writerow([mobile_name, mobile_price])

csv_file.close()
# l = []
# for tr in table_rows:
#     td = tr.find_all('td')
#     row = [tr.text for tr in td]
#     l.append(row)

#mobile name and cost - 2ndway
#name of brand
# mobile_src = soup.find_all('td')
# mobile = mobile_src.renderContents()
# print(mobile)
# brand_name = mobile.strip()

# mobile_prc = soup.find("td").find_next_sibling("td")
# mob = mobile_prc.renderContents()
# mobile_price = mob.strip()

# mobile_desc = [ mobile, mob ]

# for mobile in mobile_desc:
#     print (mobile)
    

