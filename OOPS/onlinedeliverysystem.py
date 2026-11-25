class User:
    def __init__(self,customer_name):
        self.customer_name=customer_name
        print(f'User created : {self.customer_name}')
class Order(User):
    def __init__(self,customer_name,food_item):
        super().__init__(customer_name)
        self.food_item=food_item
        print(f'Order created : {self.food_item}')
class Delivery(Order):
    def __init__(self,customer_name,food_item,distance):
        super().__init__(customer_name,food_item)
        self.distance=distance
        print(f'Delivery distance is {self.distance} kms')

    def delivery_charge(self):
        if self.distance<=3:
            return 20
        else:
            return 20+(self.distance-3)*5
            
name=input('Enter customer name                  :')
food=input('Enter fooditem name                  :')
distance=int(input('Enter travel distance in kms :'))

order1=Delivery(name,food,distance)
charge1=order1.delivery_charge()

print("Final bill amount is                      : ", order1.customer_name)
print("Food item ordered is                      : ",order1.food_item)
print("Delivey distance is                       : ",order1.distance)
print("Delivey charge is                         : ",charge1)
