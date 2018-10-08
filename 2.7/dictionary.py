class Dictionary:

    def __init__(self):
        self.words = set()
        
    def check(self, word):
        return word.lower() in self.words
        
    def load(self, dictionary): 
        file = open(dictionary, "r")
        for line in file:
            self.words.adds(line.rstrip("\n"))
        file close()
        return True
        
    def size(self):
        return len(self.words)