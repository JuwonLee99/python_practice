# from - import
# 파이썬에는 유용한 모듈이 많지만 필요 시에는 새로운 모듈을 개발해야할 필요도 있음

# 예제 : 사람 수에 따른 영화표 가격을 계산해 주는 3개 함수의 모듈

# 일반 가격
def price(people):
    print('{0}명 가격은 {1}원 입니다.'.format(people, people*10000))

# 조조 할인 가격
def price_morning(people):
    print('{0}명의 조조 할인 가격은 {1}원 입니다.'.format(people, people*6000))

# 군인 할인 가격
def price_soldier(people):
    print('{0}명의 군인 할인 가격은 {1}원 입니다.'.format(people, people*4000))


# 이 파일은 모듈이 되면 다른 파일에서 가져다가 사용할 수 있음
