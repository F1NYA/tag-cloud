import nltk
from nltk import word_tokenize, SnowballStemmer
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer

nltk.download('stopwords')
LANGUAGE = 'russian'

__morph = MorphAnalyzer()
__stop_words = stopwords.words(LANGUAGE)

def to_normal_form(word):
    return __morph.parse(word)[0].normal_form


def process_messages(messages):
    print('Processing messages ...')
    processed_messages = []
    for message in messages:
        tokens = word_tokenize(message.lower())
        processed_messages.extend(
            [to_normal_form(word) for word in tokens if word.isalpha() and word not in __stop_words]
        )
    print(processed_messages)
    return processed_messages
