"""
This is a Word Guesser type game called AHORCADO GAME. It can
take a file with a single word for each row as a list of words for the game.

Feel free to update the file variable with a .txt of your own! (Remember! Only
a word for row!)
"""
import random # For randomize the choosen word
import os # For using os.system("clear") and exit() functions

CHANCES = 6 # Editable here as a CONSTANT

file = open('Lexicon.txt','r') # You can edit the file with the words
words = file.readlines()
length = len(words)

def main():
    print_game_banner()
    while True:
        random_word = get_random_word()
        play_game(random_word)
        continue_playing()


# Select a random word from the list(file) provided
def get_random_word():
    random_no = random.randint(0,length)
    word = words[random_no].strip()
    return word

"""
This is the core function of the game: while chances are not 0 it keeps asking the user 
to guess a letter. 
    1) If the letter is in the word, it keeps asking for more letters
    2) If the letter is not in the word, it discount 1 to chances and keeps asking
    3) If the letter is already guessed, keep asking without discounting chances
"""
def play_game(random_word):
    is_found = False
    guessed_letters = []
    guess = ''
    chances = CHANCES # Assign chances variable to a CONSTANT that can updated
    print(' ' + '_ ' * len(random_word) + '\n')
    while chances > 0:
        """
        Force the input to be stored in the variable in uppercase for
        not forcing the user to use capital letters in the game despite the words
        in the file 'Lexicon.txt' are all in UPPERCASE.
        """
        guess = (input('Guess a letter or the entire word: ')).upper() 
        if guess == random_word:
            is_found = True
        else:
            if guess in guessed_letters :
                print(f"You've already guessed the letter {guess}... Let's try other letter!\n")
                continue
            print(' ', end='')
            is_current_guess = False
            for letter in random_word:
                if letter == guess :
                    is_current_guess = True
                    guessed_letters.append(letter)
                    print(letter, end=' ')
                    if len(random_word) == len(guessed_letters):
                        is_found = True
                elif letter in guessed_letters:
                    print(letter, end=' ')
                else:
                    print('_', end=' ')	
            print()
        if is_found:
            print(f"Congratulations! Your guess was correct, the word was '{random_word}'\n")		
            break
        if not is_current_guess:
            print(f'{guess} is not in the word')
            chances -= 1
            print(f'You have {chances} chances remaining\n')
    # if the user run out of chances
    if not is_found:
        print(f"\n Sorry your guesses were wrong, the entire word was '{random_word}'\n")		

# Display a banner/header for the game
def print_game_banner():
    os.system("clear")
    print()
    print(" * - * - * - * - * ".center(60,'-'))
    print(" Ahorcado Game in Python ".center(60,'-'))
    print(" * - * - * - * - * ".center(60,'-'))
    print()

# Let the user chooses to keep playing or not
def continue_playing():
    choice = input("Do you want to continue playing?(y/n): ")
    os.system("clear")
    if choice in ['no','No','NO','n','N']:
        exit()
    else:
        random_word = get_random_word()
        play_game(random_word)
        continue_playing()

if __name__ == '__main__':
    main()
