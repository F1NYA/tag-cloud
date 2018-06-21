from sklearn.feature_extraction.text import TfidfVectorizer


def create_vectorizer():
    return TfidfVectorizer()

# dd
def vectorize(tokenized_messages, vectorizer):
    print('Vectorizing ...')
    return vectorizer.fit_transform([word for word in tokenized_messages])
