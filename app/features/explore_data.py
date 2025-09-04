import pandas as pd;

#задание 1.2 Посмотреть первые строки (head), структуру (info), статистику (describe).
def explore_data(df: pd.DataFrame): 
    print('Первые 5 строк:\n', df.head())
    print('Структура:')
    df.info()
    print('Статастика:\n', df.describe())

#задание 1.3 Посчитать количество пропусков (isnull().sum()).
def count_isnull(df: pd.DataFrame):
    # заменим пустые строки на NaN для всех строковых колонок
    df.replace('', pd.NA, inplace=True)
    print('Количество пропусков:\n', df.isnull().sum())