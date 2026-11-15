import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import wordpunct_tokenize


nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def clean(text):

    text = text.lower()
    text = " ".join(text.split())
    text = re.sub(r'[^a-z\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text


def tokenization(text):
    return wordpunct_tokenize(text)

def removeStopWords(text):
    return [
        word for word in text
        if word not in stop_words
    ]

def stemming(tokens):
    return [
        stemmer.stem(word)
        for word in tokens
        ]

def lemmetization(text):
    return [
        lemmatizer.lemmatize(word)
        for word in text
    ]


text = input("Enter Text : ")
print("\nOriginial Text : ", text)

cleaned = clean(text)
print("\nCleaned Version : ",cleaned)

tokenized = tokenization(cleaned)
print("\nTokenization : ",tokenized)

removedStopWords = removeStopWords(tokenized)
print("\nRemoved Stop Words : ",removedStopWords)

stemmed = stemming(removedStopWords)
print("\nStemmed Text: ",stemmed)

lemmetized = lemmetization(removedStopWords)
print("\nLemmetized : ",lemmetized)


