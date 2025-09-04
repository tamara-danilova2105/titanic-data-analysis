import pandas as pd;

#задание 2.1 Заполнить пропуски в Age медианой.
def age_fillna_median(df: pd.DataFrame):
    df['Age'] = df['Age'].fillna(df['Age'].median())
    return df

#задание 2.2 Заполнить пропуски в Embarked модой.
def embarked_fillna_moda(df: pd.DataFrame):
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
    return df

#задание 2.3 ЗПреобразовать Sex в числовой вид (0 = male, 1 = female).
def encode_sex(df: pd.DataFrame):
    df = df.copy()
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    return df

def preprocess_data(df: pd.DataFrame):
    age_fillna_median(df)
    embarked_fillna_moda(df)
    encode_sex(df)

    # сохраняем новый файл
    df.to_csv("app/data/train_clean.csv", index=False)
    print("\n✅ Датасет сохранён в app/data/train_clean.csv")

    return df