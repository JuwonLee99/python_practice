class BigNumberError(Exception): # 에러 클래스를 만들기 위해 Exception 클래스를 상속
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return '[에러코드 001] '+self.msg #에러 메세지 가공

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요: "))
    num2 = int(input("두 번째 숫자를 입력하세요: "))
    if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
        raise BigNumberError('입력값 : {0}, {1}'.format(num1, num2)) # 자세한 에러 메세지
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err: # 사용자 정의 예외 처리
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)