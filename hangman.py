import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Laten we hangman spelen!')
    print(display_lives(tries))
    print(word_completion)
    print('\n')
    while not guessed and tries > 0:
        guess = input('Welke letter denk je dat er in het woord zit? ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Je hebt deze letter al geraden: ' , guess)
            elif guess not in word:
                print(guess , ' is niet in het woord!')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Goed gedaan, ' , guess , ' is het woord!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isaplha():
            if guess in guessed_words:
                print('Je hebt het woord' , guess , ' al geraden!')
            elif guess != word:
                print(guess , 'is niet het woord!')
                tried -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Geen geldige hok!')
        print(display_lives(tries))
        print(word_completion)
        print('\n')
    
    if guessed:
        print('Gefeliciteerd, je hebt het woord geraden!')
    else:
        print('Sorry, je hebt geen levens meer. Het woord was ' , word)

def display_lives(tries):
    print('Je hebt op dit moment nog ' , tries , ' levens!')

def main():
    word = get_word()
    play(word)
    while input("Opnieuw spelen? (J/N) ").upper() == "J":
        word = get_word()
        play(word)

if __name__ == '__main__':
    main()