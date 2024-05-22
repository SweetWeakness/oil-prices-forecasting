from datetime import datetime
import random
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера
driver = webdriver.Chrome()

# Открываем сайт
driver.get("https://iz.ru/tag/neft")

# Создаем пустой DataFrame
df = pd.DataFrame(columns=["title", "url", "date"])

# Параметры для задержки между запросами
MIN_DELAY = 1
MAX_DELAY = 2


# Функция для парсинга новостей на текущей странице
def parse_news():
    # Находим все блоки с новостями
    news_blocks = driver.find_elements(By.CSS_SELECTOR, "div.tag-materials-item__box")

    # Перебираем блоки с новостями
    for block in news_blocks:
        # Извлекаем заголовок, ссылку и дату новости
        title = block.find_element(
            By.CSS_SELECTOR, "h3.tag-materials-item__title"
        ).text.strip()
        url = block.find_element(By.CSS_SELECTOR, "a.tag-materials-item").get_attribute(
            "href"
        )
        date_element = block.find_element(
            By.CSS_SELECTOR, "div.tag-materials-item__date"
        )
        date_published = date_element.find_element(
            By.CSS_SELECTOR, "meta[itemprop='datePublished']"
        ).get_attribute("content")
        date = datetime.strptime(date_published, "%Y-%m-%dT%H:%M:%S.%fZ").strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Объединяем временный DataFrame с основным DataFrame

        df.loc[len(df.index)] = [title, url, date]


# Функция для нажатия кнопки "Показать еще"
def click_show_more_button():
    # Находим кнопку "Показать еще"
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-show-more")

    # Нажимаем кнопку "Показать еще"
    button.click()


# Парсим новости в цикле 100 раз
for i in range(10):
    # Парсим новости на текущей странице
    parse_news()

    # Нажимаем кнопку "Показать еще"
    click_show_more_button()

    # Ждем загрузки новых новостей
    time.sleep(random.uniform(MIN_DELAY, MAX_DELAY))

# Выводим DataFrame с новостями
print(df)

# Закрываем браузер
driver.quit()
