# Ask the user to enter name & age
name = input("Please enter your name:")
age = input("and now I also need you to enter your age:")
age = int(age)
# Calculate the corresponding decade and the remaining years
x = int(age / 10)
nextdecade = (x + 1) * 10
remain = nextdecade - age
# tell the user in how many years he/she will reach the next decade
print("{}, in {} years you will be {}.".format(name,remain,nextdecade))
