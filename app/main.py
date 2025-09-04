import pandas as pd;
from app.features.explore_data import explore_data, count_isnull
from app.features.preprocess_data import preprocess_data
from app.features.survival_analysis import survival_analysis

#задание 1.1 Загрузить titanic.csv в pandas DataFrame.
df = pd.read_csv('app/data/train.csv')
clean_df = pd.read_csv('app/data/train_clean.csv')

def main():
    explore_data(df)
    count_isnull(df)
    preprocess_data(df)
    survival_analysis(clean_df)

if __name__ == "__main__":
    main()