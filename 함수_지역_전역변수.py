# 지역변수 : 함수 내에서만 사용되는 변수, 함수이 호출될때 생겼다가 끝날때 사라짐
# 전역변수 : 프로그램 모든 공간에서 부를 수 있는 변수

gun = 10 # 전역

def checkpoint(soldiers):
    # gun = 20 # 지역
    global gun # 전역공간에 있는 변수를 내부에서 사용하겠다는 의미
    gun = gun - soldiers
    print('[함수 내] 남은 총 : {0}' .format(gun))


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    return gun # 함수 내에서 바뀐 값을 밖으로 보낼 수 있음

print('전체 총 : {0}' .format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun, 2)
print('남은 총 : {0}' .format(gun))
