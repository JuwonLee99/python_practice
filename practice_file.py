# 프로그램에서 사용하고 있는 데이터를 파일 형태로 저장해주는 것
# 파일을 통해 코드에서 데이터를 사용할 수 있음
# 피클에 파이썬의 모든 객체를 저장할 수 있음, 파이썬 내장 모듈


import pickle
# profile_file = open('profile.pickle', 'wb') # wb : 쓰기 + 바이너리 타입(피클 사용시 필수)
# profile = {'이름':'박명수', '나이':30, '취미':['축구', '골프', '코딩']}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()


profile_file = open('profile.pickle', 'rb') # 읽기
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close() 
# 가지고 있는 데이터(profile)를 피클을 이용하여 파일(profile.pickle)에 저장하고 파일에 있는 내용을 load를 통해 불러와서 변수(profile)에 저장하여 계속 사용할 수 있게끔 도와주는 유용한 라이브러리