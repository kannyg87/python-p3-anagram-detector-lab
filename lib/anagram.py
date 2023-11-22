class Anagram:
    def __init__(self, word):
        self.word = word

    def is_anagram(self, word1, word2):
        return sorted(word1) == sorted(word2)

    def match(self, word_list):
        matches = []
        for word in word_list:
            if self.is_anagram(self.word, word) and self.word != word:
                matches.append(word)
        return matches
