class WordsFinder:
    def __init__(self, *args):
        self.files = list(args)

    def get_all_words(self):
        all_words = {}
        punct = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.files:
            with open(i, 'r', encoding='utf-8') as file:
                _str = file.read().casefold().replace('\n', ' ')
            for _ in punct:
                _str = _str.replace(_, '')
        all_words[i] = _str.split()
        return all_words

    def find(self, word):
        dct = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            if word.casefold() in value:
                dct = {key: value.index(word.casefold())+1}
            else:
                print(f'слово {word} не найдено!')
        return dct

    def count(self, word):
        dct = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            cnt = value.count(word.casefold())
            if cnt > 0:
                dct = {key: cnt}
            else:
                print(f'слово {word} не найдено!')
        return dct


tst_str = "'It's a text for task найти везде,\nИспользуйте его для самопроверки.\nУспехов в решении задачи!\ntext text text"
with open('test_file.txt', 'w', encoding='utf-8') as tst_fl:
    tst_fl.write(tst_str)

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
