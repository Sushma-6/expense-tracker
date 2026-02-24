def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")
    with open("expenses.txt", "a") as f:
        f.write(amount + "," + category + "\n")
    print("Expense Added!")

def view_expenses():
    total = 0
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                amount, category = line.strip().split(",")
                print(f"{category}: ₹{amount}")
                total += float(amount)
        print("Total Expense: ₹", total)
    except:
        print("No expenses found.")

while True:
    print("\n1. Add Expense\n2. View Expenses\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
