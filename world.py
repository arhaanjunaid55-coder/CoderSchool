gamestop = []

# print(world)
for i in range(15):
    gamestop.append(i + 1)
    # print(world)
# print(world)

gamestopNames = [
    "",
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

products = {
    1: ["Xbox Series X", "Xbox Series S"],
    2: ["PS5 Standard", "PS5 Digital Edition"],
    3: ["Nintendo Switch", "Nintendo Switch Lite", "Nintendo Switch OLED"],
    4: ["27\" 144Hz Monitor", "32\" 4K Monitor", "Curved Gaming Monitor"],
    5: ["Xbox Wireless Controller", "Xbox Controller Elite"],
    6: ["PS5 DualSense Controller", "PS5 Controller Charging Station"],
    7: ["Gaming PC Tower", "High-End Laptop"],
    8: ["Halo Infinite", "Forza Horizon 5", "Starfield"],
    9: ["God of War Ragnarök", "Final Fantasy XVI", "Spider-Man 2"],
    10: ["Zelda Tears of the Kingdom", "Mario Kart 8", "Animal Crossing"],
    11: [],
    12: ["Pokémon Booster Packs", "Charizard Holo", "Base Set Packs"],
    13: [],
    14: [],
    15: []
}

movement = {
    1: {"Right": 2, "Down": 6},
    2: {"Right": 3, "Left": 1},
    3: {"Right": 4, "Down": 7, "Left": 2},
    4: {"Right": 5, "Left": 3},
    5: {"Left": 4, "Down": 8},
    6: {"up" : 1, "Down": 9, "Right": 7},
    7: {"Left": 6, "Right": 8, "up": 3, "Down": 11},
    8:{"Left": 7, "Up": 5, "Down": 13},
    9: { "Up": 6, "Right": 10},
    10:{"Right": 11, "Left": 9, "Down": 14},
    11:{"Left": 10, "Right": 12, "Up": 7},
    12:{"Right": 13, "Left": 11, "Down": 15},
    13:{"Up": 8, "Left": 12},
    14:{"Up": 10, "Right": 15},
    15:{"Up": 12, "Left": 14}    
}

shoppingCart = []
location = 15

def returnLocName (locNum):
    return gamestopNames[locNum]

def returnProducts(locNum):
    return products[locNum]

def selectProducts(locNum):
    availableProducts = returnProducts(locNum)
    if len(availableProducts) == 0:
        print("No products available here.")
        return
    print("Available products:")
    for idx, product in enumerate(availableProducts, start=1):
        print(f"{idx}. {product}")
    choice = input("Type the number of the product to add to your cart (or '0' to cancel): ")
    try:
        choice = int(choice)
        if choice == 0:
            return
        if 1 <= choice <= len(availableProducts):
            shoppingCart.append(availableProducts[choice - 1])
            print(f"{availableProducts[choice - 1]} added to your cart.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def moveFunction():
    global location
    moving = input("Type Where to go")

    if(moving in movement[location]):
        location = movement[location][moving]
        print("moved to ", returnLocName(location), location)
        print("Available products:", returnProducts(location))
        selectProducts(location)
    else:
        print("movement not possible")


while True:
    moveFunction()