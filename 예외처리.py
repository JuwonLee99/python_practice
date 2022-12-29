# 예외 처리 : 에러 상황을 처리하는 것

# ----------------------------------------------------------------
# print('나누기 전용 계산기입니다.')
# num1 = int(input('첫 번째 숫자를 입력하세요 : '))
# num2 = int(input('두 번째 숫자를 입력하세요 : '))
# print('{0} / {1} = {2}'.format(num1, num2, int(num1/num2)))
# ----------------------------------------------------------------

# 예외 처리 형태
# try :
#     실행 명령문1
#     실행 명령문2

# except 에러 종류1:
#     예외처리 명령문1
#     예외처리 명령문2

# except 에러 종류2:
#     예외처리 명령문1
#     예외처리 명령문2

try :
    print('나누기 전용 계산기입니다.')
    nums = []
    nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
    nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
    # nums.append(int(nums[0] / nums[1])) # 계산 결과를 리스트에 추가
    print('{0} / {1} = {2}'.format(nums[0], nums[1], nums[2]))

except ValueError :
    print('에러! 잘못된 값을 입력하였습니다.')

except ZeroDivisionError as err: # 에러의 종류에 따라 쉽게 알아볼 수 있는 메세지가 제공되는 경우 코드에서 별도로 에러 메세지 정의 없이 간편한 예외처리 가능
    print(err)

except Exception as err: # 정의되지 않은 모든 에러에 대한 처리 가능
    print('알 수 없는 에러가 발생하였습니다.')
    print(err)
