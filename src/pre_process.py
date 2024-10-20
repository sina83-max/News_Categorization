import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stopwords = set(stopwords.words('english'))


def clean_text(text):

    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    tokens = word_tokenize(text)

    filtered_tokens = []
    for word in tokens:
        if word not in stopwords:
            filtered_tokens.append(word)

    cleaned_text = ' '.join(tokens)

    return cleaned_text


sample_text = "Breaking news: The government has just announced a new policy."
cleaned = clean_text(sample_text)
print(f"Original: {sample_text}")
print(f"Cleaned: {cleaned}")
