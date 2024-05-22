import csv
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Открываем файл с ссылками на новости
with open('neftegaz.ru_news.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    # next(reader)  # пропускаем заголовок

    # Создаем DataFrame для записи новостей
    columns = ['link', 'datetime', 'headline', 'description', 'articleBody']

    # Перебираем ссылки на новости
    for i, row in enumerate(reader):
        time.sleep(1)
        link = row[1]

        print(f"Собрано {i+1} новостей {link[:40]}")

        # Делаем запрос и парсим страницу
        while True:
            try:
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'html.parser')
                break
            except requests.exceptions.ConnectionError:
                print("Ошибка подключения, повторная попытка...")
                time.sleep(5)

        # Извлекаем данные о новости
        if soup.find('time', {'itemprop': 'datePublished'}) == None:
            continue
        datetime = soup.find('time', {'itemprop': 'datePublished'})['datetime']
        headline = soup.find('h1', {'itemprop': 'headline'}).text.strip()

        description = ""
        descriptionDiv = soup.find('p', {'itemprop': 'description'})
        if descriptionDiv  != None:
            description = descriptionDiv.text.strip()

        articleBody = soup.find('div', {'itemprop': 'articleBody'}).text.strip()

        # Создаем DataFrame для одной новости
        news_data = pd.DataFrame([[link, datetime, headline, description, articleBody]], columns=columns)

        # Сохраняем DataFrame в файл
        news_data.to_csv('news_data.csv', index=False, mode='a', header=not i)
