from company import *
#from company import *
def menu():
    print("====================MENU====================")
    print("[1] Add product items to the warehouse.")
    print("[2] Add a new supermarket to the management system.")
    print("[3] List of items in the warehouse based on expiry date.")
    print("[4] Clear an item from the warehouse.")
    print("[5] Distribute products from the warehouse to a supermarket.")
    print("[6] Generate a report about the sales status of the warehouse.")
    print("[7] Exit.")

def ListOfItemsInWharehouseBasedOnExpiryDate():
    inputDate = input("Please enter the date (dd/mm/yyyy): ")
    myCompany.listItems_ExpiryDate(inputDate)
    
def menuOptions(choice):
    if choice == 1:
        myCompany.getwarehouseComp().addItemToWaerhouse()
    elif choice == 2:
        myCompany.addSupermarketToSystem()
    elif choice == 3:
        ListOfItemsInWharehouseBasedOnExpiryDate()
    elif choice == 4:
        myCompany.getwarehouseComp().clearItem()
    elif choice == 5:
        myCompany.distibuteItems()
    elif choice == 6:
        myCompany.getwarehouseComp().GenerateReport()
    elif choice == 7:
        print("The program ended.")


print("This is a managemet software system to mange the product items in a wharhouse and the distribution of these products to the supermarkets.")
companyName = input("Please enter the name of the company: ")
myCompany = company(companyName)
while 1:
    menu()
    try:
        choice = int(input("Choose one of these options to continue: "))
        if((choice < 1) | (choice > 7)):
            print("Option not defined.")
            print("Please try again...")
            continue
    except ValueError:
        print("Error in entering the type of data...")
        print("Please try again...")
        continue
        
    menuOptions(choice)
    if choice == 7:
        break


