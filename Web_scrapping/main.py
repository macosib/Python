import requests
from bs4 import BeautifulSoup
import os

BASE_URL = 'https://habr.com'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
}

with open(os.path.join(os.getcwd(), 'keywords.txt'), 'r', encoding='UTF-8') as f:
    KEYWORDS = frozenset(map(lambda x: x.lower().strip(), f.readlines()))


def get_articles(page_count=1):
    result = []
    count = 0
    while count != page_count:
        response = requests.get(url=BASE_URL + f'/ru/all/page{count + 1}', headers=HEADERS)
        if response.status_code not in range(200, 299):
            raise Exception("Не удалось получить ответ")
        soup = BeautifulSoup(response.text, features='html.parser')
        articles = soup.find_all('article')
        result.extend(articles)
        count += 1
    return result


def find_keywords(value_1: set, value_2=KEYWORDS):
    return True if value_1 & value_2 else False


def article_text(post_url):
    response = requests.get(url=BASE_URL + post_url, headers=HEADERS)
    if response.status_code not in range(200, 299):
        raise Exception("Не удалось получить ответ")
    soup = BeautifulSoup(response.text, features='html.parser')
    data_text = soup.find(class_='tm-article-body').text.lower()
    data = set(data_text.split())
    return find_keywords(data)


def get_info(article):
    name_post = article.find(class_='tm-article-snippet__title-link').text
    link = BASE_URL + article.find('a', class_='tm-article-snippet__title-link').attrs['href']
    data_post = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title'].split(",")[0]
    return f'Дата поста: {data_post}, Заголовок: {name_post}, Ссылка: {link}'


def main():
    count_page_for_scrapping = int(input('Введите кол-во страниц, с которых будут взяты заголовки: '))
    articles = get_articles(count_page_for_scrapping)
    for article in articles:
        url_post = article.find('a', class_='tm-article-snippet__title-link').attrs['href']
        if article_text(url_post):
            print(get_info(article))


if __name__ == '__main__':
    main()
