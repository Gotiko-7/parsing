import requests
from bs4 import BeautifulSoup
from pprint import pprint
import csv

url = "https://softech.kg/noutbuki/"

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

r = requests.get(url, headers=headers)
src = r.text
print(src)

# with open('index.html', 'w') as f:
#     f.write(src)
#
with open('index.html', 'r') as f:
    src = f.read()
#    print(src)


soup = BeautifulSoup(src, 'lxml')
finder = soup.find_all('div', class_='product-thumb transition')


nb = []
for i in finder:
    nb.append({
       'Names': i.find('div', class_='name').get_text(strip=True),
        'Price': i.find('div', class_='price').get_text(strip=True),
        'Info': i.find('div', class_='description-small').get_text(strip=True)

    }
    )

#pprint(nb)

with open('data.csv', 'w') as f:
     writer = csv.writer(f)
     writer.writerow(
         ('Название',
          'Описание',
          'Цена'
          )
     )

for i in range(len(nb)):
    names = nb[i]['Names']
    info = nb[i]['Info']
    price = nb[i]['Price']
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            (names,
             info,
             price
    )
)
