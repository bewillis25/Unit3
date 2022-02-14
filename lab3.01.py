'''
##############
Lab 3.01
##############
1.  Practice importing random** — Use randint with different arguments. Simulate a dice roll, printing out to the user what number they rolled.

2.  Look at the documentation of the random library — Experiment with another function (not randint) that returns a value.

3.  Create a program that simulates a magic 8-ball​
    1.  Store all of the 8-ball's possible responses (shown below) in a list

    2.  Have the program prompt the user to ask the magic 8-ball a question

        then return and print a random response.

Magic 8-Ball Response Examples
Outlook is good

Ask again later

Yes

No

Most likely no

Most likely yes

Maybe

Outlook is not good
'''

# Dice Roll Simultaion
import random
dice = random.randint(1,6)
print(f"You rolled a {dice}")

# Random Choice, picks a random value from a list
import random
list1 = [1,2,3,4,5,6]
print(random.choice(list1))

# Magic 8-ball Game
import random
list2 = ["Outlook is good","Ask again later","Yes","No","Most likely no","Most likely yes","Maybe","Outlook is not good"]
answer = input("Ask a question for the magic 8-Ball: ")
print(random.choice(list2))
