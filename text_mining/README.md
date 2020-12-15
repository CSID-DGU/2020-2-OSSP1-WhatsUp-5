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

### Data
헬스조선의 기사를 바탕으로 트렌드를 분석하여 키워드를 추출하였다. health_chosun_crawling.py의 get_article() 함수를 활용하여 데이터를 수집할 수 있다.
이슈가 되고있는 질병을 파악하기 위해 LDA 토픽 모델링을 사용하므로 특정 기간 내의 기사만 수집할 수 있으며 특정 키워드와 관련된 기사만 수집하는 것도 가능하다.
Trend_Analysis.ipynb 파일에서는 사전에 크롤링한 데이터를 활용하여 결과를 보였다.


### Preprocessing
토픽 모델링을 진행하기 위해선 주어진 string의 형태소를 분석하여 명사만을 추출해야한다. 형태소 분석을 위한 라이브러리로는 mecab, khaiii, OKT, 꼬꼬마 등이 존재하는데
이 중 mecab의 형태소 분석 속도가 가장 빠르고, 성능도 좋은 편이므로 mecab을 형태소 분석기로 사용하고 사용자 사전을 추가하였다. 사용자 정의 사전 추가 과정은  text_mining/mecab/ 에 있다.


### LDA 토픽 모델링
#### Mallet Coherence Score
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

>Gensim Coherence Score
```
# Compute Coherence Score
coherence_model_ldamallet = CoherenceModel(model=model, texts=texts, dictionary=id2word, coherence='c_v')
coherence_ldamallet = coherence_model_ldamallet.get_coherence()
print('\nCoherence Score: ', coherence_ldamallet)
```

Coherence Score:  0.5399192464467387


Coherence는 기사가 얼마나 잘 clustering 되었는지 주제의 일관성을 나타내는 지표이다. Gensim 내장 LDA model에서 Mallet의 LDA 모델을 활용함으로
Coherence Scroe를 0.05 이상 향상되었다.

### LDA MAP
![LDAMAP](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/img/ldamap.png "ldamap")
![LDA_INFO](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/img/lda_info.png "lda_info")
![DISEASE_LIST](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/img/disease_list.png "disease_list")


[LDA_MAP](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/output/LDA_Map.html "lda")

