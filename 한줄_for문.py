# 출석 번호 1 2 3 4,  앞에 100을 붙이기로 붙임 -> 101, 102, 103, 104
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)




# 학생 이름을 길이로 변환
students = ['Iron man', 'Thor', 'I am groot']
print(students)
students = [len(i) for i in students]
print(students)


# 학생 이름을 대문자로 바꾸기
students = ['Iron man', 'Thor', 'I am groot']
print(students)
students = [i.upper() for i in students]
print(students)