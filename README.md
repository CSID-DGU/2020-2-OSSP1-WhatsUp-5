# 2020-2-OSSP1-WhatsUp-5
## 공개SW프로젝트 5팀 와썹
kogpt2를 활용한 의료기사 생성 시스템

## 개발 동기

기사의 작성, 편집, 배포 등 모든 과정에서 컴퓨터를 활용한다.
<h6> \# 로봇 저널리즘 \# 알고리즘 저널리즘 </h6>

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

## 필요한 환경

> requirements.txt
1. gluonnlp == 0.9.1
2. sentencepiece >= 0.1.85
3. transformers == 2.11.0
4. mxnet == 1.6.0
5. kss
6. jamo


> 가중치 파일

가중치 파일을 다운로드 받고, PATH 설정이 필요합니다.










