# 2884
# h,m = map(int, input().split())
# if m < 45 :
#     m += 15
#     if h < 1 :
#         print(h+23, m)
#     else :
#         print(h-1, m)
# else :
#     m -= 45
#     print(h, m)


# 2525
# A,B = map(int, input().split())
# C = int(input())
# if B+C < 60 :
#     print(A, B+C)
# else :
#     A = A + (B+C)/60
#     A = int(A)
#     B = (B+C)%60
#     if A == 24:
#         print(0, B)
#     elif A > 24 :
#         print(A-24, B)
#     else:
#         print(int(A), B)


# 2480
# A,B,C = map(int, input().split())
# if A==B==C :
#     print(10000+A*1000)
# elif A != B and  A != C and B != C :
#     print(max(A, B, C)*100)
# else:
#     if A==B and A!=C :
#         print(1000+A*100)
#     elif A==C and A!=B :
#         print(1000+C*100)
#     else :
#         print(1000+B*100)




# 2739
# N = int(input())
# for i in range(9) :
#     print('{0} * {1} = {2}'.format(N,i+1, N*(i+1)))




# 10950
# case = int(input())
# for i in range(case) :
#     A,B=map(int, input().split())
#     print(A+B)



# 8393
# n = int(input())
# for i in range(n) :
#     n += i
# print(n)


# 25304
# X = int(input())
# n = int(input())
# c = 0
# while n > 0 :
#     a,b = map(int, input().split())
#     c += a*b
#     n-=1
# if X == c :
#     print('Yes')
# else :
#     print('No')




# 15552
# import sys
# T = int(input())
# for i in range(T) :
#     a,b=map(int, sys.stdin.readline().split())
#     print(a+b)



# 11021
# T = int(input())
# for i in range(T) :
#     a,b=map(int, input().split())
#     print('Case #{0}: {1}' .format(i+1,a+b))



# 11022
# T = int(input())
# for i in range(T) :
#     a,b = map(int, input().split())
#     print('Case #{0}: {1} + {2} = {3}'.format(i+1,a,b,a+b))



# 2438
# n = int(input())
# for i in range(1,n+1) :
#     print('*'*i)



# 2439
# n = int(input())
# for i in range(1,n+1) :
#     print(' '*(n-i)+'*'*i)


# 10952
# a= 1
# b= 1
# while a != 0 and b != 0:
#     a,b = map(int, input().split())
#     if a == 0 and b == 0 :
#         break
#     else :
#         print(a+b)
        


# 10951 EOF에 대하여
# while True :
#     try:
#         a,b =map(int, input().split())
#         print(a+b)
#     except:
#         break




# 1110
n = int(input())
a = n
i = 0
while True :
    a = (a%10)*10 + (a%10 + a//10)%10
    if a != n:
        i+=1
    else:
        print(i+1)
        break

