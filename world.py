budget = 2000
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
    1: {"Xbox Series X": 499, "Xbox Series S": 299},
    2: {"PS5 Standard": 499, "PS5 Digital Edition": 399},
    3: {"Nintendo Switch": 299, "Nintendo Switch Lite": 199, "Nintendo Switch OLED": 349},
    4: {"27\" 144Hz Monitor": 299, "32\" 4K Monitor": 399, "Curved Gaming Monitor": 349},
    5: {"Xbox Wireless Controller": 69, "Xbox Controller Elite": 179},
    6: {"PS5 DualSense Controller": 74, "PS5 Controller Charging Station": 30},
    7: {"Gaming PC Tower": 1299, "High-End Laptop": 1799},
    8: {"Halo Infinite": 59, "Forza Horizon 5": 59, "Starfield": 69},
    9: {"God of War Ragnarök": 69, "Final Fantasy XVI": 69, "Spider-Man 2": 69},
    10: {"Zelda Tears of the Kingdom": 59, "Mario Kart 8": 59, "Animal Crossing": 59},
    11: {},
    12: {"Pokémon Booster Packs": 4, "Charizard Holo": 50, "Base Set Packs": 200},
    13: {},
    14: {},
    15: {}
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
    global budget
    availableProducts = returnProducts(locNum)
    if len(availableProducts) == 0:
        print("No products available here.")
        return
    print(f"You're budget is ${budget}")
    print("Available products:")
    for idx, product in enumerate(availableProducts, start=1):
        print(f"{idx}. {product} - ${availableProducts[product]}")
    choice = input("Type the number of the product to add to your cart (or '0' to cancel): ")
    
    while choice != 0:
        try:
            choice = int(choice)
            
            if choice == 0:
                return
            if 1 <= choice <= len(availableProducts):
                product_names = list(availableProducts.keys())
                product_price = availableProducts[product_names[choice - 1]]
                
                if budget - product_price < 0:
                    print(f"Insufficient budget! This item costs ${product_price} but you only have ${budget}.")
                else:
                    shoppingCart.append(product_names[choice - 1])
                    print(f"{product_names[choice - 1]} added to your cart.")
                    budget -= product_price
                    print(f"Remaining budget: ${budget}")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
        choice = input("Type the number of the product to add to your cart (or '0' to cancel): ")

def returnItemsInCart():
    global location, budget, shoppingCart

    if location != 13:
        print("You can only return items at the cashier.")
        return
    
    if not shoppingCart:
        print("Your cart is empty. Nothing to return.")
        return
    
    print("Items in your cart:")
    for idx, item in enumerate(shoppingCart, start=1):
        # Find the price of the item
        price = 0
        for location_id, location_products in products.items():
            if item in location_products:
                price = location_products[item]
                break
        print(f"{idx}. {item} - ${price}")
    
    choice = input("Type the number of the item to return (or '0' to cancel): ")
    while choice != 0:
        try:
            choice = int(choice)
            
            if choice == 0:
                return
            if 1 <= choice <= len(shoppingCart):
                returned_item = shoppingCart[choice - 1]
                # Find the price of the returned item
                refund_amount = 0
                for location_id, location_products in products.items():
                    if returned_item in location_products:
                        refund_amount = location_products[returned_item]
                        break
                
                shoppingCart.pop(choice - 1)
                budget += refund_amount
                print(f"{returned_item} returned! You received ${refund_amount} refund.")
                print(f"Current budget: ${budget}")
                print("\nUpdated cart:")
                if shoppingCart:
                    for idx, item in enumerate(shoppingCart, start=1):
                        # Find the price of the item
                        price = 0
                        for location_id, location_products in products.items():
                            if item in location_products:
                                price = location_products[item]
                                break
                        print(f"{idx}. {item} - ${price}")
                else:
                    print("Your cart is now empty.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")
        choice = input("Type the number of the item to return (or '0' to cancel): ")
        



def moveFunction():
    global location
    
    print(f"\n--- {returnLocName(location)} (Location {location}) ---")
    print("You can go to:")
    for direction, destination in movement[location].items():
        print(f"  {direction}: {returnLocName(destination)}")
    
    moving = input("Type direction to go (or '0' to skip): ")

    if moving == "0":
        return
    elif moving in movement[location]:
        location = movement[location][moving]
        print(f"\nMoved to {returnLocName(location)} (Location {location})")
        print("Available products:", returnProducts(location))
        selectProducts(location)
        returnItemsInCart()
    else:
        print("Movement not possible")

while True:
    moveFunction()