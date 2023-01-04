# A열의 홀수좌석만 출력

for i in range(1,21):
    if i % 2 != 0 :
        print('A'+str(i),end=' ')

for i in range(1,21)[::2]:
    print('A'+str(i), end=' ')

for i in range(1, 21, 2):
    print(f'A{i}',end=' ')