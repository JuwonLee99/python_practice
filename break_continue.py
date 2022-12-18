#예제 : 결석한 아이들 제외 출석한 아이들 대상으로 출석부르기

#continue 해당 실행을 건너뛰고 다음 실행을 진행
#break 반복문 탈출
absent = [2, 5] #결석
no_book = [7] #책을 깜박함
for student in range(1, 11):
    if student in absent :
        continue
    elif student in no_book:
        print('오늘 수업 여기까지. {0}은 교무실로 따라와.' .format(student))
        break
    print('{0}야, 책 읽어봐.' .format(student))
