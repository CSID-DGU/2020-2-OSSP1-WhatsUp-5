## 개발 환경
- colab
- python 3.6

## 실행 방법
> 필요한 패키지를 설치해주세요. 
```
!pip install pyLDAvis
!pip install selenium
!pip install jamo
!pip install BeautifulSoup4
!apt update
!apt install chromium-chromedriver 
```

> Mecab 설치 (사용자 정의 사전 추가) 
```
!git clone https://github.com/SOMJANG/Mecab-ko-for-Google-Colab.git
cd Mecab-ko-for-Google-Colab
!bash install_mecab-ko_on_colab190912.sh
cd /content/mecab-ko-dic-2.1.1-20180720
cp "/content/drive/My Drive/GitHub/2020-2-OSSP1-WhatsUp-5/text_mining/data/nnp.csv" "./user-dic/nnp.csv"
!bash ./tools/add-userdic.sh
!make install
```

> Java 설치 (Mallet 사용을 위함) 
```
import os       #importing os to set environment variable
def install_java():
  !apt-get install -y openjdk-8-jdk-headless -qq > /dev/null      #install openjdk
  os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"     #set environment variable
  !java -version       #check java version
install_java()
```

> Mallet 설치
```
!wget http://mallet.cs.umass.edu/dist/mallet-2.0.8.zip
!unzip mallet-2.0.8.zip
```

## 설명

LDA Topic Modeling 기법을 활용하여 기사를 분석하여 키워드를 추출한다. 초기에는 빈도수 기반으로 키워드를 분석했다. 그러나 하나의 기사에서 많은 횟수의 특정 키워드가 등장한 것과 여러개의 기사에서 골고루 특정 키워드가 등장한 것을 구분할 수 없는 단점을 해결하기 위하여 LDA 기법을 도입했다. LDA는 특정 토픽에 단어가 존재할 확률과 기사에 특정 토픽이 존재할 확률을 결합한 결합확률로 추정하여 토픽을 추출한다.


### Data
헬스조선의 기사를 바탕으로 트렌드를 분석하여 키워드를 추출하였다. health_chosun_crawling.py의 get_article() 함수를 활용하여 데이터를 수집할 수 있다.
이슈가 되고있는 질병을 파악하기 위해 LDA 토픽 모델링을 사용하므로 특정 기간 내의 기사만 수집할 수 있으며 특정 키워드와 관련된 기사만 수집하는 것도 가능하다.
Trend_Analysis.ipynb 파일에서는 사전에 크롤링한 데이터를 활용하여 결과를 보였다.


### Preprocessing
토픽 모델링을 진행하기 위해선 주어진 string의 형태소를 분석하여 명사만을 추출해야한다. 형태소 분석을 위한 라이브러리로는 mecab, khaiii, OKT, 꼬꼬마 등이 존재하는데
이 중 mecab의 형태소 분석 속도가 가장 빠르고, 성능도 좋은 편이므로 mecab을 형태소 분석기로 사용하고 사용자 사전을 추가하였다. 사용자 정의 사전 추가 과정은  text_mining/mecab/ 에 있다.


### LDA 토픽 모델링
#### - Mallet Coherence Score
<p>

![coherenceScore](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/output/coherence_values.png "Mallet Coherence Score")

키워드를 파악함에 있어서 LDA에서는 적절한 개수의 topic으로 분류할지 정하는 것이 중요하다.
그러나 토픽의 개수를 정하는 방법은 결정적으로 정해져있지 않다. 
따라서 우리는 최소의 topic을 활용하여 기사를 분리하고자 하여 Coherence의 값이 감소하기 전, 최대값을 topic 개수로 하였다.<p>


> Mallet Coherence Score
```
# Compute Coherence Score
coherence_model_ldamallet = CoherenceModel(model=model, texts=texts, dictionary=id2word, coherence='c_v')
coherence_ldamallet = coherence_model_ldamallet.get_coherence()
print('\nCoherence Score: ', coherence_ldamallet)
```

Coherence Score:  0.5862624134508976

> Gensim Coherence Score
```
# Compute Coherence Score
coherence_model_ldamallet = CoherenceModel(model=model, texts=texts, dictionary=id2word, coherence='c_v')
coherence_ldamallet = coherence_model_ldamallet.get_coherence()
print('\nCoherence Score: ', coherence_ldamallet)
```

Coherence Score:  0.5399192464467387


Coherence는 기사가 얼마나 잘 clustering 되었는지 주제의 일관성을 나타내는 지표이다. Gensim 내장 LDA model에서 Mallet의 LDA 모델을 활용함으로
Coherence Scroe를 0.05 이상 향상되었다.

#### - LDA MAP
![LDAMAP](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/img/ldamap.png "ldamap")

[LDA_MAP](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/output/LDA_Map.html "lda") 
<p>토픽 모델링 결과이다. 좌측 Intertopic Distance Map은 클러스터링 된 결과를 차원을 낮추어 보여준 것으로 원이 겹칠 수록 유사한 키워드를 가질 확률이 높은 것이다.
우측 Relevant Terms는 해당 토픽 그룹에서 등장할 확률이 높은 단어를 나타낸다. 모든 기사에서 등장할 수 있는 단어들은 stopword를 추가하여 제거해주었다. 현재, 코로나19가 전세계적으로 이슈를 끌고있으며 해당 토픽은 코로나19 백신 관련한 토픽을 클러스터링한 결과이므로 해당 토픽에서는 코로나19가 등장할 확률이 높은 것을 보인

![LDA_INFO](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/img/lda_info.png "lda_info")
<p>LDA MAP을 통해 시각화 된 정보를 dataframe으로 나타낸 것이다. 해당 토픽에서 등장할 확률이 높은 Keyword와 해당 토픽의 개수, 전체 기사에서 해당 토픽의 비율을 나타낸다.
겨울에 추운 날씨로 인한 혈관의 수축으로 특히 주의해야할 고혈압과 뇌졸중 또한 키워드로 추출된 것을 관찰할 수 있다. 현재 코로나19가 유행하고 있기 때문에 대부분의 토픽들이 코로나19와 연관된 것을 관찰할 수 있다. 그러나 LDA Topic Modeling의 경우, 각 토픽이 얼마나 유사한지 알 수 없어 이에 대한 개선이 있을 경우 토픽 간의 관계를 더욱 잘 파악할 수 있을 것으로 보인다.

![DISEASE_LIST](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/img/disease_list.png "disease_list")
<p>기사 생성 모델에서 input으로 들어갈 질병명이다. LDA 모델링 결과로 출력된 keyword에서 질병명을 추줄하고, 종성을 분석하여 dataframe 형태로 값을 반환하였다. 기사를 생성할 때, .csv 파일을 불러와서 생성해야할 기사의 중심 질병 키워드를 얻을 수 있다.


## 참고 문헌
https://radimrehurek.com/gensim/models/ldamodel.html <p>
http://mallet.cs.umass.edu/ <p>
https://wikidocs.net/30708 <p>
https://colab.research.google.com/github/polsci/colab-gensim-mallet/blob/master/topic-modeling-with-colab-gensim-mallet.ipynb <p>

