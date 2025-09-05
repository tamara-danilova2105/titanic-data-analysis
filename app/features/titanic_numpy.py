import pandas as pd
import numpy as np

#задание 5.1 - Загружаем данные и превращаем в numpy массивы
def load_titanic_data(path="app/data/train_clean.csv"):
    df = pd.read_csv(path)

    survived = df["Survived"].to_numpy()
    sex = df["Sex"].to_numpy()        # 0 = male, 1 = female
    pclass = df["Pclass"].to_numpy()
    age = df["Age"].to_numpy()
    fare = df["Fare"].to_numpy()

    return survived, sex, pclass, age, fare

#задание 5.2 - Средний возраст выживших и погибших
def mean_age_by_survival(survived, age):
    print("\n Средний возраст выживших:", age[survived == 1].mean())
    print("Средний возраст погибших:", age[survived == 0].mean())

#задание 5.3 - Шансы на выживание мужчин и женщин
def survival_by_sex(survived, sex):
    print("\n Доля выживших женщин:", survived[sex == 1].mean())
    print("Доля выживших мужчин:", survived[sex == 0].mean())

#задание 5.4 - Шансы на выживание по классам
def survival_by_class(survived, pclass):
    print("\n Доля выживших по классам:")
    for c in [1, 2, 3]:
        print(f"Класс {c}: {survived[pclass == c].mean():.2f}")

#задание 5.5 - Нормализация цен на билеты
def normalize_fare(fare):
    fare_norm = (fare - fare.min()) / (fare.max() - fare.min())
    print("\n Первые 10 нормализованных цен:", fare_norm[:10])

#задание 5.6 - Дисперсия возраста у выживших и погибших
def variance_age_by_survival(survived, age):
    print("\n Дисперсия возраста выживших:", age[survived == 1].var())
    print("Дисперсия возраста погибших:", age[survived == 0].var())

def titanic_numpy():
    survived, sex, pclass, age, fare = load_titanic_data()

    mean_age_by_survival(survived, age)
    survival_by_sex(survived, sex)
    survival_by_class(survived, pclass)
    normalize_fare(fare)
    variance_age_by_survival(survived, age)