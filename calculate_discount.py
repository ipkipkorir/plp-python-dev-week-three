#create a function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (discount_percent/100*price)
        return final_price
    else:
        return price
    
#prompt the user for inputs
price = int(input("\nEnter the price: \n"))
discount_percent = int(input("\nEnter percentage discount of price: \n"))

#call the function
print(calculate_discount(price, discount_percent))    