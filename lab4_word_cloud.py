# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 10-10-2019
# purpose: Lab 4

class WordCloud:

    # initialises everything
    # everything gets kicked off here
    def __init__(self):
        self.my_dict = self.create_dict()
        # you might like to run the following line only
        # if there wasn't a problem creating the dictionary
        if self.my_dict:
            self.create_html(self.my_dict)
        else:
            print("issue with input file")

    # this function creates the actual html file
    # takes a dictionary as an argument
    # it helps to multiply the key/occurance of word number with 10
    # in order to get a decent size output in the html
    def create_html(self, the_dict):
        fo = open("output.html", "w")
        fo.write("""<!DOCTYPE html>
<html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Tag Cloud Generator</title>
    </head>
    <body>
        <div style="text-align: center; vertical-align: middle; font-family: arial; color: white; background-color:black; border:1px solid black">
""")

        # your code goes here!
        #fo.write('<span style="font-size: 10px"> HELLO </span>')
        for key in the_dict.keys():
            fo.write('            <span style="font-size: ')
            fo.write(str(the_dict[key]*10))
            fo.write('px"> ')
            fo.write(key)
            fo.write(' </span>\n')

        fo.write("""        </div>
    </body>
</html>""")


    # opens the input file gettisburg.txt
    # remember to open in in the correct mode
    # reads the file line by line
    # creates the dictionary containing the word itself
    # and how often it occurs in a sentence
    # makes a call to add_to_dict where the dictionary
    # is actually populated
    # returns a dictionary
    def create_dict(self):
        my_dict = {}
        # your code goes here:
        try:
            fo = open("gettisburg.txt","r")
        except Exception as e:
            my_dict = False
            print("Caught this err0r: %s" % e.__class__.__name__)
        else:
            for line in fo:
                line = line.lower()
                line = line.split()
                for w in line:
                    self.add_to_dict(w, my_dict)

            fo.close()

        return my_dict

    # helper function that is called from
    # create_dict
    # receives a word and a dictionary
    # does the counting of the key we are at and adds 1
    # if this word already exists. Otherwise sets the
    # word occurance counter to 1
    # returns a dictionary
    def add_to_dict(self, word, the_dict):
        # your code goes here
        for key in the_dict.keys():
            if key == word:
                the_dict[key] = the_dict[key]+1
                return the_dict
        else:
            the_dict[word] = 1
            return the_dict

        return the_dict


wc = WordCloud()
