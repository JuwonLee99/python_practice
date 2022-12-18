# for문
# print('대기번호 : 1')
# print('대기번호 : 2')
# print('대기번호 : 3')


# #range 이용
# for waiting_no in [0, 1, 2, 3, 4]:
#     print('대기번호 : {}' .format(waiting_no))
# print()
# for waiting_no in range(5):
#     print('대기번호 : {}' .format(waiting_no))


# starbucks = ['하하', '유재석', '박명수']
# for customer in starbucks :
#     print('{}, 커피가 준비되었습니다.' .format(customer))





# while문
# customer = '하하'
# index = 5
# while index >= 1 :
#     print('{0}, 커피가 준비되었습니다. {1}번 남았습니다.' .format(customer, index))
#     index -= 1
#     if index == 0:
#         print('커피는 폐기처분 되었습니다.')

#무한루프, 컨트롤 c로 빠져나올수있음
# customer = '하하'
# index =1
# while True:
#     print('{0}, 커피가 준비되었습니다. 호출 {1}회' .format(customer,index))
#     index += 1


customer = '하하'
person = 'Unknown'
while person != customer:
    print('{0}, 커피가 준비되었습니다.' .format(customer))
    person = input('이름이 어떻게 되세요?')
