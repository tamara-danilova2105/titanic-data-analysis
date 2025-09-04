import pandas as pd;

#задание 1.2 Посмотреть первые строки (head), структуру (info), статистику (describe).
def explore_data(df: pd.DataFrame): 
    print('Первые 5 строк', df.head())
    print('Структуру', df.info())
    print('Статистика', df.describe())

#задание 1.3 Посчитать количество пропусков (isnull().sum()).
def count_isnull(df: pd.DataFrame):
    print('количество пропусков', df.isnull().sum())