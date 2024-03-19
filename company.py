from supermarkets import * 
from warehouse import *

class company:
    def __init__(self,name):
        self.__name=name
        self.__warehouseComp=warehouse()
        self.__supermarketsComp={}
        self.startread()
# When creating any company, you must have a file for the names of its supermarkets (file name: company name + supermarket) and each supermarket has a file for the items inside it (file name: supermarket name + items).
# The process of obtaining this data:

   # When making any object from the company class, a reading will be performed from the store file as well as the supermarket
    def startread(self):
        self.__warehouseComp.readWaerhouse(self.__name+"warehouse_items.txt")
        self.readsupermarkets()

#     We try to access the supermarket data at the beginning. If the company already exists, we will refer to it، else we will create it .
# the next code in company class .
    def readsupermarkets(self):    
        try:
            file1 = open(self.__name+"supermarkets.txt", 'r')
            for line in file1: 
                x = line.strip().split(";")
                newob=supermarkets(x[1],x[0],x[2],x[3])
                newob.readsupermarketsItems() # will read the list of item in supermarket
                self.__supermarketsComp[x[0]]=newob  #code will be in x[1], add this supermarkt to dic of comp.
            file1.close()
        except IOError: 
            open(self.__name+"supermarkets.txt", 'a+') 
            
    #--------------------------------------------------------------------------------------------
#     We start reading the data from the file, and each line is a supermarket  so we will create object supermarket then add to supermarket dictionary.
# using this code 
    def addSupermarketToSystem(self):
        state=0
        statment=""
        code = input("Enter supermarkt's code (must be of four characters):")
        while(state!=1):
            if len(code)==4:
                state=1  
                statment=statment+code+";"
                Name = input("Enter supermarkt's Name:")
                statment=statment+Name+";"           
                address = input("Enter supermarkt's Address:")
                statment=statment+address+";"      
                addedDate = date.today().strftime("%d/%m/%Y")
                statment=statment+addedDate+"\n"
                newObj = supermarkets(Name,code,address,addedDate)
                newObj.readsupermarketsItems()
                f = open(self.__name+"supermarkets.txt", "a") 
                f.write(statment)
                f.close() 
#                 We start reading the data from the file, and each line is a supermarket  so we will create object supermarket then add to supermarket dictionary.
# using this code 
                self.__supermarketsComp[code] = statment
                # after get data , we  insert to file and to list of item in werehouse.
                print("The process of addition done successfully.")
                
            else:
                print("The code is incorrect, it should be 4 characters.")
                code = input("Enter supermarkt's code:")
                
    def listItems_ExpiryDate(self,date): # after we get the list of expared day , we will
        expiredProducts = self.__warehouseComp.listOfItemsBasedOnExpiryDate(date)
        totalWholeSaleCost = 0.0
        SaleCost = 0.0
        for key in expiredProducts:
            totalWholeSaleCost += float(expiredProducts[key].getwholesaleCost()) *float(expiredProducts[key].getQuantity())
            SaleCost += float(expiredProducts[key].getSalesCost())*float(expiredProducts[key].getQuantity())    
            expiredProducts[key].toString()
            
        print("Whole Sale Cost: ",totalWholeSaleCost)
        print("Sales Cost: ",SaleCost)
        
        
    def distibuteItems(self):
        while 1:
            supermarketCode = input("Please enter supermarket's code, If you want to cancel this operaion enter -1: ")
            if str(supermarketCode.strip()) in str(self.__supermarketsComp): #test if the supermarket code exist in the dictionary of supermarkets 
                print(" This supermarket found in company ")
                try:
                    #if the code entered is existed then open the file the contains the requested items 
                    file = open("DistributeItems_"+supermarketCode+".txt",'r')
                    print("this DistributeItems found \n")
                    for line in file.readlines():
                        print("\n"+line)
                        listFile = line.rstrip("\n").split(";") #this list contains a list of code and quantity    
                        if (listFile[0] in self.__warehouseComp.getProducts()): #item in the file exist in the warehouse
                            obj = self.__warehouseComp.getProducts() #dictionary of the products in the warehouse    
                            print("this information to this code product :")
                            obj[listFile[0]].toString()
                            #The software, will then check the warehouse and distribute the requested quantities of each item. if the requested quantities less than wherehouse will add these items to the list of items available at the supermarket and remove them from the warehouse.
#                           If the item is already in the store, we will clean the previous quantity, but if the item is new, we will work on creating it from the beginning.

                            if int(obj[listFile[0]].getQuantity()) >= int(listFile[1]): #listFile[1] is the quantity of the product 
                                print("requested quantities less than wherehouse \n")
                                objQuantity = int(obj[listFile[0]].getQuantity()) - int(listFile[1])
                                obj[listFile[0]].setQuantity(int(objQuantity)) 
                                supermarketProducts = self.__supermarketsComp[supermarketCode].getProducts()  #returns dictionary
                                if listFile[0] in supermarketProducts:
                                    supermarketProducts[listFile[0]].setQuantity(int(supermarketProducts[listFile[0]].getQuantity()) + int(listFile[1]))
                                else:
                                    string = obj[listFile[0]].printItemWithoutQuantity()+str(listFile[1])
                                    self.__supermarketsComp[supermarketCode].addItems(string)
                                print(" the oparation done ^_^")
                            # If the requested quantity of any item is not enough, the software will distribute only the available quantity. It will also print on the screen, a message about the item and the number of requested but not distributed quantities of this item.        
                            elif int(obj[listFile[0]].getQuantity()) < int(listFile[1]):
                                objQuantity = int(listFile[1]) - int(obj[listFile[0]].getQuantity()) 
                                supermarketProducts = self.__supermarketsComp[supermarketCode].getProducts()  #returns dictionary
                                if listFile[0] in supermarketProducts:
                                    supermarketProducts[listFile[0]].setQuantity(int(supermarketProducts[listFile[0]].getQuantity()) + int(obj[listFile[0]].getQuantity()))
                                else:
                                    string = obj[listFile[0]].printItemWithoutQuantity() + str(obj[listFile[0]].getQuantity())
                                    self.__supermarketsComp[supermarketCode].addItems(string)
                                obj[listFile[0]].setQuantity(int(0)) 
                                print("The requested quantity is not enough the software will distribute only the available quantity in the warehouse.") 
                                print("The number of unavailable quantity that product is:",objQuantity)  
                        # If an item is not available at the warehouse or the code is wrong, the software should print a message on the screen with the code of this item and the requested amount on screen.
                        else:
                            print(listFile[0],"does not exist in the warehouse!")
                    file.close()
                    # After basically completing the basic process and setting the appropriate values ​​in the itemsupermarket as well as the warehouse, we should update the files we have.
                    self.__warehouseComp.printinFile()  
                    file = open(supermarketCode+"items.txt","w")
                    for value in self.__supermarketsComp[supermarketCode].getProducts().values():
                        file.write(value.printItemFile())
                    file.close()
                    break
                    
                except IOError:
                    print("\nThere is no ( DistributeItems_<SupermarketCode>.txt) for this supermarket”!")
                    print("Please try again...\n")
                
            elif str(supermarketCode) == "-1":
                break
                
            else:
                print("\nThis supermarket does not exit in our company.")
                print("Please try again...\n")
                
        
    #--------------------------------------------------------------------------------------------          
    def getNameCompany(self):
        return self.__name   
    def getwarehouseComp(self):
        return self.__warehouseComp
      
       
    