# Initial global variables
import random
name = input("What is your name? ")
month_num = 3
month_name = 'March'
day_num = 1
health_num = 5
food_num = 500 
distance_traveled = 0
miles_to_go = 2000 - distance_traveled
months_with_31_days = [1, 3, 5, 7, 8, 10, 12]
first_health_loss = random.randint(1,30)
second_health_loss = random.randint(1,30)
# Whether to change month on 30 or 31
def change_month():
    global day_num
    global month_num
    global months_with_31_days
    if month_num in months_with_31_days:
        if day_num > 31:
            month_num += 1
            day_num -= 31
    else:
        if day_num > 30:
            month_num += 1
            day_num -= 30
# Turns month_num into a name for status function
def month_name_function():
    global month_num
    global month_name
    if month_num == 3:
        month_name = 'March'
    elif month_num == 4:
        month_name = 'April'
    elif month_num == 5:
        month_name = 'May'
    elif month_num == 6:
        month_name = 'June'
    elif month_num == 7:
        month_name = 'July'
    elif month_num == 8:
        month_name = 'August'
    elif month_num == 9:
        month_name = 'September'
    elif month_num == 10:
        month_name = 'October'
    elif month_num == 11:
        month_name = 'November'
    elif month_name == 12:
        month_name = 'December'
# Tracks how many days pass for a random action
def add_day(min,max):
    global day_num
    global month_num
    global month_name
    global months_with_31_days
    global health_num
    global first_health_loss
    global second_health_loss
    global food_num
    random_days = random.randint(min,max)
    print(f"{random_days} days have passed.")
    # Health decreases randomly
    upper_bound = day_num + random_days
    if first_health_loss >= day_num and first_health_loss <= upper_bound:
        health_num -= 1
        print("You lost 1 health due to time")
    if second_health_loss >= day_num and second_health_loss <= upper_bound:
        health_num -= 1
        print("You lost 1 health due to time")
    day_num += random_days
    food_num -= random_days*5
# moves you randomly between 30-60 miles and takes 3-7 days (random)
def travel():
    global distance_traveled
    global day_num
    random_distance = random.randint(30,60)
    distance_traveled += random_distance
    add_day(3,7)
    print(f"You traveled {random_distance} miles.")
# increases health 1 level (up to 5 maximum) and takes 2-5 days (random)
def rest():
    global health_num
    global day_num
    if health_num == 5:
        print("You are already at maximum health.")
        add_day(0,0)
    elif health_num < 5:
        health_num += 1
        add_day(2,5)
        print(f"Your health is now {health_num}.")
# adds 100lbs of food and takes 2-5 days (random)
def hunt():
    global food_num
    global day_num
    food_num += 100
    add_day(2,5)
    if food_num > 500:
        food_num = 500
    else:
        food_num += 100
# lists food, health, distance traveled, and date
def status():
    global distance_traveled
    global food_num
    global health_num
    global day_num
    global month_name
    change_month()
    month_name_function()
    print(f"You have {food_num} lbs of food.")
    print(f"You have traveled {distance_traveled} miles.")
    print(f"You have {2000-distance_traveled} miles to go.")
    print(f"Your health is {health_num}.")
    print(f"The date is {month_name}, {day_num}.")
# Main game loop that determines the player's action every turn
def select_action():
    action = ''
    while health_num > 0 and action != 'quit' and food_num > 0 and month_num < 13 and distance_traveled < 2000:
        action = input(f"{name}, enter a command. Type 'help' for a list of commands: ")
        if action == 'help':
            print("travel: moves you randomly between 30-60 miles and takes 3-7 days (random) \nrest: increases health 1 level (up to 5 maximum) and takes 2-5 days (random) \nhunt: adds 100lbs of food and takes 2-5 days (random) \nstatus: lists food, health, distance traveled, and day \nhelp: lists all the commands \nquit: will end the game.")
        elif action == 'travel':
            travel()
        elif action == 'rest':
            rest()
        elif action == 'hunt':
            hunt()
        elif action == 'status':
            status()
        elif action == 'quit':
            print("Bye!")
        else:
            print("Not a valid command. Please try again: ")
select_action()
if month_num > 13:
    print("Sorry, you didn't get there in time")
    print("GAME OVER")
if distance_traveled > 2000:
    print("You made it to Oregon!")
if health_num == 0:
    print("Sorry, you have no health left and are dead")
    print("GAME OVER")
if food_num == 0:
    print("You ran out of food and starved to death")
    print("GAME OVER")














