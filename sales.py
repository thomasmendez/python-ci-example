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

def imp():

    items = []
    while True:
        line = input()

        # need to make sure line follows expected format
        # format: "int str at float"
        if line:

            line = line.split(' ')

            lenght = len(line)

            quantity = line[0]
            imported = False
            cost = line[lenght-1]

            try:
                int(quantity)
            except ValueError:
                print("Input[0] must be a integer")

            if line in ['imported']:
                imported = True

            try:
                float(cost)
            except:
                print("Input[3] should be a float")

            # create a item from info extracted
            item = Item(quantity, imported, cost)

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

    inputLine = inputLine.split(' ')

    lenght = len(inputLine)

    quantity = inputLine[0]
    imported = False
    cost = inputLine[lenght-1]

    try:
        quantity = int(quantity)
    except ValueError:
        print("Input[0] must be a integer")

    if inputLine in ['imported']:
        imported = True

    try:
        cost = float(cost)
    except:
        print("Input[3] should be a float")

    # create a item from info extracted
    return Item(quantity, imported, cost)