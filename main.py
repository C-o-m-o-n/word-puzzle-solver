# Word Puzzle solver
import random

#get the letters from the user
inp = input("Enter the letters -->: ")

#convert the string of the letters into a list
letters = list(inp)

#wordListPath = "/home/comon/Dev/lesp/wordlist.txt"
#with open(wordListPath, 'r') as f:
#    wordList = f.read()
# print(wordList)

def shuffleWord():
    found = False #set found to false
    while not found:
        random.shuffle(letters)
        word = ''.join(letters)
        print(word)

        check = input("is that the word? \n[Y/N] -->: ")

        if check == "y":
            found = True
        elif check == "n":
            continue

shuffleWord()
