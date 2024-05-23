import time
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Количество странци
pages_len = 1196

# Перебираем страницы от 1 до 1196
for page in range(506, pages_len):
    time.sleep(3)
    print(f"Собрано {page} страниц новостей из {pages_len}")

    url = f"https://neftegaz.ru/tags/нефть/{page}/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    if response.status_code != 200:
        break

    # Список для хранения новостей
    news_list = []

    # Находим все блоки с новостями на странице
    news_blocks = soup.find_all("div", class_="news_week__item")

    # Перебираем каждый блок с новостью
    for news_block in news_blocks:
        # Извлекаем дату, ссылку и заголовок
        date = news_block.find("div", class_="date").text
        link = news_block.find("a")["href"]
        title = news_block.find("div", class_="title").text

        # Добавляем новость в список
        news_list.append([date, link, title])

    # Сохраняем новости в файл после каждой страницы
    df = pd.DataFrame(news_list, columns=["Дата", "Ссылка", "Заголовок"])

    # Дозапись DataFrame в CSV-файл в кодировке utf-8
    with open("news.csv", mode="a", encoding="utf-8") as file:
        df.to_csv(file, header=file.tell() == 0, index=False)
