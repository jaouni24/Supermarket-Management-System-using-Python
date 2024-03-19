from datetime import date
from products import * 
class supermarkets :
  
    def __init__(self,name,codea,address,addedDate):
        self.__Nmae=name
        self.__Code=codea
        self.__Address=address
        self.__addeddate=addedDate
        self.__product={}
    
    # -----------------------------------------------------
    #It reads the items in each supermarket.
    def readsupermarketsItems(self):
        path=self.__Code+"items.txt" # first the name of file will be codeitems.
        try:
            file1 = open(path, 'r') # open file and then 
            for line in file1: 
                if len(line)!= 1:
                  self.addItems(line.strip())  # each  line will add to dic using methoud   
            file1.close()
        except IOError: 
            open(path, 'a+') 
    
    def addItems(self, stri): # there we split string and add object of item.
        xt= stri.split(";")
        newob=products(xt[0],xt[1],xt[2],xt[3],xt[4],xt[5])
        self.__product[xt[0]]=newob
    # -----------------------------------------------------
    def addItemToSuperMarket(self,product): #product is a list
        productInfo = str(product[0])+";"+str(product[1])+";"+str(product[2])+";"+str(product[3])+";"+str(product[4])+";"+str(product[5])+"\n"
        f = open(self.__code+"items.txt", "a")
        f.write(productInfo)
        f.close()
            # there will add to werehouse>
        self.addItems(productInfo.strip())
        # after get data , we  insert to file and to list of item in werehouse.
        print("The process of addition done successfully.")
    #____________________________________________________________________________
    def getName(self):
        return self.__name
    
    def getCode(self):
        return self.__code
        
    def getAddress(self):
        return self.__address

    def getAddedDate(self):
        return self.__addedDate
    
    def getProducts(self):
        return self.__product
  
             
     
             
    