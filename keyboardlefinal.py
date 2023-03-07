from typing import List
import random

global score
global part_b
global total_score
global score

row_one = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']  # first row of standard QWERTY keyboard.
row_two = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[']  # second row of standard QWERTY keyboard.
row_three = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"']  # third row of standard QWERTY keyboard.
row_four = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']  # fourth row of standard QWERTY keyboard.

# print sequence for user to visualize keyboard:
print(row_one)
print(row_two)
print(row_three)
print(row_four)


def answer():
    row_list = [row_one, row_two, row_three, row_four]  # Create list with all possible rows for randomization.
    part_a = random.choice(row_list)  # Randomly choose a row.
    global part_b
    global part_c
    part_b = random.choice(part_a)  # Randomly choose value from chosen row.
    # Find which row the answer is from and index it.
    if row_one.count(part_b) == 1:
        part_c = row_one.index(part_b)
    if row_two.count(part_b) == 1:
        part_c = row_two.index(part_b)
    if row_three.count(part_b) == 1:
        part_c = row_three.index(part_b)
    if row_four.count(part_b) == 1:
        part_c = row_four.index(part_b)
    # Part_a = The random row choice.
    # Part_b = The answer.
    # Part_c = The index value of the answer.


def del_sequence_a():
    del row_one[guess_index:]
    del row_two[guess_index:]
    del row_three[guess_index:]
    del row_four[guess_index:]
    # Deletes everything from the guess onward in the lists.


def del_sequence_b():
    del row_one[:guess_index]
    del row_two[:guess_index]
    del row_three[:guess_index]
    del row_four[:guess_index]
    # Deletes everything up until the guess.


def del_sequence_c():
    row_two.clear()
    row_three.clear()
    row_four.clear()
    # Deletes everything in all rows besides row_one.


def del_sequence_d():
    row_one.clear()
    row_three.clear()
    row_four.clear()
    # Deletes everything in all rows besides row_two.


def del_sequence_e():
    row_one.clear()
    row_two.clear()
    row_four.clear()
    # Deletes everything in all rows besides row_three.


def del_sequence_f():
    row_one.clear()
    row_two.clear()
    row_three.clear()
    # Deletes everything in all rows besides row_four.


def print_sequence():
    print(row_one)
    print(row_two)
    print(row_three)
    print(row_four)
    # Prints the rows in their current state.


def guess_one():
    if id(guess) == id(part_b):  # Checks if answer is correct.
        print("Lets go you win!")
        print("You took " + str(score) + " tries.")
        total_score += score
        avg = avg_guesses(total_score, games)
        print("The total games you've played is: " + str(games) + ", With an average score of: " + str(avg))
    elif row_one.count(guess) == 1:  # Checks if answer is in row_one.
        if row_one.index(guess) > part_c:  # Checks if the guess is on the right or left side of answer.
            global guess_index
            guess_index = row_one.index(guess)  # Index's the guess.
            del_sequence_a()  # Left side.
        else:
            guess_index = int(row_one.index(guess))  # Index's the guess.
            del_sequence_b()  # Right side.
    elif row_two.count(guess) == 1:  # Checks if answer is in row_two.
        if row_two.index(guess) > part_c:  # Checks if the guess is on the right or left side of answer.
            guess_index = int(row_two.index(guess))  # Index's the guess
            del_sequence_a()  # Left side.
        else:
            guess_index = int(row_two.index(guess))
            del_sequence_b()  # Right side.
    elif row_three.count(guess) == 1:  # Checks if answer is in row_three.
        if row_three.index(guess) > part_c:  # Checks if the guess is on the right or left side of answer.
            guess_index = int(row_three.index(guess))  # Index's the guess.
            del_sequence_a()  # Left side.
        else:
            guess_index = int(row_three.index(guess))  # Index's the guess.
            del_sequence_b()  # Right side.
    else:  # In row four if it's gotten this far.
        if row_four.index(guess) > part_c:  # Checks if the guess is on the right or left side of answer.
            guess_index = int(row_four.index(guess))  # Index's the guess.
            del_sequence_a()  # Left side.
        else:
            guess_index = int(row_four.index(guess))  # Index's the guess.
            del_sequence_b()  # Right side.


def guess_two():
    global total_score
    if id(guess) == id(part_b):  # Checks if answer is correct.
        print("Lets go you win!")
        print("You took " + str(score) + " tries.")
        total_score += score
        avg = avg_guesses(total_score, games)
        print("The total games you've played is: " + str(games) + ", With an average score of: " + str(avg))
    elif row_one.count(guess) == 1 and row_one.count(part_b) == 1:  # Checks if guess and answer is in row_one.
        del_sequence_c()
        if row_one.index(guess) > row_one.index(part_b):  # Checks if the guess is on the right or left side of answer.
            del row_one[row_one.index(guess):]  # Deletes right side of row.
        else:
            del row_one[0:row_one.index(guess)]  # Deletes left side of row.
    elif row_two.count(guess) == 1 and row_two.count(part_b) == 1:  # Checks if guess and answer is in row_two.
        del_sequence_d()
        if row_two.index(guess) > row_two.index(part_b):  # Checks if the guess is on the right or left side of answer.
            del row_two[row_two.index(guess):]  # Deletes right side of row.
        else:
            del row_two[0:row_two.index(guess)]  # Deletes left side of row.
    elif row_three.count(guess) == 1 and row_three.count(part_b) == 1:  # Checks if guess and answer is in row_three.
        del_sequence_e()
        if row_three.index(guess) > row_three.index(part_b):  # Checks if guess is on the right or left side of answer.
            del row_three[row_three.index(guess):]  # Deletes right side of row.
        else:
            del row_three[0:row_three.index(guess)]  # Deletes left side of row.
    elif row_four.count(guess) == 1 and row_four.count(part_b) == 1:  # Checks if guess and answer is in row_four.
        del_sequence_f()
        if row_four.index(guess) > row_four.index(part_b):  # Checks if guess is on the right or left side of answer.
            del row_four[row_four.index(guess):]  # Deletes right side of row.
        else:
            del row_four[0:row_four.index(guess)]  # Deletes left side of row.
    else:  # checks if guess is not in the same row as the answer, then guess_one sequence repeats.
        guess_one()


def avg_guesses(total_score, games):
    if games == 0:
        return 0
    return total_score / games


def play_again():
    play = input("would you like to play again y/n?")
    if play.lower() == "y":
        return True
    else:
        return False

answer()
guess = " "
guessed_letters = set()
games = 0
total_guesses = 0
total_score = 0

while True:
    score = 0
    guess = input("Guess a keystroke!")  # User input.
    score += 1
    games += 1
    if guess in guessed_letters:
        print("You've already guessed the letter '{}'.".format(guess))
    elif len(guess) != 1:
        print("Invalid input. Please enter a single lowercase letter.")
    elif guess in row_one or guess in row_two or guess in row_three or guess in row_four:
        guess_one()
        guessed_letters.add(guess)
        print_sequence()
    else:
        print("The key pressed does not appear to be in the keyboard, try again.")

    while guess != part_b:
        guess = input("Guess a keystroke!")  # User input.
        score += 1
        if guess in guessed_letters:
            print("You've already guessed the letter '{}'.".format(guess))
        elif len(guess) != 1:
            print("Invalid input. Please enter a single lowercase letter.")
        elif guess in row_one or guess in row_two or guess in row_three or guess in row_four:
            guess_two()
            guessed_letters.add(guess)
            print_sequence()
        else:
            print("The key pressed does not appear to be in the keyboard, try again.")
    if play_again():
        row_one = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-']  # first row of standard QWERTY keyboard.
        row_two = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[']  # second row of standard QWERTY keyboard.
        row_three = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '"']  # third row of standard QWERTY keyboard.
        row_four = ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/']  # fourth row of standard QWERTY keyboard.
        print_sequence()
        guessed_letters = set()
        answer()
    else:
        break