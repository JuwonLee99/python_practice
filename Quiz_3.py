#사이트별로 비밀번호를 만들어주는 프로그램 작성

#예) http://naver.com
#규칙1 : http:// 부분은 제외
#규칙2 : 처음 만나는 점(.)이후 부분은 제외
#규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + '!'로 구성
#--> nav51!


#[1] 작성
# site = 'http://google.com'
# #site = 'http://naver.com'
# i = site.index('.')
# site = site[7:i]
# password = site[:3] + str(len(site)) + str(site.count('e')) + '!'
# print(password)


#[2] 답안
url = 'http://naver.com'
my_str = url.replace('http://', '')
# print(my_str)
my_str = my_str[:my_str.index('.')]
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
print('{0}의 비밀번호는 {1}입니다.' .format(url, password))
