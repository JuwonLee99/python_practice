# 상속 : 공통되는 부분은 코드를 중복으로 적지 않고도 재사용할 수 있음
# name과 hp 중복되고 있음, attakunit이 unit 클래스로부터 상속을 받으면 name과 hp를 그대로 사용할 수 있게됨
# class 자식클래스 (상속받을 부모클래스) :
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
# 지상 유닛을 위한 이동 속도를 의미라는 speed를 Unit 클래스에 추가

    def move(self, location): #이동 함수 정의
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'\
            .format(self.name, location, self.speed))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

# 공중유닛 생성
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))


# 다중 상속 (공격 유닛 + 공중 유닛 = 공중 공격 유닛)
# class 자식클래스(부모클래스1, 부모클래스2 ,...) :
# -----------------------------------------------------------------------
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)
# ----------------------------------------------------------------------- 

# Unit 클래스의 move()메소드를 FlyableAttackUnit 클래스 내에서 오버라이딩
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)


# 건물관련 클래스 생성 (이름과 체력이 있고 공격받으면 파괴될 수 있음, 위치)
class BuildingUnit(Unit):
    def __init__(self, name, hp, locartion):
        pass # 아무것도 하지않고 일단 넘어간다는 의미로 사용/ 코드 완성되지 않아도 에러없이 프로그램 작동 가능

# 서플라이 디폿 생성 : 건물, 1개 건물 = 8 유닛
supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')

def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    pass

game_start()
game_over()

# 발키리 유닛 생성
valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name, '3시')

# 메소드 오버라이딩 : 상속 관계에 있는 클래스들 사이에서 부모 클래스에 정의된 메소드를 그대로 사용하지 않고 자식 클래스에서 같은 이름으로
# 메소드를 새롭게 정의하여 사용하도록 하는 것


# 지상 유닛 벌쳐 생성
vulture = AttackUnit('벌쳐', 80, 10, 20)

# 공중 공격 유닛 배틀크루저 생성
battlecruiser = FlyableAttackUnit('배틀크루저', 500, 25, 3)

# 이동
vulture.move('11시')
# battlecruiser.fly(battlecruiser.name, '9시')
battlecruiser.move('9시') # 오버라이딩된 move() 호출

# 동일한 move()를 호출하여도 AttackUnit을 통해 만들어진 유닛은 부모클래스 Unit의 move()를
# FlyableAttackUnit을 통해 만들어진 유닛은 오버라이딩을 통해 새롭게 정의된 FlyableAttackUnit의 move()를 호출
