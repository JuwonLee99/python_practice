# #리스트 인덱싱
# a=[1,2,3]
# print(a[0], a[1], a[2])
# print(a[-1]) #a의 마지막 요소를 의미
#
# #이중 인덱싱
# b=[1,2,3,['a', 'b', 'c']]
# print(b[0])
# print(b[3])
# print(b[3][0])
# print(b[-1][0])
# print(b[3][-1])
#
# #삼중 인덱싱
# c=[1, 2, 3, ['a','b',['life', 'is']]]
# print(c[-1])
# print(c[-1][0])
# print(c[-1][-1][0])




# #리스트 슬라이싱
# a=[1, 2, 3, 4, 5]
# print(a[0:2])
# print(a[2:-1])
# print(a[2:])
# print(a[:2])
#
# #중첩 리스트 슬라이싱
# b = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
# print(b[2:5])
# print(b[3][:2])



# #리스트 연산하기
# #더하기
# a=[1, 2, 3]
# b=[4, 5, 6]
# print(a+b)
#
# #반복하기
# print(a*3)
#
# #리스트 길이 구하기
# print(len(a))


# #리스트 수정과 삭제
# #값 수정하기
# a=[1, 2, 3]
# a[2]=4
# print(a)
#
# #del을 이용하여 값 삭제하기, del 객체
# del a[1]
# print(a)
#
# #슬라이싱을 사용하여 여러개 한꺼번에 삭제
# a=[1, 2, 3, 4, 5]
# del a[2:]
# print(a)




#리스트 관련 함수들

#리스트에 요소 추가 append
# a=[1, 2, 3]
# a.append(4)
# print(a)
#
# a.append([5, 6])
# print(a)
#
# a.append(5, 6) #오류
# print(a)


#리스트 정렬 sort
# a=[1, 4, 3, 2]
# a.sort()
# print(a)
#
# b=['a', 'c', 'b']
# b.sort()
# print(b)


#리스트 뒤집기 reverse
# a=['a','c','b']
# a.reverse()
# print(a)

#인덱스 반환 index
# a=[1, 2, 3]
# print(a.index(3))
# print(a.index(1))


#인덱스 요소 삽입 insert(위치, 삽입할 요소)
# a=[1, 2, 3]
# a.insert(0,4)
# print(a)
# a.insert(-1,5)
# print(a)
# print(a[-1])


#리스트 요소 제거 remove(x) : 리스트에서 첫번째로 나오는 x를 삭제
# a= [1, 2, 3, 4, 5, 3, 6,3]
# a.remove(3)
# print(a)
# a.remove(3)
# print(a)



#리스트 요소 끄집어내기 pop, 리스트의 마지막 요소 리턴하고 삭제
# a=[1, 2, 3]
# print(a.pop())
# print(a)

# #리스트에 포함된 요소 개수 세기 count
# a= [1, 2, 3,1]
# print(a.count(1))


#리스트 확장 extend(x), x에는 리스트만 올 수 있으면 원래 리스트에 x리스트를 더하게 된다
# a=[1,2,3]
# a.extend([4,5])
# print(a)
#
# b=[6,7]
# a.extend(b)
# print(a)