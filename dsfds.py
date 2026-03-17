
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

price_of_stuff = 0
for index, item in enumerate(stuff):
    print(index, ":", item["name"])
want = int(input("what u wnat (number)"))
user = False
while user == False:
    if want == 0:
        print(stuff[0])
        price_of_stuff += 89320.09
        cont=input("countiune yes,no")
        if input == "yes":
            user == False
        elif cont == "no":
            user == True
    elif want == 1:
        print(stuff[1])
        price_of_stuff += 1000000.09
        cont=input("countiune yes,no")
        if input == "yes":
            user == False
        elif cont == "no":
            user == True

    elif want == 2:
        print(stuff[2]) 
        price_of_stuff += 32856.09        
        cont= input("countiune yes,no")
        if input == "yes":
            user == False
        elif cont == "no":
            user == True