# 2020-2-OSSP1-WhatsUp-5
## 공개SW프로젝트 5팀 와썹
kogpt2를 활용한 의료기사 생성 시스템
<h6> # 로봇 저널리즘 # 알고리즘 저널리즘 </h6>

## 개발 동기

기사의 작성, 편집, 배포 등 모든 과정에서 컴퓨터를 활용한다.

저널리즘 과정을 자동화 함으로써
- 대량의 춤형 기사 작성
- 기계적 반복 작업의 대체
- 주관적 판단의 배제
- 빠른 정보처리

## 개발 목표
1. 웹 크롤링 모듈 구현 - 의료정보, 의료기사 수집 자동화<p>
   
2. [텍스트마이닝 모듈 구현](https://github.com/CSID-DGU/2020-2-OSSP1-WhatsUp-5/blob/master/text_mining/) - 의료기사 데이터를 기반으로 한 Topic Modeling, 시각화
   
3.  [자연어 기반의 text-generator 모듈 구현](https://github.com/CSID-DGU/2020-2-OSSP1-WhatsUp-5/blob/master/model/)

## 개발환경
1. Colab
2. Python 3.6


## 필요한 라이브러리

최종 산출물 파일은 Generate_Article(final).ipynb 입니다. 필요한 라이브러리 및 가중치를 설치한 후, 순차적으로 셀을 실행하면 됩니다.

> requirements.txt

1. gluonnlp == 0.9.1
2. sentencepiece >= 0.1.85
3. transformers == 2.11.0
4. mxnet == 1.6.0
5. kss
6. jamo


> 가중치 파일

가중치 파일을 다운로드 받고, PATH 설정이 필요합니다.

 [checkpoint](https://drive.google.com/drive/folders/1D8s6tbMm-nDLBz3q-BFXCOrg7a-AQNHS?usp=sharing)
 
 2020-2-OSSP1-WhatsUp-5/model/checkpoint 에 maxlen20_loss0.36_acc0.56, psy_loss2.0_acc0.32 폴더를 복사해야합니다.
 
 동국대학교 Gsuite 계정에만 접근 권한이 있습니다.
 



## 전체 시스템 구성도
![시스템 구성도](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/img/system_flow.png "시스템 구성도")

- 기사 제목 학습 데이터 : 97517 문장

- 기사 본문 학습 데이터 : 82576 문장 (길이가 100 이하인 데이터 삭제)


## Preview

> 좋은 예시

<p><p>

![좋은 예시](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/img/ex1.png "좋은 예시")

> 나쁜 예시

<p><p>
   
![나쁜 예시](https://csid-dgu.github.io/2020-2-OSSP1-WhatsUp-5/img/ex2.png "나쁜 예시")

## 기대효과 / 특장점

> 사회적, 경제적 등 다양한 측면의 기대효과
- 로봇 저널리즘 세계 시장 규모 : 2021년 12억 달러에 이를 것으로 전망
- 국내 잠재 시장 규모는 2021년 234억원 수준으로 전망


> 특장점
- 자동화된 시스템으로 방대한 데이터를 빠르게 수집
- 기사를 보다 빠르고, 편리하게 작성/편집
- 사람이 범할 수 있는 실수의 가능성을 크게 줄여줌







