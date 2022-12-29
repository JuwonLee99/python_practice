# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# 내장함수 
# input()
# language = input('무슨 언어를 좋아하세요? ')
# print('{0}은 아주 좋은 언어입니다!'.format(language))

# dir() : 객체를 넘겼을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 알려주는 목적으로 사용
# print(dir())
# import random
# print(dir())
# import pickle
# print(dir())
# # 전달값 넘기지 않으면 현재 소스코드 범위 내에서 사용 가능한 모듈 또는 객체가 출력됨

# print(dir(random)) # random 모듈 내에서 사용 가능한 모든 것들이 출력

# lst = [1, 2, 3]
# print(dir(lst)) # 리스트에서 사용가능한 변수와 함수 목록 확인 가능

# name = 'Jim'
# print(dir(name)) # 문자열에서 사용가능한 기능들 확인 가능

# 더 자세한 내용은 list of python builtins 검색을 통한 파이썬 공식 홈페이지에서 확인할 수 있음

# -----------------------------------------------------------------------------

# 외장 함수 list of python modules

# import glob # glob : 어떤 경로 내의 폴더 또는 파일의 목록을 조회할 때 사용
# print(glob.glob('*.py')) # 확장자가 py 인 모든 파일 

# -----------------------------------------------------------------------------

# import os
# print(os.getcwd()) # 현재 디렉토리

# import os # 주어진 경로에 해당하는 폴더 또는 파일이 존재하는지 여부를 알려주는 os.path.exists() 함수를 통해 새로운 폴더를 생성
# folder = 'sample_dir'
# if os.path.exists(folder):
#     print('이미 존재하는 폴더입니다.')
#     os.rmdir(folder)
#     print(folder, '폴더를 삭제하였습니다.')
# else:
#     os.makedirs(folder)
#     print(folder, '폴더를 생성하였습니다.')


# import os
# print(os.listdir()) # glob() 함수와 비슷하게 현재 작업 디렉토리 내의 폴더와 파일 목록을 출력

# -----------------------------------------------------------------------------
# 시간 관련 함수를 제공하는 time 모듈

# import time
# print(time.localtime())
# # strftime() 함수를 통해 사용자가 원하는 문자열 형태로 시간 정보 출력 가능
# print(time.strftime('%Y-%m-%d %H:%M:%S')) # 연-월-일 시:분:초

# -----------------------------------------------------------------------------
# time 과 비슷한 datetime 모듈
# import datetime
# print('오늘 날짜는', datetime.date.today())

# timedelta() 함수 : 두 날짜 사이의 간격을 쉽게 계산할 수 있음
import datetime
today = datetime.date.today()
td = datetime.timedelta(days = 100)
print('우리가 만난지 100일은', today + td)