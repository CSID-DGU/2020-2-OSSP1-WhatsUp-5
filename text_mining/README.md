
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


[LDA_MAP](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/text_mining/output/LDA_Map.html "lda")

