import requests
from bs4 import BeautifulSoup
import io

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}


def write_In_file(url):
    # создаем сессию и отправляем get запрос
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    # запишем html в файл
    with io.open("ht.html", "w", encoding="utf-8") as file:
        file.write(response.text)


def get_page():
    with open("ht.html", encoding="utf8") as file:
        # читает ранее записанный код
        src = file.read()

    # используем lxml т.к. он быстрее парсит
    soup = BeautifulSoup(src, "lxml")
    all_news_part = soup.find_all("div", class_="cell-list__item m-no-image")
    print(all_news_part)

    # у этого сайта 2 вида новостей.

    news_dict = []
    for news in all_news_part:
        # извлекаем дату
        date = news.find('span', class_="elem-info__date").get_text(strip=True)
        # извлекаем url
        url = news.a.get('href')
        # извлекаем новость
        content = news.find('span', class_="cell-list__item-title").get_text(strip=True)

        news_dict.append({
            'date': date,
            'url': url,
            'content': content,
        })

    with open('info.txt', 'w', encoding='utf-8') as f:
        for item in news_dict:
            f.write(
                f'\n\nВремя: {item["date"]}\nНовость: {item["content"]}\nКонтент: {item["url"]}\n\n\n_______________________\n')

    soup = BeautifulSoup(src, "lxml")
    all_news_part2 = soup.find_all("div", class_="cell cell-main-photo")
    print(all_news_part2)
    news_dict1 = []
    new = []
    for news1 in all_news_part2:
        # извлекаем URL картинки

        # извлекаем название
        content1 = news1.find('span', class_="cell-main-photo__desc").get_text(strip=True)
        # Время
        date1 = news1.find('span', class_="elem-info__date").get_text(strip=True)
        # извлекаем url
        # url1 = news1.find('a', class_="cell-main-photo__link").get(href=True)


        for link in soup.find_all('a', class_="cell-main-photo__link"):
            t=link.get('href')


            news_dict1.append({
                'date1': date1,
                'content1': content1,
                'url1': t,
            })

        with open('info.txt', 'a', encoding='utf-8') as f:
            for item1 in news_dict1:
                f.write(
                    f'\n\nВремя: {item1["date1"]}\nНовость: {item1["content1"]}\nКонтент: {item1["url1"]}\n\n\n_______________________\n')


def main():
#    write_file("https://ria.ru/")
    get_page()


if __name__ == "__main__":
    main()
