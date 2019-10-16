# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:

    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", str(self.user_input))


        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3

        li = list(self.user_input)
        print(li)

        #for i in range(1, len(li) - 2, 3):
        #    temp = li[i]
        #    li[i] = li[i + 1]
        #    li[i + 1] = temp

        #print(li)


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation


word_scrambler = WordScramble()
word_scrambler.scramble()

