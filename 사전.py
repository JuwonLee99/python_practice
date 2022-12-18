# 키와 값으로 구성

# cabinet = {3: '유재석', 100: '박명수'}

# #값 접근하기
# print(cabinet[3])
# print(cabinet[100])
# print(cabinet.get(3))

#두 접근법의 차이 / []접근시 없는 키를 입력하면 오류가 나고 프로그램 종료, get을 이용해 접근시 none값을 반환하고 프로그램 지속
# print(cabinet[5])
# print('hi')

# print(cabinet.get(5))
# print(cabinet.get(5, '사용 가능')) #none이 아닌 다른 값 출력가능
# print('hi')


#키 값 확인하기
# print(3 in cabinet) #참이면 True, 거짓이면 Flase
# print(5 in cabinet)


#문자열 키도 가능
cabinet = {'A-3': '유재석','B-100':'박명수'}
print(cabinet['A-3'])
print(cabinet['B-100'])

#요소 추가하기
print(cabinet)
cabinet['A-3'] = '김종국'
cabinet['c-20'] = '이광수'
print(cabinet)


#키 삭제
del cabinet['A-3']
print(cabinet)


#키만 출력
print(cabinet.keys())

#value만 출력
print(cabinet.values())

#둘다 출력
print(cabinet.items())


#비우기
print(cabinet.clear())
