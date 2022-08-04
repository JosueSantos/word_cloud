import re

import nltk
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import word_tokenize

from wordcloud import WordCloud
import matplotlib.pyplot as plt


class CreaterWordCloud:
    def __init__(self):
        nltk.download('stopwords')
        nltk.download('punkt')
        
    def create(self, text, titleText, qtn = 50):
        text = re.sub(r'[^\w\s$]|http\S+','', text).lower()
        text = word_tokenize(text)

        data = []
        data.append((" ").join(text))

        frequency = FreqDist( data )
        word_dict = frequency.keys()

        unique_string = (" ").join(word_dict)

        wordcloud = WordCloud(
            stopwords=['então'] + stopwords.words('portuguese'),
            max_words=qtn,
            background_color="white"
        ).generate( unique_string )

        plt.figure(figsize=(8,6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.title(titleText)
        plt.margins(x=0, y=0)

        return plt
