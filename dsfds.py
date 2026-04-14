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
    "name": "for something",
    "price": 32856.09,
    "department": "nothing",
    "description": "revenging for u"
    },
    {
    "name": "china",
    "price": 328560000000.09,
    "department": "country",
    "description": "中国"
    }
]
total_of_cart = 0
cart = []
user = False
while user == False:
    for index, item in enumerate(stuff):
        print(index, ":", item["name"])
    want = int(input("what u wnat (number)"))
    cart.append(stuff[want])
    total_of_cart += stuff[want]["price"]
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