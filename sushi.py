name = input("What is your name?")
food = input("What is your favourite food?")
num = 0

while food != "sushi":
    num += 1 * 2 
    food = input("What is your favourite food? \n" * num)

print("I agree with you {}, sushi is the best food." .format(name))
