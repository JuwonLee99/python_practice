# if 조건:
#     실행명령문

# weather = input('오늘의 날씨 : ')
# if weather == '비' or '눈' : 
#     print('우산을 챙기세요.')
# elif weather == '미세먼지' :
#     print('마스크를 챙기세요.')
# else:
#     print('준비물 필요 없어요.')


temp = int(input('오늘의 기온 : '))
if 30 <= temp :
    print('너무 더워요. 외출을 삼가하세요')
elif 10 <= temp and temp < 30 :
    print('괜찮은 날씨에요.')
elif 0 <= temp < 10 :
    print('외투를 챙기세요.')
else:
    print('너무 추워요. 외출을 삼가하세요.')