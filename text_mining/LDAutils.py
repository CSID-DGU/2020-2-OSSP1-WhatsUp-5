# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models.wrappers import LdaMallet
from gensim.models.coherencemodel import CoherenceModel
from gensim import similarities

from tqdm import tqdm
import pandas as pd
import numpy as np

# spacy for lemmatization
import spacy

# Plotting tools
from pprint import pprint
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt
#% matplotlib inline

# Enable logging for gensim - optional
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)
import os.path
import re
import glob

import nltk

nltk.download('stopwords')

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

os.environ['MALLET_HOME'] = '/content/mallet-2.0.8'
mallet_path = '/content/mallet-2.0.8/bin/mallet'

#최적의 토픽 수를 찾기 위해 여러 토픽 수로 일관성을 계산하고 비교
def compute_coherence_values(mallet_path, id2word, corpus, texts, limit, start=8, step=2,):
    coherence_values = []
    model_list = []
    topic_cnt = 0

    for num_topics in tqdm(range(start, limit, step)):
        model = gensim.models.wrappers.LdaMallet(mallet_path, corpus=corpus, num_topics=num_topics, id2word=id2word)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=id2word, coherence='c_v')
        coherence_values.append(coherencemodel.get_coherence())

    for idx, value in enumerate(coherence_values[1:]):
        if coherence_values[topic_cnt] < value:
            topic_cnt = idx
        else:
            break

    return model_list, coherence_values, topic_cnt


def show_coherence_graph(start, limit, step, coherence_values, path):
    x = range(start, limit, step)
    plt.plot(x, coherence_values)
    plt.xlabel("Topic Number")
    plt.ylabel("Coherence")
    plt.legend(("coherence_values"), loc='best')
    plt.show()

def save_coherence_graph(start, limit, step, coherence_values, path):
    x = range(start, limit, step)
    plt.plot(x, coherence_values)
    plt.xlabel("Topic Number")
    plt.ylabel("Coherence")
    plt.legend(("coherence_values"), loc='best')
    plt.savefig(path)

#트윗들의 토픽을 확인 (토픽별로)
def format_topics_sentences(ldamodel, corpus, texts):
    sent_topics_df = pd.DataFrame()

    #ldamodel[corpus]: lda_model에 corpus를 넣어 각 토픽 당 확률을 알 수 있음
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:
                wp = ldamodel.show_topic(topic_num,topn=20)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)


# 각 Document의 topic
def format_topics_sentences(ldamodel, corpus, texts):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row in enumerate(ldamodel[corpus]):
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(
                    pd.Series([int(topic_num), round(prop_topic, 4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return (sent_topics_df)


def mallet_to_lda(mallet_model):
    '''
    :param mallet_model: mallet's LDA model
    :return: gensim's LDA model
    change mallet's LDA model to gensim's LDA model.
    To ensure successful visualization in pyLDAvis.
    '''
    model_gensim = gensim.models.LdaModel(
        id2word=mallet_model.id2word, num_topics=mallet_model.num_topics,
        alpha=mallet_model.alpha, eta=0, iterations=1000,
        gamma_threshold=0.001,
        dtype=np.float32
    )
    model_gensim.sync_state()
    model_gensim.state.sstats = mallet_model.wordtopics
    return model_gensim