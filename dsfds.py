
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

k = 0
for index, item in enumerate(stuff):
    print(index, ":", item["name"])
want = int(input("what u wnat (number)"))
while A == False:
    if want == 0:
        print(stuff[0])
    elif want == 1:
        print(stuff[1])
    elif want == 2:
        print(stuff[2]) 
