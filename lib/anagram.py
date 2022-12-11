# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, arr_of_words):
        output = []
        for word in arr_of_words:
            if (sorted(list(word)) == sorted(list(self.word))):
                output.append(word)
        
        return output

    # def is_anagram(self, word):
    #     sortedA = list(word)
    #     sortedB = list(self.word)
    #     sortedA.sort()
    #     sortedB.sort()
    #     if sortedA == sortedB:
    #         return True
        
    #     return False
   
        