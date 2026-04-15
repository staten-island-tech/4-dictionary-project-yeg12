stuff = [
    {
    "name": "insurance",
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
    },
    {
    "name": "bitcoin miner",
    "price": 3285.09,
    "department": "miner",
    "description": "free bitcoin at the expenise of you eletcrial bill"
    },
    {
    "name": "gggold machine",
    "price": 3228410.09,
    "department": "gold",
    "description": "free gggold, it the ggggold machine"
    }
]
total_of_cart = 0
cart = []
user = False
while user == False:
    for index, item in enumerate(stuff):
        print(index, ":", item["name"])
    want = int(input("what u wnat (number)"))
    cart.append(stuff[want]["name"])
    total_of_cart += stuff[want]["price"]
    cont = input("countiune yes,no  ")
    if input == "yes":
        user = False
    elif cont == "no":
        user = True
if user == True:
    total = input("do u want to bill    ")
    if total == "yes":
        print (total_of_cart)
        print(cart)
    elif total == "no":
        print("ok")
        print(cart)