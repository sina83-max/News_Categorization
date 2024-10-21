import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os


def extract_features(df, text_column, max_features=5000):

    vectorizer = TfidfVectorizer(
        max_features=max_features, stop_words='english')

    X = vectorizer.fit_transform(df[text_column])

    return X, vectorizer


if __name__ == "__main__":
    processed_data_path = "data/processed/proceesed_ag_news.csv"

    if os.path.exists(processed_data_path):
        df = pd.read_csv(processed_data_path)

        X, vectorizer = extract_features(
            df, text_column='cleaned_text', max_features=5000)
    else:
        print(f"Preprocessed dataset not found at {processed_data_path}")
