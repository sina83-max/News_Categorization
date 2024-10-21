import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from joblib import dump
from feature_extraction import extract_features


def train_model(X, y):

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    model = LogisticRegression(max_iter=200)

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy * 100:.2f}%")
    print(classification_report(y_test, y_pred))

    return model, X_test, y_test, y_pred


if __name__ == "__main__":
    proccesed_data_path = "data/processed/proceesed_ag_news.csv"
    df = pd.read_csv(proccesed_data_path)

    X, vectorizer = extract_features(
        df, text_column='cleaned_text', max_features=5000)
    y = df['Class Index']

    model, X_test, y_test, y_pred = train_model(X, y)

    dump(model, 'models/logistic_regressin_model.joblib')
    dump(vectorizer, 'models/tfidf_vectorizer.joblib')
