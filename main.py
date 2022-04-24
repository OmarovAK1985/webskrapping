import requests
from bs4 import BeautifulSoup
import re

url = 'https://habr.com'

ret = requests.get('https://habr.com/ru/all/')

soup = BeautifulSoup(ret.text, 'html.parser')

results = soup.find_all('article')
KEYWORDS = ['почты', 'PHP', 'Vue', 'python', 'С++']
my_list_urls = []
count = 0
for i in results:
    title = i.find('h2').text
    for k in KEYWORDS:
        if k in title:
            count = count + 1
            href = i.find('h2').find('a').attrs['href']
            url_ = url + href
            date = i.find(class_="tm-article-snippet__datetime-published").find('time').attrs['title'][0:10]
            print(f'{count}. Название статьи: {title.upper()}')
            print(f'\t Ссылка на статью {url_}')
            print(f' \t Дата публикации: {date}')
            my_list_urls.append(url_)
print(f'В выборку попало {count} статей. {len(results) - count} статей отсеялось.')
print('________________')

count = 0
for url in my_list_urls:
    ret = requests.get(url)
    soup = BeautifulSoup(ret.text, 'html.parser')
    soup.find(class_='article_formatted_body')
    texts = soup.find_all('p')
    title = soup.find('h1').text
    text = str()
    for i in texts:
        text = text + i.text
    if re.search(r'инфра\w+', text):
        count = count + 1
        print(f'{count}. Название статьи - {title.upper()}')
        print(f'\t {text}')
    else:
        print('Ничего не найдено')
        break






