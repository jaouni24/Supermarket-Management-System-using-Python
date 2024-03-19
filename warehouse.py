from products import *
class warehouse:
    def __init__(self):
        self.__product={} 
    
    def getProducts(self):
        return self.__product
    
    def addItems(self, str1):
        x = str1.split(";")
        newob=products(x[0],x[1],x[2],x[3],x[4],x[5])
        self.__product[x[0]]=newob
    
     # this to read all old data find in werehouse.    
    def readWaerhouse(self,path):
        self.__namefile=path
        try:
            file1 = open(path, 'r')
            for line in file1: 
                self.addItems(line.strip())    
            file1.close()
        except IOError: 
            open(path, 'a+') 
            
        
 # 1) Add a product item to the warehouse  
    def addItemToWaerhouse(self):
        stat=0
        statment=""
        code = input("Enter code of items:")
        while(stat!=1):
            if len(code)==4:
                stat=1
                statment=statment+code+";"
                Name = input("Enter Name of items:")
                statment=statment+Name+";"
                data1 = input("Enter Item Expiry Date:")
                statment=statment+data1+";"
                cost1 = input("Enter Item Wholesale Unit Cost:")
                statment=statment+cost1+";"
                cost2 = input("Enter Item Sales Unit Cost:")
                statment=statment+cost2+";"
                qua = input("Enter Item Quantity:")
                statment=statment+qua+"\n"
                f = open(self.__namefile, "a")
                f.write(statment)
                f.close()
                # there will add to werehouse>
                self.addItems(statment.strip())
                # after get data , we  insert to file and to list of item in werehouse.
                print(" The process of adding has been completed successfully, the information of the adder is as follows:")
                self.getProducts()[code].toString()
                # print(statment)
            else:
                print("the code incorrect, should be 4 digital .")
                code = input("Enter code of items:")

    # 4. Clear an item from the warehouse
    #1. The software should ask the user to input the code of an item;
    def clearItem(self):
        while 1:
            code = input(" input the code of an item , or 0 to exit : ")
            if code in self.__product:
                self.__product[code].toString()
                #will ask the user to input the quantity that needs to be cleared (which should be at most the available quantity)
                while 1:
                    try:
                        reqQuantity=int(input("input the quantity that needs to be cleared , or 0 to not clear"))
                        if((reqQuantity >=0) & (reqQuantity <= int(self.__product[code].getQuantity()))):
                            self.__product[code].setQuantity(int(self.__product[code].getQuantity())-int(reqQuantity))
                            #after claer , will change the value in file . so we should print all data after that.
                            #instedd to do print every time, before  exit from progream , i will change all file .
                            print("claer done ^_^ .")
                            break
                        else:
                            print("not available quantity ")
                    except ValueError:
                        print("Error in entering the type of data...")
                        print("Please try again...")
                        continue
                       
                continue
            elif code == '0':
                break
            else :
                print("Error , this code not found ")
                print("Please try again , or 0 to exit ")
                continue
        self.printinFile()

    # 6. Generate a report about the sales status of the warehouse
# Number of items in the warehouse;
# Total wholesale cost of all items in the warehouse;
# Total sales cost of all items in the warehouse;
# Expected profit after selling all items in the warehouse.
    def GenerateReport(self):
        counterItem=0
        totalwholesalecost=0
        TotalSalesCost=0
        for value in self.__product.values(): # get loop off all proudect in warehouse
            counterItem=counterItem+float(value.getQuantity()) # get the number of item  .
            totalwholesalecost=totalwholesalecost+(float(value.getwholesaleCost())*float(value.getQuantity())) # gat the sum ......
            TotalSalesCost=TotalSalesCost+(float(value.getSalesCost())*float(value.getQuantity()))
        print(" \n Number of items in the warehouse=" ,counterItem)
        print("  Total wholesale cost=" ,totalwholesalecost)
        print("  Total sales cost=" ,TotalSalesCost)
        profit=TotalSalesCost-totalwholesalecost
        fprofit = '{0:.4f}'.format(profit)
        print("  Expected profit after selling all items =" ,fprofit)

    def printinFile(self):   # we will use this tp print proudect  warehouse in file
        file = open(self.__namefile,"w")
        for value in self.__product.values():
            file.write(value.printItemFile())
        file.close()
#---------------------------------------------------------------------------------------------------------------------
    def listOfItemsBasedOnExpiryDate(self,date):  
        expiredProducts = {} 
        for key in self.__product:  
            counter = 2
            temp = self.__product[key]
            dateOfProduct = temp.getExpiryDate()
            listDate = dateOfProduct.split("/") #contanis list of date for the date in the dictionary           
            listDateInput = date.split("/") #contanis list of date for the intput date           
            while counter >= 0:
                if int(listDate[counter]) < int(listDateInput[counter]):
                    expiredProducts[key] = self.__product[key]  
                    break
                elif int(listDate[counter]) == int(listDateInput[counter]):
                    counter -= 1
                else:
                    break
                
        return expiredProducts   