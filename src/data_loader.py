import pandas as pd
from pre_process import clean_text

x = pd.read_csv(
    '/Users/sina/Desktop/ML_projects/News_Categorization/data/raw/ag_news.csv')
print(x.columns)


def load_date(file_path):
    '''
    This function is a pre_write module so you can ensure that the data are loaded completely
    '''

    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def save_data(df, save_path):
    try:
        df.to_csv(save_path, index=False)
        print(f"Preprocessed data saved to {save_path}")
    except Exception as e:
        print(f"Error saving dataset: {e}")


def preprocess_data(df):
    df['cleaned_text'] = df['Description'].apply(clean_text)
    return df


if __name__ == "__main__":
    raw_data_path = "data/raw/ag_news.csv"

data = load_date(raw_data_path)

if data is not None:
    preprocessed_data = preprocess_data(data)
    print(preprocessed_data[['Description', 'cleaned_text']].head())

    save_data(preprocessed_data, 'data/processed/proceesed_ag_mews.csv')
