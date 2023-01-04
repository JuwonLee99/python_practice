class Unit:
    def __init__(self, name, hp, damage): # __init__을 통해 기본적으로 필요한 전달값들을 전달받음
        self.name = name # 멤버변수 name 에 전달값 name 저장, slef.을 통해 클래스 내에서 멤버변수 정의
        self.hp = hp
        self.damage = damage
        print('{0} 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

# Unit 클래스를 통해 만들어진 마린과 탱크를 객체라고 하며, '마린과 탱크는 Unit 클래스의 인스턴스'라고 한다
marine1 = Unit('마린', 40, 5)
marine2 = Unit('마린', 40, 5)
tank = Unit('탱크', 150, 35)



# __init__ : 클래스로 부터 만들어지는 객체, 
# 멤버변수: 클래스 내부에서 정의된 변수

# 레이스 : 공중 유닛, 비행기, 클로킹(상대에게 보이지 않음)
wraith1 = Unit('레이스', 80, 5)
print('유닛 이름 : {0}, 공격력 : {1}'.format(wraith1.name,wraith1.damage)) # .을 통해 멤버변수에 접근할 수 있음/ 클래스 외부에서 멤버변수 사용 가능

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit('빼앗은 레이스', 80 , 5)
wraith2.clocking = True # 레이스2의 멤버변수 clocking 정의
if wraith2.clocking == True :
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 클래스로부터 객체를 만든 다음 그 객체만을 위한 멤버변수의 정의가 필요한 경우에는 외부에서 추가로 변수를 만들어서 사용할 수 있음 (오직 이 객체만을 위한 멤버변수)

