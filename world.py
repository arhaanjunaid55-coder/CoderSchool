import tkinter as tk
from tkinter import messagebox

# ---------- SETTINGS ----------
budget = 2000
shoppingCart = []
location = 15

# ---------- STORE DATA ----------
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
    6: {"Up": 1, "Down": 9, "Right": 7},
    7: {"Left": 6, "Right": 8, "Up": 3, "Down": 11},
    8: {"Left": 7, "Up": 5, "Down": 13},
    9: {"Up": 6, "Right": 10},
    10: {"Right": 11, "Left": 9, "Down": 14},
    11: {"Left": 10, "Right": 12, "Up": 7},
    12: {"Right": 13, "Left": 11, "Down": 15},
    13: {"Up": 8, "Left": 12},
    14: {"Up": 10, "Right": 15},
    15: {"Up": 12, "Left": 14}
}

# ---------- HELPER FUNCTIONS ----------

def returnLocName(loc):
    return gamestopNames[loc]

def get_product_price(product):
    for loc_products in products.values():
        if product in loc_products:
            return loc_products[product]
    return 0

def calculate_cart_total():
    return sum(get_product_price(item) for item in shoppingCart)

# ---------- GAME LOGIC ----------

def change_location(direction):
    global location
    if direction in movement[location]:
        location = movement[location][direction]
        update_gui()

def add_to_cart(product):
    global budget
    price = get_product_price(product)

    if budget < price:
        messagebox.showwarning("Budget Warning", "Not enough money!")
        return

    shoppingCart.append(product)
    budget -= price
    update_gui()

def return_item():
    sel = cart_list.curselection()
    if not sel:
        return

    index = sel[0]
    item = shoppingCart.pop(index)
    refund = get_product_price(item)

    global budget
    budget += refund
    update_gui()

# ---------- GUI ----------

def update_gui():
    location_label.config(
        text=f"{returnLocName(location)}  |  Location {location}",
        fg="#00ffcc"
    )

    budget_label.config(
        text=f"Budget: ${budget}   |   Cart Total: ${calculate_cart_total()}"
    )

    # Clear direction buttons
    for widget in directions_frame.winfo_children():
        widget.destroy()

    # Create direction buttons
    for direction in ["Up", "Down", "Left", "Right"]:
        state = tk.NORMAL if direction in movement[location] else tk.DISABLED
        btn = tk.Button(
            directions_frame,
            text=direction,
            width=8,
            state=state,
            command=lambda d=direction: change_location(d),
            bg="#333",
            fg="white"
        )
        btn.pack(side=tk.LEFT, padx=5)

    # Clear products
    for widget in products_frame.winfo_children():
        widget.destroy()

    available = products[location]

    if not available:
        tk.Label(products_frame, text="No products here.", bg="#222", fg="white").pack()
    else:
        for product, price in available.items():
            btn = tk.Button(
                products_frame,
                text=f"{product}  -  ${price}",
                anchor="w",
                width=40,
                command=lambda p=product: add_to_cart(p),
                bg="#444",
                fg="white"
            )
            btn.pack(pady=2)

    # Update cart
    cart_list.delete(0, tk.END)
    for item in shoppingCart:
        price = get_product_price(item)
        cart_list.insert(tk.END, f"{item} - ${price}")

def start_gui():
    global root, location_label, budget_label, directions_frame, products_frame, cart_list

    root = tk.Tk()
    root.title("🎮 GameStore Explorer")
    root.geometry("700x600")
    root.configure(bg="#111")

    title = tk.Label(root, text="GameStore Explorer", font=("Arial", 20, "bold"),
                     bg="#111", fg="#00ffcc")
    title.pack(pady=10)

    location_label = tk.Label(root, font=("Arial", 14),
                              bg="#111", fg="white")
    location_label.pack(pady=5)

    budget_label = tk.Label(root, font=("Arial", 12),
                            bg="#111", fg="white")
    budget_label.pack(pady=5)

    directions_frame = tk.Frame(root, bg="#111")
    directions_frame.pack(pady=10)

    products_frame = tk.LabelFrame(root, text="Products",
                                   bg="#222", fg="white",
                                   font=("Arial", 12, "bold"))
    products_frame.pack(padx=10, pady=10, fill="both")

    cart_frame = tk.LabelFrame(root, text="Shopping Cart",
                               bg="#222", fg="white",
                               font=("Arial", 12, "bold"))
    cart_frame.pack(padx=10, pady=10, fill="both")

    cart_list = tk.Listbox(cart_frame, width=60, height=6,
                           bg="#333", fg="white")
    cart_list.pack(pady=5)

    tk.Button(cart_frame, text="Return Selected Item",
              command=return_item,
              bg="#aa3333", fg="white").pack(pady=5)

    update_gui()
    root.mainloop()

if __name__ == "__main__":
    start_gui()
