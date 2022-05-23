class customer:
    def __init__(self,name,age,nid,address):
        self.name = name
        self.age = age
        self.nid = nid
        self.address = address
    def update(self):
        
        print("Customer name: {} Age: {} Nid: {} Address: {}".format(self.name,self.age,self.nid,self.address) )
       
    

class savings_amounts():
    def __init__(self,amount):
        self.amount =amount
        #print(self.amount)
    
    def widthdraw(self,widthdraw_amount):
        if self.amount>widthdraw_amount:
            total = self.amount-widthdraw_amount
            print(total)
        else:
            print("Insufficient balance")
    
    def deposite(self,deposit_amount):
        sum = self.amount+deposit_amount
        print(sum)
  

ob1 = customer("samin",24,111111,"cpmilla")
ob = savings_amounts(1200)
ob.widthdraw(1000)
ob1.update()
