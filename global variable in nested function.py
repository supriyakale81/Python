price=int(input("Enter the price"))  # global variable
def shopping():
    discount=float(input("Enter the Discount : "))
    globals()['price']=price-(price*discount)  #aceessing and changing global variable
    print("Price : ",price)
    def final_price():
        print("Adding more 5% discount : ")
        nonlocal discount  # access outer function local variable
        discount = discount + 0.05
        globals()['price'] = price - (price * discount) #aceessing and changing global variable
        print("Price after more 10% discount : ",price)
    final_price()
print("price before Discount : ",price)
shopping()
print("price after Discount : ",price)



class Shopping:
    Price=int(input("Enter the price : "))  # class variable
    def discount_price(self):
        self.discount=float(input("Enter the discount"))
        Discount_Price=self.Price-(self.Price*self.discount)  #aceessing and changing class variable
        print("Price : ",Discount_Price)
    def final_price(self):
        print("Adding more 5% discount : ")
        self.discount = self.discount + 0.05
        final_Price = self.Price - (self.Price * self.discount) #aceessing and changing class variable
        print("Price after more 5% discount : ",final_Price)
        # final_price(self)

S=Shopping()
S.discount_price()
S.final_price()








