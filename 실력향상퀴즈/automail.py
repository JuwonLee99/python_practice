# names = ['유튜버1','유튜버2','유튜버3','유튜버4']
# for name in names :
#     with open(name+'.txt','w',encoding='utf8') as mail_file:
#         mail_file.write('안녕하세요? {0}님.'.format(name))
#         mail_file.write('\n\n(주)나도출판 편집자 나코입니다.\n현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.')
#         mail_file.write('\n{0}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.'.format(name))
#         mail_file.write('\n자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.')
#         mail_file.write('\n\n좋은 하루 보내세요^^\n감사합니다.\n\n-나코 드림.')
        
        
        
# (답안)
names = ['유재석','박명수','하하']
for name in names :
    with open('{}.txt'.format(name), 'w', encoding='utf8') as email_file:
        contents = (f"안녕하세요? {name}님.\n\n"
        "(주)나도출판 편집자 나코 입니다.\n"
        "현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.\n"
        f"{name}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.\n"
        "자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.\n\n"
        "좋은 하루 보내세요 ^^\n"
        "감사합니다.\n\n"
        "- 나코 드림.")

        email_file.write(contents)