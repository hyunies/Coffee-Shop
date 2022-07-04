# This code allows users to choose an item and quantity from a menu and calculates cost, tax and final cost

# Creating functions
# This function makes the program not case-sensitive and allows the program to be robust to leading and trailing spaces, including cases when multiple spaces separate words in input lines
def formatInput(textLine):
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine

# Assigning variables
egg = 0.99
bacon = 0.49
sausage = 1.49
hashbrown = 1.19
toast = 0.79
coffee = 1.09
tea = 0.89

# Assigning variable cost to 0
cost = 0

# While loop for inputting user's items and item quantity
while True:
    while True:
        choice = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
        choice = formatInput(choice)
        if choice not in ('q', 'small breakfast', 'regular breakfast', 'big breakfast', 'egg', 'bacon', 'sausage', 'hash brown', 'toast', 'coffee', 'tea'):
            continue
        else:
            break

    if choice == 'q':
        break

    while True:
        quantity = input("Enter quantity: ")
        if not quantity.isnumeric():
            continue
        else:
            break

    quantity = int(quantity)

    if choice == 'egg':
        cost += egg*quantity
    elif choice == 'bacon':
        cost += bacon*quantity
    elif choice == 'sausage':
        cost += sausage*quantity
    elif choice == 'hash brown':
        cost += hashbrown*quantity
    elif choice == 'toast':
        cost += toast*quantity
    elif choice == 'coffee':
        cost += coffee*quantity
    elif choice == 'tea':
        cost += tea*quantity
    elif choice == 'small breakfast':
        cost += quantity * (egg*1 + hashbrown*1 + toast*2 + bacon*2 + sausage*1)
    elif choice == 'regular breakfast':
        cost += quantity * (egg*2 + hashbrown*1 + toast*2 + bacon*4 + sausage*2)
    elif choice == 'big breakfast':
        cost += quantity * (egg*3 + hashbrown*2 + toast*4 + bacon*6 + sausage*3)

# Printing cost
print("Cost: $%.2f" % cost)

# Calculating and printing tax
tax = (cost*0.13)
roundedTax = tax
print("Tax: $%.2f" % roundedTax)

# Calculating and printing total
totalCost = (cost*1.13)
print("Total: $%.2f" % totalCost)
