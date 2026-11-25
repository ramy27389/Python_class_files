balance = 6000
amount=int(input("enter the withdrawal amount:"))

if amount<=balance:
    if amount%100==0:
        balance-=amount
        print("Transaction success \nRemaining balance is: Rs",balance)
    else:
        print("Enter multiples of 100")
else:
    print("insufficient balance")
