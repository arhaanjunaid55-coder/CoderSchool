word = "Rubics"

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
        if grayLetter(letter, word, guess):
            result.append("gray")
        elif yellowLetter(letter, word, guess):
            result.append("yellow")
        elif greenLetter(letter, word, guess):
            result.append("green")
    return result

def game():
    while True:
        guess = input("Enter your guess: ")
        if len(guess) != len(word):
            print(f"Please enter a {len(word)}-letter word.")
            continue
        result = checkGuess(guess, word)
        print(result)
        if all(color == "green" for color in result):
            print("Congratulations! You've guessed the word!")
            break

if __name__ == "__main__":
    game()