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

<h3>Mallet Coherence Score</h3><p>

![coherenceScore](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/output/coherence_values.png "Mallet Coherence Score")

키워드를 파악함에 있어서 LDA에서는 적절한 개수의 topic으로 분류할지 정하는 것이 중요하다.
그러나 토픽의 개수를 정하는 방법은 결정적으로 정해져있지 않다. 
따라서 우리는 최소의 topic을 활용하여 기사를 분리하고자 하여 Coherence의 값이 감소하기 전, 최대값을 topic 개수로 하였다.<p>

Coherence는 기사가 얼마나 잘 clustering 되었는지 주제의 일관성을 나타내는 지표이다. Gensim 내장 LDA model에서 Mallet의 LDA 모델을 활용함으로
Coherence Scroe를 0.05 이상 향상시켰다.


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


[LDA_MAP](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/output/LDA_Map.html "lda")

