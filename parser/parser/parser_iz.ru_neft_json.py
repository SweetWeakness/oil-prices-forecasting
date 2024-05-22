import json
import httpx
import pandas as pd


url = "https://iz.ru/api/0/tag/neft"

# Общее количество новостей, которые нужно собрать
total_news = 1000
offset = 4500

# Список для хранения новостей
news_list = []

# Цикл для парсинга новостей
while len(news_list) < total_news:
    # Параметры запроса
    json_data = {
        "include": {
            "materials": {"limit": 50, "offset": offset + len(news_list)},
        }
    }
    params = {"json": json.dumps(json_data)}

    # Заголовки запроса
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36",
        "Referer": "https://iz.ru/tag/neft",
    }

    # Отправка запроса
    response = httpx.get(url, params=params, headers=headers)

    # Проверка статуса ответа
    if response.status_code == 200:
        data = response.json()

        # Добавление новостей в список
        news_list.extend(data["included"]["materials"]["objects"])

        # Вывод текущего количества новостей
        print(f"Собрано {len(news_list)} новостей из {total_news}")

        # Создание DataFrame из списка новостей
        df = pd.DataFrame(news_list)

        # Дозапись DataFrame в CSV-файл в кодировке utf-8
        with open("news_links.csv", mode="a", encoding="utf-8") as file:
            df.to_csv(file, header=file.tell() == 0, index=False)

    else:
        print(f"Ошибка: {response.status_code}")
        break
