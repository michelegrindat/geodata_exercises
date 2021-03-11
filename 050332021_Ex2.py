import random
# create a random no. between 0 and 100
random_number = random.randint(0,100)
# initate while-loop
counter = 0
while counter == 0:
# let the user guess the randomly created no.
    input_no = input("Please guess the randomly created number between 0 and 100:")
# converting the string into an integer
    input_no = int(input_no)
# assign different output messages to the values, depending on if the guessed value was higher, lower or equal the variable
    if (input_no < random_number):
        print("The number that you‘ve guessed was lower than the randomly created number, please guess again!")
    elif (input_no > random_number):
     print("The number that you‘ve guessed was higher than the randomly created number, please guess again!")
    else:
        print("Hurray, you have guessed the right number!")
        counter = 1

