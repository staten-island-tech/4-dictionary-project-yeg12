
stuff = [
    {
    "name": "insurance 1 life time covering everything ",
    "price": 89320.09,
    "department": "Misc",
    "description": "covers everthing from death to lost in jungle, just buy it."
    },
    {
    "name": "sketchy surgery",
    "price": 1000000.09,
    "department": "surgery",
    "description": "fix everything, no questions asked"
    },
    {
    "name": "revenge",
    "price": 32856.09,
    "department": "revenge",
    "description": "revenge"
    }
]
total_of_cart = 0
cart = []
user = False
while user == False:
    for index, item in enumerate(stuff):
        print(index, ":", item["name"])
    want = int(input("what u wnat (number)"))
    if want == 0:
        cart.append(stuff[0])
        total_of_cart += 89320.09
    elif want == 1:
        cart.append(stuff[1])
        total_of_cart += 1000000.09
    elif want == 2:
        cart.append(stuff[2])
        total_of_cart += 32856.09
    cont = input("countiune yes,no  ")
    if input == "yes":
        user = False
    elif cont == "no":
        user = True
if user == True:
    x = 0
    for i in cart:
        print(cart[x]["name"])
        x+=1
        if x > 2:
            x=0
total = input("do u want to bill    ")
if total == "yes":
    print (total_of_cart)
elif total == "no":
    print("ok")