import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#задание 4.1 Построить гистограмму возраста пассажиров.
def plot_age_passengers(df: pd.DataFrame):
    df["Age"].plot(kind="hist", bins=10, title="Распределение возраста")
    plt.xlabel("Возраст")
    plt.ylabel("Количество пассажиров")
    plt.show()

#задание 4.2 Построить bar chart выживаемости по полу.
def plot_survival_by_sex(df: pd.DataFrame):
    survival_by_sex = df.groupby("Sex")["Survived"].mean()

    sns.barplot(x=survival_by_sex.index, y=survival_by_sex.values)
    plt.title("Выживаемость по полу")
    plt.ylabel("Доля выживших")
    plt.xlabel("Пол")
    plt.show()

#задание 4.3 Построить scatter plot: возраст vs цена билета.
def plot_age_vs_fare(df: pd.DataFrame):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df, x="Age", y="Fare", hue="Survived", alpha=0.6)
    plt.title("Возраст vs Цена билета")
    plt.xlabel("Возраст")
    plt.ylabel("Цена билета")
    plt.show()

def visualization(df: pd.DataFrame):
    plot_age_passengers(df)
    plot_survival_by_sex(df)
    plot_age_vs_fare(df)