import requests
from time import sleep
from termcolor import colored
from os import system, name

HANGMAN_ASCII = ['''
    +---+
        |
        |
        |
       ###''', '''
    +---+
    0   |
        |
        |
       ###''','''
    +---+
    0   |
    |   |
        |
       ###''','''
    +---+
    0   |
   /|   |
        |
       ###''','''
    +---+
    0   |
   /|\  |
        |
       ###''','''
    +---+
    0   |
   /|\  |
   /    |
       ###''','''
    +---+
    0   |
   /|\  |
   / \  |
       ###''']

responses = responses = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/ksnlksjsfkna")

while(responses.status_code != 200):
    response = requests.get("https://random-word-api.herokuapp.com/word?number=1&swear=0")
    l = response.json()[0]    
    responses = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{}".format(l))
    data = responses.json()
    try:
        definition = data[0]['meanings'][0]['definitions'][0]['definition']
    except KeyError:
        continue


n = len(l)
dash = "_"*n

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def replace(a, b, c):
    i = 0
    b1 = list(b)
    c1 = list(c)
    for s in b1:
        if a==s:
            c1[i] = a
        i+=1
    final = "".join(c1)
    return final

life = 0
won = True
wrong_guess = list()
correct_guess = list()
hints = False
while(life <= 7 and won):
    if life == 7:
        break
    clear()
    print(colored("LIVES : {}".format(7-life), 'red'))
    print(colored(HANGMAN_ASCII[life], 'yellow'))
    print(dash)
    print(colored("Wrong guesses : {}".format(wrong_guess), 'red'))
    print(colored("Correct guesses: {}".format(correct_guess), 'green'))
    count = 0
    if hints:
        print(colored(definition, 'yellow'))
    print(dash)
    print("Enter character (lowercase a-z)")
    guess = input()
    if guess in l:
        correct_guess.append(guess)
        dash = replace(guess, l, dash)
    else:
        wrong_guess.append(guess)
        life+=1
    if life == 4:
        print("hint: {}".format(definition))
        hints = True
    if dash == l:
        print("correct! its {}".format(l))
        print("Score is {}".format(len(l)*(7-life)))
        print(colored("WINNER", 'green'))
        won = False

if won:
    print("YOU LOSE!!!")
    print("Word was {}".format(l))