
class products:
    
    def __init__(self,code,name,expiryDate,wholesaleCost,salesCost,Quantity):
        self.__code=code
        self.__name=name
        self.__expiryDate=expiryDate
        self.__wholesaleCost=wholesaleCost
        self.__salesCost=salesCost
        self.__Quantity=Quantity
        
    def getName(self):
        return self.__name
        
    def getCode(self):
        return self.__code
        
    def getExpiryDate(self):
        return self.__expiryDate
        
    def getwholesaleCost(self):
        return self.__wholesaleCost
        
    def getSalesCost(self):
        return self.__salesCost
    
    def getQuantity(self):
        return self.__Quantity
        
    def setQuantity(self,newValue):
        self.__Quantity=newValue
        
    def toString(self):
        print("Product Name:",self.getName(),", Code:",self.getCode(),", Expiry Date:",self.getExpiryDate(),", whole sale Cost",
        self.getwholesaleCost(),", Sale Cost: ",self.getSalesCost(),", Quantity:",self.getQuantity())

    def printItemFile(self):
        return (str(self.__code)+";"+str(self.__name)+";"+str(self.__expiryDate)+";"+str(self.__wholesaleCost)+";"+str(self.__salesCost)+";"+str(self.__Quantity)+"\n")
    
    def printItemWithoutQuantity(self):
        return (str(self.__code)+";"+str(self.__name)+";"+str(self.__expiryDate)+";"+str(self.__wholesaleCost)+";"+str(self.__salesCost)+";")


