class Word:
    def __init__(self, new_word, sample1, sample2, answer):
        self.new_word = new_word
        self.sample1 = sample1
        self.sample2 = sample2
        self.answer = answer

    def show_question(self):
        print('"{0}"의 뜻은?'.format(self.new_word))
        print(f'1.{self.sample1}')
        print(f'2.{self.sample2}')

    def check_answer(self, ans_num):
        if ans_num == self.answer:
            print('정답입니다!')
        else:
            print('틀렸습니다.')


word = Word('얼죽아','얼어 죽어도 아메리카노', '얼굴만은 죽어도 아기피부', 1)
word.show_question()
word.check_answer(int(input('=> ')))