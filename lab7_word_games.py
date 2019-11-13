# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 07-11-2019
# purpose: Lab 7 - Word Games

class WordGames:
    def __init__(self):
        self.mywords = input("Please enter a word or sentence: ")
        self.word_play()

    def word_play(self):
        print("User input was: "+self.mywords)

class WordDupli(WordGames):
    def word_play(self):
        #super().__init__()
        sentence = self.mywords
        print("The sentence was:", sentence+sentence)

class WordScramble(WordGames):
    #def __init__(self):
        #super().__init__()
        #WordGames

    def word_play(self):
        sentence = self.mywords.strip().split() # .strip() is first
        for word in sentence:
            scrambled = list(word)
            if len(word) > 4:
                if len(word) % 2 == 0:
                    for i in range(1, int((len(word) - 1) / 2)):
                        temp = scrambled[i]
                        scrambled[i] = scrambled[-1 - i]
                        scrambled[-1 - i] = temp
                else:
                    for i in range(1, int(len(word) / 2)):
                        temp = scrambled[i]
                        scrambled[i] = scrambled[-1 - i]
                        scrambled[-1 - i] = temp
                scrambled = ''.join(scrambled)
            elif len(word) == 4:
                scrambled = word[0] + word[-2] + word[1] + word[3]
            else:
                scrambled = ''.join(scrambled)
            print(scrambled)

class Whatever(WordScramble, WordDupli):
    pass


#wg = WordGames()
#ws = WordScramble()
wd = WordDupli()