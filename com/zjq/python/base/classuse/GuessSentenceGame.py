from com.zjq.python.base.classuse.KeyValueSet import KeyValueSet


class GuessSentenceGame:
    def __init__(self):
        self.kv = KeyValueSet()
        self.score = 0


    def setup(self, sentences):
        for sentence in sentences:
            self.append(sentence)

    def append(self, sentence):
        cut_pos = sentence.find(' ')
        first_word, rest = sentence[0:cut_pos], sentence[cut_pos + 1:].strip()
        self.kv.set(first_word, rest)

    def guess(self, first_word):
        ret = self.kv.get(first_word)
        if ret is None:
            return 1, None
        else:
            return 0, ret

    def run(self):
        self.score = 0
        for first_word in self.kv.keys():
            ret = input("猜一猜下半句是什么？ {} -> :".format(first_word))
            err, value = self.guess(first_word)
            if err == 0:
                print('你太厉害了，这都能猜得到！+10分！')
                self.score += 10
            else:
                self.score -= 2
                print('哈哈，肯定猜不到得啦：{}->{}，扣除2分！'.format(first_word, value))
        print('游戏结束，你本次游戏得分：', self.score)


if __name__ == '__main__':
    sentences = [
        "hello world",
        'monkey king',
        'tomorrow is another day',
        "good bye"
    ]

    game = GuessSentenceGame()
    game.setup(sentences)
    game.run()