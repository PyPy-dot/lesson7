import re


class WordsFinder:
    def __init__(self, *args) -> None:
        self.file_names = args

    def get_all_words(self) -> dict:
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                for line in file:
                    list_of_words = map(lambda word: re.search(r"[a-zA-Zа-яА-Я'-]{1,}", word),
                                        line.split())
                    all_words.setdefault(file_name, []).extend(map(lambda word: word.group(0).lower(),
                                                                   filter(bool, list_of_words)))
        return all_words

    def find(self, word: str) -> dict:
        first_pos_dict = {}
        all_words = self.get_all_words()
        for key, value in all_words.items():
            if word.lower() in value:
                first_pos_dict[key] = all_words[key].index(word.lower()) + 1
                continue
        return first_pos_dict

    def count(self, word: str) -> dict:
        all_words = self.get_all_words()
        return {key: value.count(word.lower()) for key, value in all_words.items()}


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))  # 3 слово по счёту

print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
