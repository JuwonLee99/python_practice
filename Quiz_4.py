# 당신의 학교에서는 파이썬 코딩대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자 중에 추첨을 통해 1명은 치킨 3명은 커피쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건 2 : 댓글 내용과 상관없이 무작위 추첨하되 중복 불가
# 조건 3 : random 모듈의 shuffle 과 sample을 활용


#작성
# from random import shuffle, sample

# comment = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# shuffle(comment)
# luck = sample(comment, 4)
# print('-- 당첨자 발표 --')
# print('치킨 당첨자 : %d' %int(luck[0]))
# print('커피 당첨자 : ', luck[1:])
# print('-- 축하합니다 --')

#답안
from random import *
users = range(1, 21)
users = list(users)
shuffle(users)
winners = sample(users, 4)
print('-- 당첨자 발표 --')
print('치킨 당첨자 : {}' .format(winners[0]))
print('커피 당첨자 : {}' .format(winners[1:]))
print('-- 축하합니다 --')

