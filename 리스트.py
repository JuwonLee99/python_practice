# #리스트 []

# subway = [10, 20, 30]
subway = ['유재석', '박명수', '이광수']

# print(subway.index('유재석')+1)

# #맨 뒤에 요소를 추가 append
# subway.append('하하')
# print(subway)

# #사이에 요소 추가 insert(요소를 넣을 인덱스 값, 요소)
subway.insert(1, '정형돈')
print(subway)

# # #뒤에서 부터 꺼냄
# # print(subway.pop())
# # print(subway.pop())
# # print(subway.pop())
# # print(subway)


# #같은 값이 몇개 있는지 count
# subway.append('유재석')
# print(subway)
# print(subway.count('유재석'))



# #정렬
num_list = [5, 2, 3, 4, 1]
# num_list.sort()
# print(num_list)

# #뒤집기
# num_list.reverse()
# print(num_list)


# #모두 지우기
# num_list.clear()
# print(num_list)


#다양한 자료형 함께 사용
# num_list = [5, 2, 3, 4, 1]
# mix_list = ['유재석', 20, True]
# print(mix_list)


#리스트 확장
num_list.extend(mix_list)
print(num_list)

