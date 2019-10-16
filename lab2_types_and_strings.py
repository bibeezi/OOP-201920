#course: Object-oriented programming, year 2, semester 1
#academic year: 201920
#author: B. Schoen-Phelan
#date: 29-09-2019
#purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        # print only first and last of the sentence
        print(message[0] + message[-1])

        # use slice notation
        print(message[:4])
        print(message[2:])
        print(message[:])

        # escaping a character
        print("That\'s fantastic!")


        # find all a's in the input word and count how many there are
        x = message.find("a", 0, -1)
        print(x)
        print(message.count('a'))
        print(len(message))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()
        print(message.replace('a', '-'))


        # printing only characters at even index positions
        for i in range(0, len(message) - 1, 2):
            print("index[", i, "]", message[i])


    def play_with_lists(self):
        message = input("Please enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        message2 = input("Please enter another sentence:")
        li = list(message2.split(" "))


        # append a new element to the list and print
        li.append("and I like cake !")


        # remove from the list in 3 ways
        #x = "my name is"
        li.pop()
        #li.remove(x)


        # check if the word cake is in your input list
        print(li)
        print('cake' in li)


        # reverse the items in the list and print
        li.reverse()
        print(li)

        # reverse the list with the slicing trick
        reverseli = li[::-1]
        print(reverseli)

        # print the list 3 times by using multiplication
        sentence = 'Hello again'
        print(sentence * 3 + ' ')


tas = Types_and_Strings()
tas.play_with_strings()
tas.play_with_lists()