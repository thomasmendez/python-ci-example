# sales tax

# import tax

# calculate tax of items

# calculate total with tax

# rounded up to the nearest 0.05

# take input 

# create output 

# allow user to have input (from file or from manual input)
# following the expected format
# extract nesseary information

from item import Item

def extractItem(line):

    line = line.split(' ')

    lenght = len(line)
    quantity = line[0]
    imported = False
    cost = line[lenght-1]

    try:
        quantity = int(quantity)
    except ValueError:
        raise ValueError("Input[0] must be a integer")

    if line in ['imported']:
        imported = True

    try:
        cost = float(cost)
    except ValueError:
        raise ValueError("Input[3] should be a float")

    # create a item from info extracted
    return (Item(quantity, imported, cost))

def op():

    try:
        f = open('./input/input1.txt', "r")

        items = []

        for line in f:

            item = extractItem(line)
            items.append(item)

        f.close()

        return items

    except FileNotFoundError:
        raise FileNotFoundError("Input file does not exist")

def imp():

    items = []
    while True:
        line = input()

        # need to make sure line follows expected format
        # format: "int str at float"
        if line:

            item = extractItem(line)
            
            # add our item to list of items
            items.append(item)

        else:
            break

    # return a list of items
    return items

def impLine():

    lineLenght = input("Enter line lenght")

    imp = input("Enter line info")

    inputLine = []

    # reads through line lenght
    for i in range(lineLenght):
        inputLine.append(imp[i])
    
    inputLine = ''.join(inputLine)

    item = extractItem(inputLine)

    return item
