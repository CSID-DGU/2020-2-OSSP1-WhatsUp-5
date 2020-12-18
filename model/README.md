# GPT2를 이용한 기사생성
> 개발환경

: 구글 코랩(Colaboratory), 공유 드라이브

**requirements.txt : 환경설정**
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


## koGPT2 미세 조정 학습(fine-tuning)
**trainNews.ipynb**:
koGPT2를 사전모델로 한 미세조정 학습을 하는 파일이다. 학습된 파라미터가 한국어 GPT2의 경우 huggingface에 모델로 등록돼 있지 않아 다음 명령어로 파라미터를 다운로드한다.
```
wget https://github.com/NLP-kr/tensorflow-ml-nlp-tf2/releases/download/v1.0/gpt_ckpt.zip -O gpt_ckpt.zip 
```
gpt_ckpt 폴더가 생성되고 config.json, tf_model.h5, gpt_kor_tokenizer.spice가 다운 받아진다. tf_model.h5 파일은 깃허브에 올릴 수 없기 때문에 해당 폴더에 존재하지 않는 상태이다. 이로써 사전모델과 토크나이저가 다운 받아진다. 학습데이터를 전처리한 후 eda분석을 참고해 적절한 배치 사이즈, 에폭수, MAX_LEN값을 설정하고 학습을 시작한다. 학습이 지속적으로 이어갈 수 있도록 텐서플로우의 checkpoint를 이용했다.

학습한 파일을 저장하는 코드를 실행하면 다음과 같이 드라이브에 폴더가 한개 생성된다.

![스크린샷 2020-12-18 오후 10 14 08](https://user-images.githubusercontent.com/40908279/102618553-5a346500-417e-11eb-9c15-156ef0f96ea9.png)

## 텍스트 생성 
 **generateNews.ipynb**: 학습한 모델로 문장을 생성하는 파일이다. Generate_sent 함수는 아래 그림과 같은 매개변수로 구성되어 있다. 
 
 <img width="700" alt="스크린샷 2020-12-18 오후 10 23 08" src="https://user-images.githubusercontent.com/40908279/102619323-9fa56200-417f-11eb-9cb7-140842e7bff1.png">
top_k는 확률이 높은 순서대로 k번째까지 필터링, top_p는 일정 확률값 이상인 단어에 대해서 필터링을 진행해주는 값이다. Generate_sent 함수를 실행하면 Max_step만큼 반복문을 돌며 토큰을 생성하고 기사(제목)의 끝을 알리는 스페셜 토큰 슬래시 에스</s>가 나오면 문장 생성을 멈춘다.
