# 파일입출력의 필요성 : 프로그램이 꺼진 이후에도 데이터를 저장하기 위해서는 파일입출력이 필요, 어떠한 데이터를 프로그램 안에서만 사용하는 것이 아닌 프로그램 외부에 일시적으로 저장을 해두었다가 프로그램을
# 다시 실행시킬 때 다시 불러올 수 있도록하는 역할을 할 수 있다.


# score_file = open('score.txt', 'w', encoding='utf8') # 쓰기 용도, utf8: 한글 적기 위해서 사용해주는게 좋음
# print('수학 : 0', file = score_file)
# print('영어 : 50', file=score_file)
# score_file.close() # 항상 마지막에는 파일을 닫아줘야함


# score_file = open('score.txt', 'a', encoding='utf8') # 이어쓰기 용도
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100')
# score_file.close()


# score_file = open('score.txt', 'r', encoding='utf8') # 읽어오는 용도
# print(score_file.read())
# score_file.close()


# score_file = open('score.txt', 'r', encoding='utf8')
# print(score_file.readline(), end='') # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# score_file.close()


# score_file = open('score.txt', 'r', encoding='utf8') # 몇 줄인지 모를때
# while True :
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()



# score_file = open('score.txt', 'r', encoding='utf8')
# lines = score_file.readlines() # 리스트 형태로 저장
# for line in lines :
#     print(line, end="")
# score_file.close()