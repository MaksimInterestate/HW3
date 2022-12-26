# Написать простой парсер для извлечения информации с любого сайта.
# Например - новость, или погоду с сайта mail.ru
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю']

import requests
from bs4 import  BeautifulSoup as bs
url = 'https://www.rambler.ru'
response = requests.get(url).text # приеобразовал в текст весь сайт
soup = bs(response, 'html.parser')
razdel = soup.find('div', class_='rui__1uzyO') # find_all() список всех найденных элементов
print(razdel.text)




url2 = 'https://news.rambler.ru/'
response2 = requests.get(url2).text
soup2 = bs(response2, 'html.parser')
news = soup2.find('div', class_='_2TC8G commercial-branding')
print(news.text)



