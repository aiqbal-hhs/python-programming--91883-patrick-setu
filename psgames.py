ps3_game = 17
ps4_game = 45

want_ps3 = int(input("How many ps3 games would you like?"))
want_ps4 = int(input("How many ps4 games would you like?"))

total_cost = ((want_ps3 * ps3_game) + (want_ps4 * 45))

print("The total cost for your order is: ${}." .format(total_cost))
