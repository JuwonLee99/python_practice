# 변수 할당하기
# a=100
# b=3.14
# c='k'
# d='Hello World'
#
# print('a변수의 값은?', a)
# print('b변수의 값은?', b)
# print(a, b,c,d)

# == 연산자 실습 / 데이터의 값이 같은지 확인할 때 사용
# a= [1, 2, 3, 4, 5]
# b=a
# c=[1, 2, 3, 4, 5, 6]
#
# print(a==b)
# print(a==c)
# print(b==c)

#다중 할당
# a=b=c=d=e=100, 200
# print(a,b,c,d,e)
# print(type(a))
#(100, 200), type은 tuple / list와의 차이점 : list는 [] / tuple은 ()

#다중 할당시 여러개의 값을 여러 개의 변수에 각각 저장시키는 코드를 한줄로 구현하시오
# a,b,c,d=100, 3.14, 'k', 'korea'
# t=100,3.14,'k','korea'
# print(a,b,c,d)
# print(t)

#쌍따옴표, 홀따옴표가 출력되도록 코드를 작성
#쌍따옴표 출력
# sample_1 = '나는 엄마에게 말했다. "더 이상 카레는 먹기 싫어요!"라고...'
# print(sample_1)
# #홀따옴표 출력
# sample_2 = '나는 엄마에게 말했다. "더 이상 \'카레\'는 먹기 싫어요!"라고...'
# print(sample_2)
#
# sample_3 = "나는 엄마에게 말했다. \"더 이상 '카레'는 먹기 싫어요!\"라고..."
# print(sample_3)

#id는 무엇을 출력하는가 / 출력값이 다른 이유는 무엇인가 / 입력받은 객체의 주소값 반화, 한번 정해지면 변하지 않음
# a='붕어빵'
# print(a, id(a))
#
# b=a
# print(b, id(b))
#
# a='잉어빵'
# print(a, id(a))

#is 연산자 / ==와같이 변수에 들어있는 데이터 값을 비교하는 것이 아닌, 같은 객체를 가리키는지를 비교

# a=[1, 2, 3 ,4 ,5]
# b=a
# c=[1, 2, 3, 4, 5]
#
# print(a is b, id(a), id(b))
# print(a is c, id(a), id(c))
# print(b is c, id(b), id(c))

# a='붕어빵'
# b=a
# print(id(a), id(b), id('붕어빵'))
# c='붕어빵'
#
# print(id(a), id(b), id(c), id('붕어빵'))


#숫자
# a =101
# b=100 +1
# print(a is b) #T
# print(a==b) #T
#
# #문자열
# c= 'korea'
# d= 'korea'
# print(c is d)#T
# print(c==d)#T
#
# #리스트
# e = [1, 2, 3, 4, 5]
# f = [1, 2, 3, 4, 5]
# print(e is f) #F
# print(e==f)#T

#리스트는 변수 할때마다 새롭게 저장됨

#is 예제 1 (강의 확인하기)
# a = "korea"
# print( '[1]', a, id(a) )
#
# b = "korea"
# print( '[2]', b, id(b) )
# print( 'a is b = ', a is b ) #T
#
# b += "!"  #--- korea! --;;
# print( '[3]', b, id(b) )
# print( 'a is b = ', a is b )  #F
#
# # korea!
# c = b[ :-1 ]
# print( '[4]', c, id(c) )
# print( 'a is c = ', a is c ) #F


#is 예제 2 (강의 확인)
# t = 'korea'
# print(t, id(t), '-', t[:1], id(t[:1]), '-', t[:2], id(t[:2]), '-', t[:], id(t[:]), t[:4])
#
# print( '-' * 140 )
# print( 't is t[:] = ', t is t[:] ) #T
# print( 't is t[:1] = ', t is t[:1] ) #F
# print( 't[:1] is t[:2] = ', t[:1] is t[:2] )#F
# print( 't[:] is t[:5] = ', t[:] is t[:5] )#T
# #내부에서 조작하는거는 값만 같으면 같은 주소에 할당되어 있음


