#!/usr/bin/env python

# Password generator that requires an input phrase to then encrypt using the random module
import random

# defining a list of symbols
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=', '+', '{', '}', '[', ']', '|', ';', ':', "'", '"', ',', '.', '/', '?', '<', '>']

phrase = input('Input a phrase to turn it into a strong password: ')  # Input phrase
cycles = input('How many passwords do you want to generate: ')  # user choice of how many cycles or generations

for i in range(int(cycles)):  # repeats by number of cycles
    # turn the phrase into a list
    phrase = list(phrase)
    # create an empty list called part1.
    part1 = []  # this is were all modified characters will be appended to
    
    # goes through every character (char) in the phrase list and modifies it accordingly
    for char in phrase:
        # 50 percent chance that 'e' will be turnned into a '3'
        if char == 'e' or char == 'E':
            chance = random.randint(0, 1)
            if chance == 0:
                part1.append(char)
            else:
                part1.append('3')  # appends modified char to part1
        
        # replaces spaces with '-' character or removes them
        elif char == ' ':
            chance = random.randint(0, 1)
            if chance == 1:
                part1.append('-')
            else:
                part1.append('')  # removes space
        
        # 50 percent chance that 's' will be turnned into a '$'
        elif char == 's' or char == 'S':
            chance = random.randint(0, 1)
            if chance == 0:
                part1.append(char)
            else:
                part1.append('$')  # appends modified char to part1
        
        # 50 percent chance that 'l' will be turnned into a '1'
        elif char == 'l':
            chance = random.randint(0, 1)
            if chance == 0:
                part1.append(char)
            else:
                part1.append('1')  # appends modified char to part1
        
        # 50 percent chance that 'H' will be turnned into a '#'
        elif char == 'H':
            chance = random.randint(0, 1)
            if chance == 0:
                part1.append(char)
            else:
                part1.append('#')  # appends modified char to part1
        
        # 50 percent chance that'A' will be turnned into a '4'
        elif char == 'A':
            chance = random.randint(0, 1)
            if chance == 0:
                part1.append(char)
            else:
                part1.append('4')  # appends modified char to part1
        
        # checks if char is a letter
        elif char.isalpha():
            # checks if the char is uppercase
            if char.isupper():
                chance = random.randint(0, 1)  # 50 percent chance that the letter will be made lowercase
                if chance == 0:
                    part1.append(char.lower())
                else:
                    part1.append(char.upper())
            
            # checks if the char is lowercase
            else:
                chance = random.randint(0, 1)  # 50 percent chance that the letter will be made uppercase
                if chance == 0:
                    part1.append(char.lower())
                else:
                    part1.append(char.upper())
        
        elif char.isdigit():  # numbers are left alone
            part1.append(char)

    # creates a list called password
    password = []

    # changes some characters to symbols
    for chars in part1:  # goes through each character in part1
        sym_choice = random.randint(0, 9)  # 10 percent cahnce a character will be modified

        if sym_choice == 1:
            # randomly chooses a symbol from the 'symbols list'
            final_symbol = random.choice(symbols)
            password.append(final_symbol)
        else:
            password.append(chars)

    # joins the final 'password' list into a string and prints it out
    password = ''.join(password)
    print(password)
