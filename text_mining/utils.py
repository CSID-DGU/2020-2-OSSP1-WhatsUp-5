from konlpy.tag import Mecab
import pandas as pd
from tqdm import tqdm
import pandas as pd
from jamo import h2j, j2hcj


def get_disease_in_keywords(result_df, disease_df):
    '''
    :param result_df: LDA result dataframe
    :param disease_df: disease list dataframe
    :return: disease words in LDA model topics
    '''
    dis = disease_df['disease'].tolist()
    dis = set(dis)

    # result dataframe에서 keyword만 추출
    keywords_list = []
    for keywords in result_df['Keywords']:
        keywords = keywords.split(',')
        for keyword in keywords:
            if keyword.strip() in dis:
                keywords_list.append(keyword.strip())
    keywords_list = list(set(keywords_list))

    # make dict
    dic = {}
    for disease_keyword in keywords_list:
        dic[disease_keyword] = get_jongsung_TF(disease_keyword)

    # for return
    df = pd.DataFrame()
    for key, value in dic.items():
        df = df.append(
            pd.Series([key, value]), ignore_index=True)
    df.columns=['disease', 'jongsung']

    return df


# 종성 확인
def get_jongsung_TF(sample_text):
    sample_text_list = list(sample_text)
    last_word = sample_text_list[-1]
    last_word_jamo_list = list(j2hcj(h2j(last_word)))
    last_jamo = last_word_jamo_list[-1]
    jongsung_TF = "T"
    if last_jamo in (
    'ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅘ', 'ㅚ', 'ㅙ', 'ㅝ', 'ㅞ', 'ㅢ', 'ㅐ', 'ㅔ', 'ㅟ', 'ㅖ', 'ㅒ', '2', '4',
    '5', '9'):
        jongsung_TF = "F"

    return jongsung_TF


def get_stopword(path="data/stopword.txt"):
    '''
    path : Stop Word path
    return : set

    Generate a set of stop words by reading texts in the path
    '''
    f = open(path, encoding="utf-8")
    stopword = []
    lines = f.readlines()
    for line in lines:
        stopword.append(line.split()[0])
    stopword = set(stopword)

    f.close()
    return stopword


def df_to_dic(df):
    dic = {}
    for idx in range(len(df)):
        disease = df.loc[idx, 'disease']
        syn_list = df.loc[idx, 'syn'].split(',')
        for syn in syn_list:
            dic[syn] = disease
    return dic


def to_syn(noun, dic):
    syn = dic.get(noun)
    if syn:
        return syn
    return noun


def preprocess(nouns, stopword, dic):
    '''
    nouns : list type, list of words
    stopword : set type, stopword
    dic : dict type, for synonym processing
    return : list type, nouns after preprocess
    '''
    preprocess_nouns = []
    additional_word = ('암') # 사용하는 단어
    for noun in nouns:
        if (noun in additional_word) or (len(noun) > 1 and (noun not in stopword)):
            noun = to_syn(noun, dic)
            preprocess_nouns.append(noun)
    return preprocess_nouns


def get_nouns_from_csv(data, stopword, synonym):
    '''
    requirement : pandas, mecab
    data : dataframe type, content of article
    stopword : set type, stopword
    synonym : dict type, use in function preprocess
    return : word_list

    입력받은 path에서 csv 파일을 읽어와 dataframe에 저장
    'text' col을 차례대로 Mecab을 이용해 형태소 분석하여 명사만 word_list에 추가
    '''
    mecab = Mecab()  # 형태소분석기 Mecab(사용자정의사전 추가)
    word_list = []

    for idx in tqdm(range(len(data))):
        try:
            nouns = mecab.nouns(data.loc[idx, 'content'])
            nouns = preprocess(nouns=nouns, stopword=stopword, dic=synonym)
            word_list.append(nouns)
        except Exception as e:
            continue
    print("\nNoun Extraction Complete")

    return word_list