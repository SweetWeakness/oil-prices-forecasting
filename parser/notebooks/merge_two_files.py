import pandas as pd
import sys

def merge_files(file1, file2, outfile):
    # Открываем первый файл
    df1 = pd.read_csv(file1, parse_dates=['datetime'])

    # Открываем второй файл и меняем формат даты
    df2 = pd.read_csv(file2)
    df2['Date'] = pd.to_datetime(df2['Date'], format='%m/%d/%Y')

    # Делаем merge двух DataFrame
    df = pd.merge(df1, df2, left_on='datetime', right_on='Date')

    # Сохраняем результат в новый файл
    df.to_csv(outfile, index=False)

if __name__ == '__main__':
    # Проверяем, что передано три аргумента
    if len(sys.argv) != 4:
        print('Usage: python merge_files.py <file1> <file2> <outfile>')
        sys.exit(1)

    # Вызываем функцию, передавая названия файлов как аргументы
    merge_files(sys.argv[1], sys.argv[2], sys.argv[3])
