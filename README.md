# News_Categorization using Machine Learning

This project aims to classify news articles into categories like World, Sports, Business, and Sci/Tech using machine learning. The model is trained on preprocessed news data, and features are extracted using TF-IDF. A Logistic Regression model serves as a baseline for classification.

## Current Status

- Data Preprocessing: Complete
- Logistic Regression Model: Complete
- Further model improvements, such as hyperparameter tuning and trying other models, are planned for future iterations.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sina83-max/News_Categorization.git
cd news-categorization
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download the dataset

Download the dataset from Kaggle AG News Dataset and place it in the `data/raw/` directory. Please follow this link:
https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset

### 4. Preprocess the data

Preprocess the dataset by running:

```bash
python src/data_loader.py
```

### 5. Train the model

Train the model by running:

```bash
python src/model.py
```

## Future Work and Contributions

- Implement hyperparameter tuning for Logistic Regression.
- Experiment with other models like Random Forest and Support Vector Machines (SVM).
- Consider building a deep learning model (e.g., LSTM or BERT).

If you'd like to contribute, feel free to fork the repository and submit a pull request with your improvements!
