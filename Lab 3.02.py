'''
############
Lab 3.02
############
Lab Exercise 1
--------------
Create a function, birthday_song, that prints out the happy birthday song to whatever name is input as an argument. The contract should be:

  # Name: birthday_song
  # Purpose: birthday_song prints out a personalized birthday song
  # Arguments: name, string
  # Returns: none
  name = input("What is your name? ")
  def birthday_song(name):
    print(f"Happy Birthday to you, Happy Birthday to you, Happy Birthday dear {name}, Happy Birthday to you.")
  birthday_song(name)
     

Lab Exercise 2
---------------
Create a function that randomly picks 5 cards from a deck 

The cards can repeat

Write out the contract for this function using the list.

number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
Bonus
Practice passing in lists as an argument to a function.

What is different about passing in a list as an argument?

Read about list aliasing in section 3.4 of the associated reading, and write down what is happening in this case.
Remember, the associated reading is in the "SWBAT" section on moodle!
'''

'''
# Birthday Song
name = input("What is your name? ")
def birthday_song(name):
  print(f"Happy Birthday to you, Happy Birthday to you, Happy Birthday dear {name}, Happy Birthday to you.")
birthday_song(name)
'''

import random
def random_card():
  number = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
  suit = ['hearts','diamonds','spades','clubs']
  random_number = random.choice(number)
  random_suit = random.choice(suit)
  card = []
  card.append(f"{random_number} of {random_suit}")
  print(card)
def hand():
  [random_card(),random_card(),random_card(),random_card(),random_card()]
hand()








