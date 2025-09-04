import pandas as pd;
from app.features.explore_data import explore_data, count_isnull

#задание 1.1 Загрузить titanic.csv в pandas DataFrame.
df = pd.read_csv('app/data/train.csv')

def main():
    explore_data(df)
    count_isnull(df)

if __name__ == "__main__":
    main()