gamestop = []

# print(world)
for i in range(15):
    gamestop.append(i + 1)
    # print(world)
# print(world)

gamestopNames = [
    'XBox Consoles',
    'PS5 Consoles',
    'Nintendo Consoles',
    'Monitors',
    'XBox Controllers',
    'PS5 Controllers',
    'PCs',
    'XBox Games',
    'PS5 Games',
    'Nintendo Games',
    'Welcome Sign',
    'Pokemon Cards',
    'Cashier',
    'Exit',
    'Entrance'
    ]

# for i in range(len(gamestop)):
#     print(f"{gamestop[i]}: {gamestopNames[i]}")

movement = {
    1: {"Right": 2, "Down": 6},
    2: {"Right": 3, "Left": 2},
    3: {"Right": 4, "Down": 7, "Left": 2},
    4: {"RIght": 5, "Left": 3},
    
}

location = 1

moving = input("up, down left right")

if(moving in movement[location]):
    location = movement[location][moving]
    print("moved to ", location)
else:
    print("movement not possible")