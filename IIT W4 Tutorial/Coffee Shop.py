# Weolcome message
print("Welcome to python Coffee Shop!")

# Ask for a name
customer_name = input("What is your name?")
print("Hello, "+customer_name+"! Let's order some coffee.")

# Setting Prices for the coffee
price_coffee = 3.50
price_latte = 4.00
price_mocha = 5.00

flag = input("Would you like to make an order: (yes/no):")

while flag == "yes":
    print("Coffee: $"+str(price_coffee))
    print("Latte: $"+str(price_latte))
    print("Mocha: $"+str(price_mocha))

    # Print out the menu
    menu_items = ['coffee','latte','mocha']
    print("Our menu: ",menu_items)

    # Ask user to choose an option
    choice = input("What would you like to order? (coffee/latte/mocha)")

    # Set the cost variable based on choice
    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "mocha":
        cost = price_mocha
    else:
        print("Sorry, we do not have that.")
        cost = 0

    if cost != 0:          
    # Ask user for quantity and convert to whole number or integer
        quantity = int(input("How many cups would you like"))

        # Calculate the total cost
        total_cost = cost * quantity

        # Ask if the customer is a student. If yes, take 10% off the total.
        student = input("Are you a student? (y/n):")

        # User gets one dollar discount if quantity is more than 1
        if quantity > 1:
            print("You get a discount of $1.00!")
            total_cost -= 1
            
        # Apply 10% student discount
        if student == "y":
            print("You get a 10% discount!")
            total_cost -= (0.10 * total_cost)

        # Print the total cost to the user
        print("Your total is: $"+str(total_cost))
    

    # Update statement for the loop
    flag = input("Would you like to make an order: (yes/no)/; ")

print("Thank you, "+customer_name+"! Please come again.")


