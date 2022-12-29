# import theater_module

# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# -------------------------------------------------------------------- 

# from - import 를 통해 가져온 모듈은 모듈명과 점(.) 부분은 적어줄 필요없이 모듈 내 함수 이름을 그대로 적으면됨

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# ---------------------------------------------------------------------

# 모듈에 정의된 내용 중 필요한 것만 가져다 써야할 때
# * 대신에 사용하고자 하는 부분만 콤마(,)로 적어주면됨

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_soldier(7) # import 하지 않았으므로 사용 불가

# ---------------------------------------------------------------------

# as를 적용하여 별명 설정
# price_soldier 만 사용할 예정으로 새로운 별명인 price를 붙여 사용하고자 함
from theater_module import price_soldier as price
price(5) # price_soldier()를 호출