from colorama import init, Fore, Style
from random_word import RandomWords

init(autoreset=True)

r = RandomWords()

word = r.get_random_word()
GREEN = '\033[32m'
RESET = '\033[0m'

def grayLetter(letter, word, guess):
    if letter in word:
        return False
    else:
        return True
    
def yellowLetter(letter, word, guess):
    if letter in word:
        guess_index = guess.index(letter)
        word_index = word.index(letter)
        if guess_index == word_index:
            return False
        else:
            return True
    else:
        return False

def greenLetter(letter, word, guess):
    if letter in word:
        guess_index = guess.index(letter)
        word_index = word.index(letter)
        if guess_index == word_index:
            return True
        else:
            return False
    else:
        return False
    
def checkGuess(guess, word):
    result = []
    for letter in guess:
        if greenLetter(letter, word, guess):
            result.append(("green", letter))
        elif yellowLetter(letter, word, guess):
            result.append(("yellow", letter))
        elif grayLetter(letter, word, guess):
            result.append(("gray", letter))
    return result

def printResult(result):
    color_map = {
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "gray": Fore.BLACK
    }
    for color, letter in result:
        print(color_map[color] + letter.upper(), end=" ")
    print()

def game():
    count = 0
    guess = 5
    while count < guess:
        guess = input("Enter your guess: ").lower()
        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue
        result = checkGuess(guess, word)
        printResult(result)
        colors = [color for color, _ in result]
        if all(color == "green" for color in colors):
            print("Congratulations! You've guessed the word!")
            break

        count+=1
        print("Guesses so far: ", count)

if __name__ == "__main__":
    game()

