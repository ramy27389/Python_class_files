cart_items=['apple','orange', 'banana','Milk', 'Rice']
prices=[45,66,77,88,99]

gst_prices=[p+(p*0.5) for p in prices]
expensive_items=[(item,price) for item,price in zip(cart_items,prices) if price >40]

price_tags=["Expensive" if price>70 else "Budget friendly" for price in prices]

bill_table=[(item,price) for item,price in zip(cart_items,prices)]

def upper(name):
    return name.upper()
upper_name=[upper(b) for b in cart_items]

quantity=[1 for x in range(len(cart_items))]

print('Items in carts are: ',cart_items)
print('Base prices are: ',prices)
print("Gst appliicalble is: ",gst_prices)
print('Expensive items are: ', expensive_items)
print("price tags: ", price_tags)
print('Bill table :',bill_table)
print('Items in upper: ', upper_name)
print('Item quantity: ', quantity)
