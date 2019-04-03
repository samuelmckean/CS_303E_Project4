class Order:
    def __init__(self, size, crustType, sauceAmount, toppings, complete=False):
        self.size = size
        self.crustType = crustType
        self.sauceAmount = sauceAmount
        self.toppings = toppings
        self.complete = complete

    def completeOrder(self):
        self.complete = True


def menu(orders):
    while True:
        print("Welcome to Pie in the Sky Pizza Shoppe!")
        print("(O)rder a pizza")
        print("(F)inish an order")
        print("(D)isplay un-finished orders")
        print("(E)xit")
        menuChoice = input()
        if menuChoice == 'O' or menuChoice == 'o':
            orderPizza(orders)
        elif menuChoice == 'F' or menuChoice == 'f':
            finishOrder(orders)
        elif menuChoice == 'D' or menuChoice == 'd':
            displayOrders(orders)
        elif menuChoice == 'E' or menuChoice == 'e':
            break
        else:
            print("Type an O, F, D, or E")


def orderPizza(orders):
    # Size
    while True:
        size = input("What size pizza do you want? (S)mall, (M)edium, or (L)arge ")
        if (size == 's' or size == 'S' or size == 'm' or size == 'M' or
                size == 'l' or size == 'L'):
            break
        print("That is not a size we have. Try again")
    # Crust type
    while True:
        crust = input("What crust do you want? (H)and-tossed, (T)hin, (C)heese stuffed or (D)eep dish ")
        if (crust == 'h' or crust == 'H' or crust == 't' or crust == 'T' or
                crust == 'c' or crust == 'C' or crust == 'd' or crust == 'D'):
            break
        print("That is not a crust we have. Try again")
    # Sauce amount
    while True:
        sauce = input("How much sauce do you want? (N)one, (E)xtra, or (L)ight ")
        if (sauce == 'n' or sauce == 'N' or sauce == 'e' or sauce == 'E' or
                sauce == 'l' or sauce == 'L'):
            break
        print("That is not a level of sauce we have. Try again")
    # Toppings
    print("(E)xtra cheese, (M)ushrooms, (G)oat cheese")
    print("(T)omatoes, (P)ineapple, (F)resh veggies")
    print("(K)alamata olives, (G)reen olives, (B)lack olives")
    print("B(A)con, Pepperon(I), (H)am, Bee(F)")
    toppingList = []
    availableToppings = "E M G T P F K G B A I H F".split()
    while True:
        topping = input("Enter a topping or done: ")
        if topping.capitalize() in availableToppings:
            toppingList.append(topping)
        elif topping == "done":
            break
        else:
            print("That is not a valid input. Try again")
    # Create Order object
    thisOrder = Order(size, crust, sauce, toppingList)
    orders.append(thisOrder)
    # Display order number to user
    print("This order number is {}".format(len(orders)))


def finishOrder(orders):
    while True:
        try:
            orderNum = int(input("Please enter the order number: "))
            orders[orderNum-1].complete = True
            break
        except IndexError:
            print("That is not a valid order number. Try again")


def displayOrders(orders):
    allOrdersComplete = True # Assume all order complete initially
    for i in range(len(orders)):
        if not orders[i].complete:
            print("{} is not complete.".format(i+1))
            allOrdersComplete = False
    # If allOrdersComplete still True, print
    if allOrdersComplete:
        print("All orders complete")


def main():
    orders = []
    menu(orders)


main()
