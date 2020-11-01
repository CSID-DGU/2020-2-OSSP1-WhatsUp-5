# -*- coding: utf-8 -*-

import pandas as pd
from tqdm import tqdm
from collections import Counter
from konlpy.tag import Okt

link = "data/test.csv"
df = pd.read_csv(link, names=["title", "text"], dtype={"title": str, "text": str})

okt = Okt()
dic = {}
for i in tqdm(range(len(df))):
    nouns = okt.nouns(df.loc[i, "text"])
    count = Counter(nouns)
    dic.update(count)

sorted(dic.items(), key=lambda x: x[1], reverse=True)

# Commented out IPython magic to ensure Python compatibility.
from wordcloud import WordCloud 

import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
# %matplotlib inline

import matplotlib
from IPython.display import set_matplotlib_formats
matplotlib.rc('font',family = 'Malgun Gothic')

set_matplotlib_formats('retina')

matplotlib.rc('axes',unicode_minus = False)

font_path = "data/Maplestory Light.ttf"

wordcloud = WordCloud(font_path = font_path, background_color='white', width=1500, height=1000).generate_from_frequencies(dic) 

fig = plt.figure(figsize=(15, 10))
plt.imshow(wordcloud) 
plt.axis('off') 
plt.show()
fig.savefig("output/tf-wordcloud.png")
