# from random import *
# words = ['apple', 'banana', 'orange']
# n = randint(0,2)
# quiz = words[n]

# print('게임을 시작합니다.')
# print('-----------------')
# paper = ('_'*len(quiz))
# print(paper)
# while True :
#     ans = input('알파벳을 입력하세요: ')
#     if ans in quiz :
#         paper[quiz.index(ans)] = quiz[quiz.index(ans)]
#         print(paper)
#     elif paper.count('_') == 0 :
#         print("Success")
#         break
#     else :
#         print(paper)
#         continue
# print('-----------------')
# print('게임을 종료합니다.')



from random import * # 랜덤 모듈 import
words = ["apple", "banana", "orange"] # 리스트에 영어 단어 후보를 나열
word = choice(words) # 랜덤으로 단어 중 1개를 선택
print("answer : " + word) # 참고용으로 정답 출력 (실제 게임에서는 지우기)
letters = "" # 플레이어가 지금까지 입력한 알파벳들 저장

while True:
    ans = input('Input letter > ')
