# print('Python', 'Java') #띄어쓰기
# print('Python'+'Java') #띄어쓰기 X
# print('Python', 'Java', sep=',') #띄어쓰기 부분에 어떤걸 넣을지 지정가능
# print('Python', 'Java','JavaScript', sep=' vs ')



# print('Python', 'Java', sep=',', end="?") #문장의 끝부분에 들어갈 것, 기본적으로는 줄바꿈이 되었던것
# print('무엇이 더 재밌을까요?')


# # import sys
# # print('Python','Java',file=sys.stdout) #표준 출력
# # print('Python','Java',file=sys.stderr) #표준 에러



# scores = {'수학':0, '영어':50, '코딩':100}
# for subject, score in scores.items():
#     #print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep =':') #8개의 공간을 두고 왼쪽 정렬, 4칸의 공간을 확보하고 오른쪽 정렬



#은행 대기 순번표
# #001, 002, 003 ....
# for num in range(1, 21):
#     print('대기번호 : '+str(num).zfill(3)) #0을 채운다, 3만큼의 공간을 확보하고 숫자를 넣음


#표준 입력
# answer = input('아무 값이나 입력하세요 : ')
answer = 10
print(type(answer))
print('입력하신 값은 '+answer+'입니다.') # 정수형인 경우 문자와 연산할 수 없으므로 str으로 자료형을 변경해줘야함

#사용자 입력을 받게되면 항상 문자열로 저장됨