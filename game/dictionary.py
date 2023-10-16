class Dictionary:
    def __init__(self, file_path):
        self.words = self.words_load(file_path)

    @staticmethod
    def words_load(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return set(word.strip() for word in file)

    def word_exist(self, word):
        word = word.lower()
        return word in self.words