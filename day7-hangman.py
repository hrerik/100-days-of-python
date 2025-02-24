import random

# Getting the word
word_list = ["aadvark", "baboon", "camel"]
word = word_list[random.randint(0, len(word_list) - 1)]

# Other variables
guessing_word = list("_" * len(word)) # guessing word is a list, not a string for now
placeholder_word = "".join(guessing_word) # the string itself, which will be used for comparisons (using this method since strings are immutable in python)
lives = 6

def is_in(c,s): # c = char, s = string
  for _c in s:
      if c == c:
          return True
  return False
    

# Intro
print("Welcome to hangman!!!")

# Running the game
while lives != 0: 
  print(f"You have {lives}/6 lives")
  print(f"The word is: {placeholder_word}")
  guess_letter = input("What letter will you guess??\n>").lower()
  
  # Extra space on the console
  print()
  
  
  
  # Checking the letters and putting them on the word
  no_letter = True
  i = -1
  for letter in word:
    i += 1
    if guess_letter == letter:
      guessing_word[i] = guess_letter
      no_letter = False
  if no_letter:
    lives -= 1
    print(f"There's no {guess_letter} letter on the word, -1 life   .\n")
   
  placeholder_word = "".join(guessing_word) # Turning list into string
  
  # Checking the word
  if placeholder_word == word:
    print(f"YOU GOT IT RIGHT!! The word was {word}!!\nYou had {lives} lives left.")
    break
  
# No more lives
else: 
  print(f"You lost!! The right word was {word}")
