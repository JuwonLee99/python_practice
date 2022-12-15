# #[1] 0부터 9까지 출력하는 for 반복문을 구현하시오
# for i in range(10):
#     print(i)



#아래 중 틀린 곳을 찾아보시오
# # [1]
# for i in range(10):
#         print( i )
#
# # [2] for문 한줄쓰기 가능
# for i in range(10): print( i )
#
# # [3] 들여쓰기 해줘야함
# for i in range(10):
# print( i )



#0     1       2       3       4       5       6       7       8       9 출력해보기
#end='' : 현재 속한 출력물을 그 다음 출력값과 이어지게함
# \t : 탭을 의미, \n : 줄바꾸기
# for i in range(10):
#     print(i, end='\t')
# print('\n')
# for a in range(10):
#     print(a, end='')

# 0부터 9까지 숫자를 가로출력 했을 때 마지막 콤마를 없애시오.
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# #[1]
# for i in range(10):
#     print(i,end=',' )
# print('\b')
#
# #[2]
# n=0
# for i in range(10):
#     if n < 9:
#         print(i, end=',')
#     else:
#         print(i)
#     n+=1



# for 반복문을 사용해서 4부터 21까지의 홀수들의 합을 구하는 코드를 구현하시오.
#range 함수 - range(A): 0~A-1까지의 정수 범위를 반환 / range(A, B): A부터 B-1까지의 정수 범위를 반환 / range(A, B, C): A부터 C숫자의 간격으로 B-1까지 반환

# #[1]
# n = 0
# for i in range(4, 22):
#     if i % 2 != 0:
#         n+=i
#
# print(n)
#
#
#
# #[2]
# first =4
# last =21
# sum_odd = 0
# for i in range(first, last+1):
#     print(i, end='\t')
#     if i % 2 != 0:
#         sum_odd += i
# print()
# print(sum_odd)





# 1부터 100까지의 수에서 짝수들만 출력하는 코드를 구현하시오.

# # [1] : if 조건문을 이용 --> 홀짝 판단 후 처리.
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i, end='\t')
#
# print()
# # [2] : range() 함수의 step(간격) 옵션 값을 이용하여 처리.
# for i in range(2,101,2):
#     print(i, end='\t')




#리스트, len() 리스트의 요소 갯수
#
# lst = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator']
# for i in range(len(lst)):
#     print(lst[i], end='\t\t')
#
# print('총', len(lst), '개 요소')



# 리스트 요소의 값을 반복문을 사용하여 거꾸로 출력시키시오.
# lst = ['dog', 'hippo', 'elephant', 'lion', 'tiger', 'alligator']
# for i in lst[::-1]:
#     print(i, end='\t\t')
# print()
# print(type(i))


# lst = [1, 2, 3, 4, 5]
# for i in lst[::-1]:
#     print(i, end='\t\t')
# print()
# print(type(i))







#이중반복문
# for 반복문을 사용해서 구구단 전체(2단~9단)를 출력하는 코드를 구현하시오.

for i in range(2, 10):
    for j in range(1,10):
        print(i,'x',j,'=',i*j)
    print('-'*10)