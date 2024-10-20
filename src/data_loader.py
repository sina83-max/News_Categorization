import pandas as pd


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


if __name__ == "__main__":
    raw_data_path = "data/raw/ag_news.csv"

data = load_date(raw_data_path)

if data is not None:
    print(data.head())
