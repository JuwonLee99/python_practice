# 패키지 : 여러 모듈들을 모아놓은 집합, 보통 하나의 폴더 안에 여러 모듈 파일들로 구성됨

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# ---------------------------------------------------------------------

# 클래스 직접 import는 불가
# import travel.thailand.ThailandPackage (X))

# from - import를 통해서는 가능
# from travel.thailand import ThailandPackage # travel.thailand 모듈에서 ThailandPackage 클래스 가져오기 
# trip_to = ThailandPackage # travel.thiland. 는 생략
# trip_to.detail()

# ---------------------------------------------------------------------

# from travel import vietnam # 트래블 패키지에서 베트남 모듈 가져오기
# # 모듈명인 vietnam.을 이용하여 모듈 내 클래스에 접근
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# ---------------------------------------------------------------------

# *을 통해 불러와보기
# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()
# 오류
# 원인 : 패키지에 있는 모든 것을 가져다 쓰겠다를 의미하지만 실제로는 패키지를 만든 사함이 공개 범위를 설정해줄 수 있음
# 패키지에 포함된 모듈 중에서 import 되기를 원하는 것만 공개하고 나머지를 비공개로 둘 수 있음
# __init__ 파일 수정 

# 패키지, 모듈의 경로 확인
import inspect
import random
from travel import *
# print(inspect.getfile(thailand)) # thailand 모듈 위치
print(inspect.getfile(random)) # 랜덤 모듈의 위치

# 라이브러리 lib 폴더로 travel 패키지 복사 후 실행되는지 확인



