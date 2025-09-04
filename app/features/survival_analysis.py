import pandas as pd;

#задание 3.1 Найти долю выживших (Survived) среди мужчин и женщин.
def survived_by_sex(df: pd.DataFrame):
    result = df.groupby('Sex')['Survived'].mean().round(2)
    print('\n Выживамость по полу:')
    print(result)

#задание 3.2 Найти долю выживших по классам кают (Pclass).
def survived_by_pclass(df: pd.DataFrame):
    result = df.groupby('Pclass')['Survived'].mean().round(2)
    print('\n Выживамость по классам кают:')
    print(result)

#задание 3.2 Построить сводную таблицу выживаемости по полу и классу (groupby).
def pivot_survived_by_sex_pclass(df: pd.DataFrame):
    pivot = df.groupby(["Sex", "Pclass"])["Survived"].mean().unstack()
    print('\n Сводная таблица выживаемости по полу и классу:')
    print(pivot)

def survival_analysis(df: pd.DataFrame):
    survived_by_sex(df)
    survived_by_pclass(df)
    pivot_survived_by_sex_pclass(df)