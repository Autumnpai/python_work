fav_num = {
    "allan": [4, 200, 5],
    'hebe': [9,10],
    'mickey': [200, 8, 5],
    'autumn': [1_000_000, 56, 28],
    'pai': [6_523_830, 888, 1]
}

for name, num in fav_num.items():
    print(f"{name.title()}'s favorite number is: ")
    for each in num:
        print(each)
