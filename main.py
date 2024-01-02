# Word Puzzle solver

import random

inp = input("Enter the letters -->: ")

letters = list(inp)

wordListPath = "/home/comon/Dev/lesp/wordlist.txt"

with open(wordListPath, 'r') as f:
    wordList = f.read()

# print(wordList)

found = False
while not found:
    random.shuffle(letters)
    word = ''.join(letters)
    print(word)

    check = input("is that the word? \n[Y/N] -->: ")

    if check == "y":
        found = True
    elif check == "n":
        continue

