<h1>2020-2-OSSP1-WhatsUp-5</h1>
<h2>공개SW프로젝트 5팀 와썹</h2>
### GPT2를 이용한 기사생성

**필요한 환경-requirements.txt**

1. Python >= 3.6
2. PyTorch == 1.5.0
3. MXNet == 1.6.0
4. gluonnlp == 0.9.1
5. sentencepiece >= 0.1.85
6. transformers == 2.11.0


- GPT2_finetuning.ipnynb
: tensorflow를 이용한 허깅페이스의 transformers 라이브러리와 SKT KoGPT2 모델 기반으로 작성된 코드 + 소설 "운수 좋은 날" 데이터 전처리 후 학습
- koGPT2_use.ipnynb
: SKI의 koGPT2를 실행시켜 본 코드, 어떠한 학습도 시키지 않고 "감기는" 이라는 단어로 문장을 생성한 예시

