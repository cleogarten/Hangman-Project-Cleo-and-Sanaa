import random
"""
TO DO (but honestly its fine if we dont do it)
- created rejected pile
- check for non letters
- add more words (this is kinda important i just cant think of any)

dictionary: list that contains choice of words
word: string that is selected for game
blanks: list that starts off with blanks, inputted letters are replaced
blanks_string: string that is blanks (easier to work with)
tries: string that is number of attempts

"""
# SETTING UP THE GAME
dictionary = ["apple", "business", "crystal", "delight", "epilogue", "flavor", "grapefruit", "holiday", "island", "jaundice", "kite", "lemon", "meteor", "newspaper", "orange", "parachute", "quaint", "rustic", "sear", "tornado", "umbrella", "volcano", "world", "xylem", "yodel", "zinc"]
print("Welcome to Hangman! You have 9 attempts to guess the word.")
drawing = [
  "|===| \n|     \n|     \n|     \n|     \n|=======", # none
  "|===| \n|   O \n|     \n|     \n|     \n|=======", # head
  "|===| \n|   O \n|   | \n|     \n|     \n|=======", # arm body
  "|===| \n|   O \n|   | \n|   | \n|     \n|=======", # lower body
  "|===| \n|   O \n|   | \n|   | \n|  /  \n|=======", # left leg
  "|===| \n|   O \n|   | \n|   | \n|  / \\\n|=======", # right leg
  "|===| \n|   O \n|  _| \n|   | \n|  / \\\n|=======", # left arm
  "|===| \n|   O \n|  _|_\n|   | \n|  / \\\n|=======", # right arm
  "|===| \n|  /O \n|  _|_\n|   | \n|  / \\\n|=======", # left hair
  "|===| \n|  /O\\\n|  _|_\n|   | \n|  / \\\n|=======" # right hair
]

def game():
  word = random.choice(dictionary)
  attempts = 0
  blanks = []
  rejected = [' ']
  for i in range(0,len(word)): # to print as many blanks as letters in word
    blanks.append("_ ")
  
  def update(): # updates blanks_string to match blanks
    blanks_string = ''.join(blanks)
    print(blanks_string)
    rejected_string = rejected[0] + ', '.join(rejected[1:])
    print("Incorrect letters:" + rejected_string)
  
  def guess(): # asks for letter
    letter = input("Guess a letter: ").lower() # asks for letter
    replaced = False
    while letter not in 'abcdefghijklmnopqrstuvwxyz' or len(letter) != 1:
      letter = input("That's not a letter, try again: ")
    while letter in rejected:
      letter = input("You already entered that letter, try again: ")
    for i in range(len(word)):
      if letter == word[i]:
        blanks[i] = letter + " " # replaces each blank for inputted letter (repeats included)
        replaced = True
    if replaced == False:
      rejected.append(letter)
    return replaced
  
  while attempts < 9 and blanks.count("_ ") > 0:
    print(drawing[attempts])
    update()
    if guess() == False:
      attempts += 1
  
  if attempts == 9: # if game is lost
    print(drawing[attempts])
    print("Sorry you lost. The word was", word + ".")
  
  if blanks.count("_ ") == 0: # if game is won
    print("\nCongrats! You won! The word was", word + ".")

# GAMEPLAY
game()
again = 'Y'
while again == 'Y':
  again = input("Try again? Type Y for yes, N for no.\n").upper()
  while again != 'Y' and again != 'N': # if input isnt Y or N
    again = input("That's not Y or N, only type either letter.\n").upper()
  if again == 'Y':
    print("\n")
    game() # repeat
  elif again == 'N':
    print("Thanks for playing! Bye!") # ends code