# 스타크래프트 만들기
# 마린 : 공격 유닛, 총을 쏠 수 있음

name = '마린' # 유닛의 이름
hp = 40 # 유닛의 체력
damage = 5 # 유닛의 공격력

print('{} 유닛이 생성되었습니다.'.format(name))
print('체력 {0}, 공격력 {1}\n'.format(hp,damage))


# 탱크 : 포를 쏠 수 있음, 일반모드/시즈모드

tank_name = '탱크'
tank_hp = 150
tank_damage = 35

print('{} 유닛이 생성되었습니다.'.format(tank_name))
print('체력 {0}, 공격력 {1}\n'.format(tank_hp,tank_damage))

tank2_name = '탱크'
tank2_hp = 150
tank2_damage = 35

print('{} 유닛이 생성되었습니다.'.format(tank2_name))
print('체력 {0}, 공격력 {1}\n'.format(tank2_hp,tank2_damage))

#게임 내에서는 수많은 유닛이 생성됨, 이렇게 하나하나 작성할 수 없음 = 클래스의 필요성
# 클래스는 붕어빵 틀에 비유됨 / 서로 연관이 있는 변수와 함수의 집합

def attack (name, location, damage) :
    print('{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]'.format(\
        name, location, damage ))

attack(name, '1시', damage)
attack(tank_name, '1시', tank_damage)
attack(tank2_name, '1시', tank2_damage)

