#필요 패키지 import
import csv
import re

def SynSearch():
  #데이터
  syn = []
  header = []
  rownum = 0

  #검색 csv file & 동의어 입력
  csv_file = input("읽어올 csv 파일명을 입력하세요 : ")
  data = input("동의어를 입력하세요 : ")
  print(csv_file, "에서 입력하신 동의어에 관련된 질병을 검색합니다.")

  #csv파일 읽어오기
  with open(csv_file, "r", encoding="utf8") as f:
    csv_data = csv.reader(f)
  
    for row in csv_data:
      #맨 윗줄은 필드명
      if rownum == 0:
        header = row
    
      #검색하려는 열(index) 선택(disease_list.csv의 경우 [2]에 동의어가 있다.)
      location = row[2]
      list_row = location.split(' ')
      list_data = data.split(',')

      #해당 동의어를 찾으면 해당 질병을 return
      for i in list_row:
        if i in list_data:
          #질병명 괄호()안의 내용은 제외하고 return
          return re.sub(r'\([^)]*\)', '',row[1])
      rownum += 1

SynSearch()
