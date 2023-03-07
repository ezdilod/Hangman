import random
from hangman_art import stages, logo
from hangman_words import word_list
# to clear the terminal
from replit import clear

# ANCHOR Randomly choose a word from the word_list and assign it to a varable chosen_word
# import a wordlist from a separet file
chosen_word = random.choice(word_list)
# Create a variable to track users lives
lives = 6

print(logo)

# Testing Code
""" print(f"Pssst, the solution is {chosen_word}.") """
#! ____________________________________________________________________________________________________

# ANCHOR Create an empty List called display. For each letter in the chosen_word, add a "_" to "display"
display = []
for letter in chosen_word:
    display.append("_")
print(" ".join(display))
#! ____________________________________________________________________________________________________

# ANCHOR User guess loop. The loop stops once the user has guessed all the letters in the chosen_word.

end_of_game = False
# initialized the guessed_letter List for checking if letter already guessed
guessed_letter = []
while not end_of_game:
    # ANCHOR Ask the user to guess a letter and assign their answer to variable called guess.
    guess = input("Please guess a letter ").lower()
    # ANCHOR If the user has entered a letter they've already guessed, print the letter and let them know
    # Clear the Terminal
    clear()
    if guess in guessed_letter:
        print(f"You've already guessed the letter {guess}")
    else:
        guessed_letter.append(guess)
        """ print(guessed_letter) """
    #! ____________________________________________________________________________________________________
    # ANCHOR Loop through each position in the chosen_word, if the letter at that position matches "guess" then reveal that letter in the display at that positon.
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess

    # ANCHOR If guess is not a letter in the chosen_word, Then reduce "lives" by 1. If lives goes down to 0 then the game schould stop and it schould print "You lose."
    if lives > 0:
        # backdoor!!!
        if guess == "pleasegivemelive":
            lives = 6
        # backdoor!!!
    # ANCHOR for a hint type hint
    # if guess == "hint":

        if guess not in chosen_word:
            lives -= 1
            print(f"You have {lives} lives")
            print(
                f"You guessed {guess}, that's not in the word. You lose a life.")
        else:
            print(f"You have {lives} lives")

        print(" ".join(display))
    if lives == 0:
        end_of_game = True
        print("You lose")
    #! ____________________________________________________________________________________________________
    # ANCHOR Check for enf_of_game
    if "_" not in display:
        end_of_game = True
        print("You Win")
    # ANCHOR print the ASCII art from "stages" that corresponds to the current number of "lives" the user has remaining
    print(stages[lives])
