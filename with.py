# with을 통해 좀 더 쉽게 파일을 열고 닫는 과정을 진행할 수 있음

# import pickle

# with open('profile.pickle', 'rb') as profile_file : # profile_file이라는 변수에 파일을 저장
#     print(pickle.load(profile_file)) # 파일에 대한 데이터 불러와서 출력
# # close 할 필요없이 with문을 탈출하면서 자동으로 닫힘


# 피클을 사용하지않고 일반적인 파일을 쓰고 읽는 것을 with을 통해 해보기
# with open('study.txt','w', encoding='utf8') as study_file:
#     study_file.write('파이썬을 열심히 공부하고 있어요')


with open('study.txt', 'r', encoding='utf8') as study_file:
    print(study_file.read())



