counter = 0
position_alexandra = 0
position_levon = 0

while True:
    name = input()
    counter += 1
    if name == "Александра":
        position_alexandra = counter
    elif name == "Левон":
        position_levon = counter
    if (position_alexandra != 0) and (position_levon != 0):
        break

print(max(0, position_levon - position_alexandra - 1))