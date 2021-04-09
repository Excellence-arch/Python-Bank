import random

details = {}
new_det = ["username", "email", "firstname", "lastname", "password", "amount"]
def main():
    to = ["1. Login", "2. Register", "3. Quit"]
    for i in to:
        print(i)
    what = input("please choose a number : ").lower()
    if what == "1":
        return login()
    elif what == "2":
        return reg_details()
    elif what == "3":
        quit()
    else:
        print("Invalid Input, Please try again")
        main()


def reg_details():
    user_name = input("Enter your username: ")
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password. It must be 8 characters: ")
    if len(password) != 8:
        print("Your password must be 8 characters")
        reg_details()
    else:
        amount = 50000
        no = random.randint(1000,9999)
        new = [user_name, first, last, email, password, amount]
        kins_dict=dict(zip(new_det, new))
        details[no]=dict(zip(new_det, new))
        print("Your account number is " + str(no) + " and your password is " + password + ". Please, do not lose it.")
        # print(details)
        main()

def try_again(mess, func):
    lint = [mess, "1. Yes", "2. No"]
    choose = input("Choose: ")
    for k in lint:
        print(k)
    if choose == "1":
        func
    else:
        quit()

def login():
    user = int(input("Enter your account number: "))
    if user in details.keys():
        pins = input("Enter your password: ")
        if pins in details[user]["password"]:
            print("Login Successful")
            others()


def others():
    what = ["1. Withdraw", "2. Transfer", "3. Pay Bill", "4. Check Balance", "5. Main menu"]
    for wetin in what:
        print(wetin)
    num = input("Choose a number: ")
    if num == "4":
        balance()
    elif num == "1":
        withdraw()
    elif num == "2":
        transfer()
    elif num == "3":
        pay_bill()
    elif num == "5":
        main()


def pay_bill():
    user = int(input("Enter your account Number: "))
    bal = int(input("Enter the amount you want to pay: "))
    if bal <= int(details[user]["amount"]):
        rem = int(details[user]["amount"]) - bal
        print("Transaction successful")
        details[user]["amount"] = rem
        print("Your new account balance is ", details[user]["amount"])
        perform_transaction()
    else:
        try_again("Insufficient Balance, do you wish to try again? ", withdraw())




def withdraw():
    user = int(input("Enter your account Number: "))
    bal = int(input("Enter the amount you want to withdraw: "))
    if bal <= int(details[user]["amount"]):
        rem = int(details[user]["amount"]) - bal
        print("Transaction successful")
        details[user]["amount"] = rem
        print("Your new account balance is ", details[user]["amount"])
        perform_transaction()
    else:
        try_again("Insufficient Balance, do you wish to try again? ", withdraw())



def transfer():
    user = int(input("Enter your account Number: "))
    new_user = int(input("Enter the account Number you want to transfer to: "))
    bal = int(input("Enter the amount you want to transfer: "))
    if bal <= int(details[user]["amount"]):
        print("You are trying to transfer " + str(bal) + " to " + str(details[new_user]["firstname"]) + "press 1 to continue or 2 to go back")
        fun = input("Your Choice: ")
        if fun == "1":
            rem = int(details[user]["amount"]) - bal
            mine = int(details[new_user]["amount"]) + bal
            print("You have sent " + str(details[user]["amount"]) + " to " + str(details[new_user]["firstname"] + " " + str(details[new_user]["lastname"])))
            details[user]["amount"] = rem
            details[new_user]["amount"] = mine
            print("Your new account balance is ", details[user]["amount"])
            perform_transaction()
        else:
            quit()
    else:
        try_again("Insufficient Balance, do you wish to try again? ", withdraw())

        

def balance():
    user = int(input("Enter your account Number: "))
    print("Your balance is " + str(details[user]["amount"]))
    perform_transaction()


def perform_transaction():
    lin = ["Do you want to perform another transaction? ", "1. Yes", "2. No"]
    for i in lin:
        print(i)
    used = input("Choose: ")
    if used == "1":
        others()
    elif used == "2":
        quit()
    else:
        print("Invalid Input, try again")
        perform_transaction()


main()