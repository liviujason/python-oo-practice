import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:

    def __init__(self, file, list=[]):
        self.file = file
        self.list = list
        self.read()

    def __repr__(self):
        return f"{len(self.list)} words read"

    def read(self):
        self.list = []
        dictionary = open(self.file, 'r')
        for line in dictionary:
            self.list.append(line.strip())
        dictionary.close()
        print(f"{len(self.list)} words read")
        return self.list

    def random(self):
        return self.list[random.randint(1, 235886)]

    def reset(self):
        return self.list.clear()


class SpecialWordFinder(WordFinder):

    def random(self):
        answer = super().random()
        if str(answer)[0] != '#' or str(answer).strip() != 0:
            return answer
