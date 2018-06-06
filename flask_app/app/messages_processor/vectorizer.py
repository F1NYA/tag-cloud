from sklearn.feature_extraction.text import TfidfVectorizer


def create_vectorizer():
    return TfidfVectorizer()


def vectorize(tokenized_messages, vectorizer):
    print('Vectorizing ...')
    return vectorizer.fit_transform([word for word in tokenized_messages])
