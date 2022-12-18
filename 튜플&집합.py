#튜플 : 리스트와는 다르게 내용 변경이나 추가가 불가능함 하지만 속도가 빠름

# menu = ('돈까스', '치즈까스')
# print(menu[0])
# print(menu[1])

#선언이 빨라짐
# name = '김종국'
# age = 20
# hobby = '코딩'
# print(name, age, hobby)

# name, age, hobby = ('김종국', 20, '코딩')





#집합 : 중복이 안되고 순서가 없음
my_set = {1, 2, 3, 3, 3}
print(my_set)


#교집합
java = {'유재석', '이광수', '김종국'}
python =set(['유재석', '박명수'])
print(java & python)
print(java.intersection(python))


#합집합
print(java | python)
print(java.union(python))


#차집합
print(java - python)
print(java.difference(python))


#추가
python.add('하하')
print(python)


#삭제
java.remove('이광수')
print(java)