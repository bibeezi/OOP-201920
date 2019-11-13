# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    # first scramble is just one word
    # reverse two indices
    # particularly good to use is to switch the first two
    # and the last two
    # this only makes sense if you have a world that is longer than 3

    # now try to scramble one sentence

    # do just words first, then you can move on to work on
    # punctuation

    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", str(self.user_input))
        list1 = self.user_input.strip().split()
        print("The sentence right now is", list1)

        for counter, word in enumerate(list1):
            print(counter)
            #for counter = 0, number of words in list1
            checkWord = list(word)
            if len(word) > 4:
                #swap second and second last letter
                #swap third and third last letter
                #etc.
                print("In if word > 4 letters")
                if len(checkWord) % 2 == 0:
                    for i in range(1, int(len(checkWord) / 2)):
                         temp = checkWord[i]
                         checkWord[i] = checkWord[-1 - i]
                         checkWord[-1 - i] = temp
                else:
                    for i in range(1, int((len(checkWord) / 2) - 0.5)):
                         temp = checkWord[i]
                         checkWord[i] = checkWord[-1 - i]
                         checkWord[-1 - i] = temp
                print("After swapping, word is", checkWord)
            elif len(word) == 4:
                # swap indexes [1] and [2]
                print("In elif word is 4 letters")
                checkWord = (checkWord[0], checkWord[2], checkWord[1], checkWord[3])
                print("After swapping, word is", checkWord)
            else:
                #do nothing
                print("in else where word < 4 letters")
                print("No swap:", checkWord)

            #put scrambled word back into list
            list1[counter] = ''.join(checkWord)

        #put scrambled words back into a sentence
        sentence = ' '.join(word for word in list1)
        print("After everything, sentence is now:", sentence)




#Lecturer answer:
        # if len(self.user_input) > 3:
        #     # swap first two indexes.
        #     new_word = self.user_input[0] + self.user_input[2] + self.user_input[1] + self.user_input[3:]
        # elif len(self.user_input) <= 3:
        #     new_word = self.user_input
        # else:
        #     # new_word doesn't exist yet for the print() below so
        #     # create the variable for when it falls in the else.
        #     print("try again")
        #     new_word = False
        #
        # print(new_word)
        #
        # sentence = self.user_input.strip().split()
        # # strip() takes out whitespaces.
        # for index, word in enumerate(sentence):
        #     if len(word) > 3:
        #         # container to swap letters
        #         temp_word = list(word)
        #
        #         if (',' in temp_word):
        #             # swap but keep positionn of comma ,
        #             temp = temp_word[1]
        #             temp_word[1] = temp_word[-3]
        #             temp_word[-3] = temp
        #
        #         else:
        #             # normal swap
        #             temp = temp_word[1]
        #             temp_word[1] = temp_word[2]
        #             temp_word[2] = temp
        #
        #         temp_word = ''.join(temp_word)
        #         # put the word into
        #         sentence[index] = temp_word
        #     else:
        #         # new word is same as the input in else
        #         sentence[index] = word

word_scrambler = WordScramble()
word_scrambler.scramble()