# #변수 값 교환 swap
# a= 100
# b= 200
# print('교환전', a, b)
#
# # #temp 이용하여 교환
# # temp = a
# # a=b
# # b=temp
# # print('교환후', a, b)
#
# #tmep 사용하지 않고 교환
# a,b=b,a
# print('교환후', a, b)

#자료형: 자료형 또는 데이터 타입이라고 한다. /파이썬에서 자주 쓰이는 타입 : 정수, 실수, 문자열, 리스트, 튜플, 집합, 딕셔너리 / 확인 type()
# a = 100
# print(a, type(a))
#
# b=3.14
# print(b, type(b))
#
# c='korea'
# print(c, type(c))
#
# d='010-1234-5678'
# print(d, type(d))
#
# lst=[1, 2, 3, 4, 5, 500, 500]
# print(lst, type(lst))
#
# tpl=(1, 2, 3, 4, 5)
# print(tpl, type(tpl))
#
# s ={1, 2, 3, 4, 5, 500, 500}
# print(s, type(s))
#
# dic = {'a':97 , 'b':98}
# print(dic, type(dic))



# a = ( 1, 2, 3, 4, 5 )
# print( '[1-1] a 변수값의 자료형 : ', a, type(a) )
# b = 1, 2, 3, 4, 5, 6, 7, 8, 9
# print( '[1-2] b 변수값의 자료형 : ', b, type(b) )


#아스키코드 : 컴퓨터는 0과 1로만 정보를 처리하기 때문에 문자 또한 숫자로 기억하고 있음, 이때 문자를 숫자로 표현할때 아스키 규약에 따라 붙여지게됨
#A > 65 이후부터 1씩 증가
#a > 97 이후부터 1씩 증가
#숫자 0 > 48 이후부터 1씩 증가
#엔터 > 13
#아스키코드 0번 > NULL

#ord()로 아스키코드 출력
# print('A', type('A'))
# print(ord('A'))
#
# #아스키코드를 입력받아 문자로 출력 chr() 이용
# a= input('숫자를 입력하면 해당하는 문자를 출력합니다 =')
# #입력받은 숫자의 자료형 str
# a=int(a)
# chr_ = chr(a)
# print('당신이 입력한 숫자의 문자는:', chr_)
# print(f'당신이 입력한 숫자의 문자는 {chr_}입니다.')
# print(type(chr_))





#연산자
#산술 연산자 + - * / // ** %
#관계 연산자 > < >=(크거나 같다) <=(작거나 같다) == !=(같지 않다)
#논리 연산자 and(양쪽 다 참인 경우에만 참) or(한쪽만 참이면 참) not(참이면 거짓으로 거짓이면 참으로)
#부울 연산자 True, False 값으로 출력

# print(10+10)
# print(10-5)
# print(10*10)
# print(10/10) #왜 1이 아니고 1.0인가
# print(3**2, 3**3)
# print(14%3)

# a=True
# b=False
# print(a and b)
# print(a or b)
# print(a, not(a))


# if a or b:
#     print('True')
# else:
#     print('False')


# a=100
# a=a*2
# print(a)
#
# b=200
# b*=2 #b*2=b
# print(b)


#in 멤버쉽 연산자
# lst= [1, 2, 3, 4, 5]
# a=100 in lst
# print(a)
#
# tpl=1, 2, 3, 4
# print(tpl, type(tpl))
# b = 4 in tpl
# print(b)


# print(bool(1))
# print(bool(0))
# print(bool(-1)) #??
# print(bool(None))

#None 은 말 그대로 아무것도 없다는 뜻으로 이 자체가 하나의 타입이 된다 NoneType, 아무것도 없기때문에 bool 연산자로 출력하면 할상 거짓을 출력
# a= None
# print(a, type(a))
# print(bool(a))
# #값이 들어가 있으면 참이 출력됨 / 0 과 None, 비어있는 변수는 거짓
# b=12312312
# print(bool(b))
