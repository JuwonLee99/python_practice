# def profile(name, age, lang1, lang2, lang3, lang4, lang5) :
#     print('이름 : {0}\t나이 : {1}\t' .format(name, age), end="") # end="" : 해당 프린트문이 끝날때 줄바꿈 하지 않고 이어서 출력
#     print(lang1, lang2, lang3, lang4, lang5)




def profile(name, age, *language) :
    print('이름 : {0}\t나이 : {1}\t' .format(name, age), end=" ")
    for lang  in language :
        print(lang, end=" ")
    print()

profile ('유재석', 20, 'Python','Java', 'C', 'C++', 'C#', 'JavaScript')
profile ('이광수', 25, 'Kotlin', 'Swift')