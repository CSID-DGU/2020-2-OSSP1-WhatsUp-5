### GPT2를 이용한 기사생성

**필요한 환경-requirements.txt**

1. gluonnlp == 0.9.1
2. mxnet == 1.6.0
3. sentencepiece >= 0.1.85
4. torch == 1.5.0
5. transformers == 2.11.0


- GPT2_finetuning.ipnynb
: 허깅페이스의 transformers 라이브러리와 SKT KoGPT2 모델 기반으로 작성된 코드 + 소설 "운수 좋은 날" 데이터 전처리 후 학습
