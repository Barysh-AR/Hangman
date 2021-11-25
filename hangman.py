# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for i in secret_word:
      if i not in letters_guessed:
        return False
    return True
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    string = ''
    for i in secret_word:
      if i in letters_guessed:
        string += str(i)
      else: string += ' _ '
    return string
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    a = 'abcdefghijklmnopqrstuvwxyz'
    lis = ''
    for i in a:
      if i not in letters_guessed:
        lis += i
    return lis
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

secret_word = 'aboba'
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = ''
    number_of_attempts = 6
    warnings = 3
    print('Welcome to the game Hangman!' + '\n' + 'I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('-------------')
    while is_word_guessed(secret_word, letters_guessed)==False and number_of_attempts > 0:
      
      print('You have {} guesses left.'.format(number_of_attempts) + '\n' + 'Available letters: {}'.format(get_available_letters(letters_guessed)))
      while True:
        your_letter = (str(input('Please guess a letter: ')).lower())
        
        if your_letter in get_available_letters(letters_guessed) and your_letter in 'abcdefghijklmnopqrstuvwxyz' and len(your_letter)==1:
          break
        print('-------------')
        print('You only need to enter one letter from the list: {}'.format(get_available_letters(letters_guessed)))
        if warnings == 0:
          number_of_attempts -=1
          print('-1 guesse'  + '\n' + 'You have {} guesses left.'.format(number_of_attempts))
          if number_of_attempts == 0:
            your_letter=''
            break
        else:
          warnings -=1
          print('You have {} warnings left'.format(warnings))
      
      if your_letter != '':
        if your_letter in secret_word:
          letters_guessed += your_letter
          print( 'Good guess: ' + str(get_guessed_word(secret_word, letters_guessed)))
          print('-------------')
          
        else:
          if your_letter in 'aeiou':
            number_of_attempts -= 2
            letters_guessed += your_letter
            print('-2 guesse')
            print( 'Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, letters_guessed)))
            print('-------------')
            
          else:
            number_of_attempts -= 1
            letters_guessed += your_letter
            print('-1 guesse')
            print( 'Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, letters_guessed)))
            print('-------------')
            
      
    if is_word_guessed(secret_word, letters_guessed):
      
      n = 0
      lis =[]
      for i in secret_word:
        if i not in lis:
          n+=1
          lis += i
      score = number_of_attempts * n
      print('Congratulations, you won! Your total score for this game is: {}'.format(score))
    else:
      
       
      print('Sorry, you ran out of guesses. The word was {}'.format(secret_word))
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word =''
    for i in my_word:
      if i != ' ':word += i
    if len(word) == len(other_word):
      n = 0
      for i in my_word:
        if i == ' ': pass
        elif i == '_': 
          if other_word[n] in word:
            return False
          n += 1 
          pass 
        elif i != other_word[n]:
          return False
        else: n += 1
    else: return False
    return True

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    global wordlist
    n = 0
    for i in wordlist:
      if match_with_gaps(my_word, i):
        print(i, end = ' ')
        n +=1
    if n == 0:
      print('No matches found')
    else: print('')
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = ''
    number_of_attempts = 6
    warnings = 3
    print('Welcome to the game Hangman!' + '\n' + 'I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('-------------')
    while is_word_guessed(secret_word, letters_guessed)==False and number_of_attempts > 0:
      
      print('You have {} guesses left.'.format(number_of_attempts) + '\n' + 'Available letters: {}'.format(get_available_letters(letters_guessed)))
      while True:
        your_letter = (str(input('Please guess a letter: ')).lower())
        if your_letter == '*':
          print('Possible word matches are: ', end= '')
          show_possible_matches(get_guessed_word(secret_word, letters_guessed))
          print('-------------')
        else:

          
          if your_letter in get_available_letters(letters_guessed) and your_letter in 'abcdefghijklmnopqrstuvwxyz' and len(your_letter)==1:
            break
          print('-------------')
          print('You only need to enter one letter from the list: {}'.format(get_available_letters(letters_guessed)))
          if warnings == 0:
            number_of_attempts -=1
            print('-1 guesse'  + '\n' + 'You have {} guesses left.'.format(number_of_attempts))
            if number_of_attempts == 0:
              your_letter=''
              break
          else:
            warnings -=1
            print('You have {} warnings left'.format(warnings))
      
      if your_letter != '':
        if your_letter in secret_word:
          letters_guessed += your_letter
          print( 'Good guess: ' + str(get_guessed_word(secret_word, letters_guessed)))
          print('-------------')
          
        else:
          if your_letter in 'aeiou':
            number_of_attempts -= 2
            letters_guessed += your_letter
            print( 'Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, letters_guessed)))
            print('-------------')
            print('-2 guesse')
            
          else:
            number_of_attempts -= 1
            letters_guessed += your_letter
            print( 'Oops! That letter is not in my word: ' + str(get_guessed_word(secret_word, letters_guessed)))
            print('-------------')
            print('-1 guesse')
            
      
    if is_word_guessed(secret_word, letters_guessed):
      n = 0
      lis =[]
      for i in secret_word:
        if i not in lis:
          n+=1
          lis += i
      score = number_of_attempts * n
      print('Good guess: {}'.format(secret_word))
      print('Congratulations, you won! Your total score for this game is: {}'.format(score))
    else:
      print('Sorry, you ran out of guesses. The word was {}'.format(secret_word))
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
