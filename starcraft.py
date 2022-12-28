# 기본 유닛 생성 클래스 Unit 작성
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 유닛이 생성되었습니다.'.format(name))


    # 지상 유닛 이동 메서드
    def move(self, location):
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))


    # 피해 행동 메서드
    def damaged(self, damage):
        print('{0} : {1} 데미지를 입었습니다.'.format(self.name, damage))
        self.hp -= damage
        print('{0} : 현재 체력은 {1} 입니다.'.format(self.name, self.hp))
        if self.hp <= 0 :
            print('{0] : 파괴되었습니다.'.format(self.name))


# 공격 유닛 생성 클래스 AttackUnit 작성
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
         Unit.__init__(self, name, hp, speed)
         self.damage = damage

    # 공격 행동 메서드
    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]'.format(self.name, location, self.damage))


# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, '마린', 40, 1, 5)

    # 스팀팩 기능 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if self.hp > 10 :
            self.hp -= 10
            print('{0} : 스팀팩을 사용합니다. (HP 10 감소)'.format(self.name))
        else :
            print('{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.'.format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가
    siege_developed =False # 시즈모드 개발여부
    def __init__(self):
        super().__init__('탱크', 150, 1, 35)
        self.siege_mode = False # 시즈모드 (해제 상태)

    # 시즈 모드 실행 메서드
    def set_siege_mode(self):
        if Tank.siege_developed == False: # 시즈모드가 개발되지 않은 경우 메소드 탈출
            return
        
        if self.siege_mode == False :
            print('{0} : 시즈모드로 전환합니다.'.format(self.name))
            self.damage *= 2
            self.siege_mode = True
        
        else : # 시즈모드일 때
            print('{0} : 시즈모드를 해제합니다.'.format(self.name))
            self.damage /= 2
            self.siege_mode = False
    

# 공중 유닛 생성 클래스 Flyable 작성
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location, self.flying_speed))


# 공중 공격 유닛 생성 클래스 FlyableAttackUnit 작성
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
       AttackUnit.__init__(self, name, hp, 0, damage)
       Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)


# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, '레이스', 80, 20, 5)
        self.cloaked = False # 클로킹 모드 (해제 상태)


    # 클로킹 모드
    def clocking(self):
        if self.cloaked == True:
            print('{0} : 클로킹 모드 해제합니다.'.format(self.name))
            self.cloaked = False

        else :
            print('{0} : 클로킹 모드 설정합니다.'.format(self.name))
            self.cloaked = True




def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('Player : gg')
    print('[Player] 님이 게임에서 퇴정하셨습니다.')

# ----------------------------------------------------

# 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄관리 (생성된 모든 유닛 append)
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units :
    unit.move('1시')

# 탱크 시즈모드 개발
Tank.siege_developed = True
print('[알림] 탱크 시즈 모드 개발이 완료되었습니다.')


# 리스트로 관리되는 유닛들을 구분하기 : isinatance()
# 객체가 특정 클래스의 인스턴스인지 여부를 확인할 수 있음

# 공격 모드 준비
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 공격
for unit in attack_units:
    unit.attack('1시')

from random import *

# 피해
for unit in attack_units:
    unit.damaged(randint(5, 20))

# 패배
game_over()