# GPT2를 이용한 기사생성

### requirements.txt : 환경설정

1. gluonnlp == 0.9.1
2. sentencepiece == 0.1.85
3. transformers == 2.11.0
4. mxnet == 1.6.0

## 학습 데이터의 탐색적 자료 분석(EDA) 
**dataEDA.ipynb**
: 학습할 데이터를 분석하는 파일로, 학습할 csv 폴더에 접근하여 csv 파일의 모든 데이터를 읽어온 후 해당 데이터셋에 대해 중복을 체크하고 아래 세가지에 대해 최대값, 최소값, 평균값, 표준편차, 중간값, 제 1사분위, 제 3사분위 값에 대한 분석을 진행한다.
1.  문장 길이(“Number of characters”): 학습시키는 데이터의 문장 길이
   2. 문장 토큰(“Number of tokens”): 학습시키는 데이터를 버트 토크나이저를 이용해 분석하여 토큰 개수를 구한다.
   3. 문장 단어 개수(“Number of words”): 학습시키는 데이터를 띄어쓰기(‘ ’)기준로 분리해 문장의 단어 개수를 파악한다.

## **trainNews.ipynb**: 기사 학습 

## **generateNews.ipynb**: 텍스트 생성 
