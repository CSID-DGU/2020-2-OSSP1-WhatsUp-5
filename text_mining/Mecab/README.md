# 사용자 사전 추가된 Mecab
- 크롤링을 통해 수집한 질병명과 동의어, 기타기관명을 수집했습니다.
- 수집한 데이터를 Mecab 사용자 사전에 추가하였습니다. 

코랩에서 사용은 아래 링크 과정대로 진행하였습니다.

https://somjang.tistory.com/entry/Google-Colab%EC%97%90%EC%84%9C-Mecab-koMecab-ko-dic-%EC%89%BD%EA%B2%8C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

주피터 노트북을 참고하면 아래 과정을 쉽게 익힐 수 있습니다.
(1) 구글 드라이브로 data/nnp.csv 파일을 옮깁니다. 
(2) colab에 Mecab를 설치합니다. 
(3) 드라이브로 옮긴 nnp.csv 파일을 /content/mecab-ko-dic-2.1.1-20180720/user-dic/nnp.csv로 파일을 복사합니다.
(4) bash를 통해 컴파일 후 설치합니다.
(5) from konlpy.tag import Mecab를 통해 사용자 정의 사전이 추가된 Mecab를 사용할 수 있습니다.

