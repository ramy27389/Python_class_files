def calculate_bill(amount,tax,deliverycharge):
    total=amount+(amount*tax/100)+deliverycharge
    print("Total bill amount : ", total)
def display_bill(customer_name,food_ordered,amount):
    print(customer_name,food_ordered,amount)
def thankyou(customer_name):
    print("Thank you ", customer_name)

bill=calculate_bill
display=display_bill
greet=thankyou

display("Anu","\nBurger","\n120")
bill(120,5,10)
greet("Anu")