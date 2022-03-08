'''
###############
Lab 3.04
###############
In Your Notebook
----------------
Aliasing
--------
1.  Will updating b affect a? Explain why or why not?
a = [1, 2, 4]
b = a
-Yes it will; since a = b, changing one side will change the other, or the equality wouldn't stand.

2.  Predict what my_list list will print out when this code is run. If you are not sure check the code by copying and running it.
# input: a list of ints
# output: an int
def update_list(a_list):
    a_list[3] = "yo"
    b = a_list[4]
    b = 100
my_list = [1, 2, 3, 4, 5]
update_list(my_list)

Prediction: [1,2,3,yo,5].We don't have [1,2,3,yo,100] because we don't have a = b, only b = a[4], so aliasing doesn't work here.
Actual: [1,2,3,yo,5]

Scope
-----
Draw a stack diagram for the following:

 var_1 = "kittens"
 var_2 = "cookies"
​
 # input: a string
 # output: a string
 def my_function(my_favorite_things):
     song_lyrics = "rain drops on roses,"
     combined_song = song_lyrics + my_favorite_things
     return combined_song
​
 # input: a string
 # output: a string
 def my_function_2(item, item2):
     full_lyrics = item + "on " + item2
     full_song = my_function(full_lyrics)
     return full_song
​
my_song = my_function_2(var_1, var_2)

_main_: var_1 = "kittens", var_2 = "cookies"

my_function: song_lyrics = "rain drops on roses", "combined_song = "rain drops on roses" + 
my_function_2: 




Complete the following on your own:
-----------------------------------
Write down what (if anything) is wrong with the following code.

If there was an issue write out how to fix it. 

If you are unsure copy and run the code and fix it

Problem 1
---------
var_1 = 'cat'
var_2 = 'dog'
​
def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")
    var_2 = "cat"
​
print_out_my_favorite(var_1)
print(var_2)

Gives an error saying local variable refrenced before assignment
We need to change the second if to elif or add global var_2 and global var_1 into the function

Problem 2
---------
var_1 = 'cat'
var_2 = 'dog'
​
def print_out_my_favorite(favorite_pet):
    var_1 = 'dog'
    var_2 = 'cat'
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")
​
print_out_my_favorite(var_1)
print(var_1 + " " + var_2)

Nothing is wrong with the code unless you want to modify the global variable.

Problem 3
---------
var_1 = 'cat'
var_2 = 'dog'
​
def print_out_my_favorite(favorite_pet):
    if favorite_pet == var_1:
        print("My favorite pet is the cat.")
    if favorite_pet == var_2:
        print("My favorite pet is the dog.")
​
print_out_my_favorite(var_1)
print(var_2)

Nothing is wrong with the code unless you want to modify the global variable

In script mode
---------------------
Write a program using the following specifications
That has a global variable, my_num.

Create three functions that update my_num

add2: this function adds 2 to my_num

multiply_num: this function takes in a parameter, multiplier, and multiplies my_num by that parameter

add2_and_multiply: this function takes in a parameter, multiplier, and calls add2, then calls multiply_num.

Complete the program
--------------------
Write the following code in the main part of the program.

sets my_num to some initial value you choose

prints my_num

calls add2_and_multiply() with some argument you choose

prints the final value of my_num

Confirm that the printed values match what you expected.
'''
# Global Variable Modification Functions
my_num = 5
print(my_num)
def add2():
    global my_num
    my_num += 2
def multiply_num(multiplier):
    global my_num
    my_num = my_num * multiplier
def add2_and_multiply(multiplier):
    global my_num
    add2()
    multiply_num(multiplier)
add2_and_multiply(4)
print(my_num)







