from bs4 import BeautifulSoup
import requests

data = []
url = 'https://www.kitapyurdu.com/index.php?route=product/bargain&category=0&discount=60&filter_in_stock=1&sort=p.price&order=ASC&limit=50'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html5lib')

title = soup.find_all('div', {'class': 'name ellipsis'})
print(title)
for i in title:
    print(i.getText())
    data.append(i.getText())


with open('out.txt', 'w') as output:
    output.write(str(data))
