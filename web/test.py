numbers = [2,2,1,5,4,5,6,5,7,8]

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)