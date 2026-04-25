menu = {
    1: {'name' : 'Bread' , 'prices' : 2.50},
    2: {'name' : 'Milk' , 'prices' : 3.0},
    3: {'name' : 'Eggs' , 'prices' : 4.00},
    4: {'name' : 'Cheese' , 'prices' : 5.00}
    
}
def Display_menu():
    print("Menu: ")
    for items_id , items_info in menu.items():
        print(f"{items_id}. {items_info['name']} - ${items_info['prices']:.2f}")

def calculate_total(cart):
    
    # total = 0 
    # for item in cart.values():
    #     total_each_item = item["prices"] * item["quantity"]
    #     total += total_each_item
    
    total = sum (item["prices"] * item["quantity"] for item in cart.values())
    
    # Apply Discount based on total amount
    if total >= 100:
        discount = 0.1
        discount_message = "10% discount applid"
        
    elif total >= 50:
        discount = 0.05
        discount_message = "5% discount applid"
        
    else:
        discount = 0
        discount_message = "0% discount appild"
        
    # discount_in_dollar = total * discount
    # discounted_total = total - discount_in_dollar  
    
    discounted_total = total * (1 - discount)
    return discounted_total, discount_message
        
        
        
        
    
        
def main():
    while True:
        cart = {} # Dictionary to store selcted items and quantity
        Display_menu()
        
      # Get user input for items seletion  

        try:
            item_number = int(input('Enter items number: '))
            
            if item_number not in menu:
                print("Invaild item number. Please try again.")
                continue
        except ValueError:
            print("Invaild input. Please enter a number. ")
            continue
            
            
        # Get quantity
        try:
            quantity = int(input("Quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero. ")
                continue
            
        except ValueError:
            print("Invaild input. Please enter a number.")
            continue
            
            
        # Add items to cart
        item = menu[item_number]
        if item_number in cart:
            cart[item_number]["quantity"] += quantity
        else:
            # cart[1] =  {"name" : item["name"] , "prices" : item["prices"], "quantity" : quantity}
            cart[item_number] = {"name" : item["name"] , "prices" : item["prices"], "quantity" : quantity} 
        
        while True:
            add_more = input("Add more?(y/n): ").strip().lower()
            if add_more in ['y' , 'n' , 'yes' , 'no']:
                break
            else:
                print("Invaild input. Please enter 'y' for yes or 'n' for no.")
                
        if add_more =='n' or add_more == 'no':
            break
            
        
    discounted_total , discount_message = calculate_total(cart=cart)           
    
    print("\nYour Cart:")
    for item in cart.values():
        print(f"{item['name']} x {item['quantity']} = ${item['prices'] * item['quantity']:.2f}")
        
    print(f"\nTotal: ${discounted_total:.2f} ({discount_message})")
        
if __name__ == "__main__":
    main()
    