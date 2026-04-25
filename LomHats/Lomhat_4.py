print("\nEnter the prices of three items:")

price_1 = float(input("Price ot item 1: $ "))
price_2 = float(input("Price ot item 2: $ "))
price_3 = float(input("Price ot item 3: $ "))


subtotal = price_1 + price_2 + price_3


tex = subtotal * 0.08

total_with_tex = subtotal + tex

dicount = 0
if subtotal > 50:
    dicount = total_with_tex * 0.10
    
total_after_dicount = total_with_tex - dicount


print("\n--- Itemeized Receipt ---")
print(f"Item 1: {price_1:.2f} $")
print(f"Item 2: {price_2:.2f} $")
print(f"Item 3: {price_3:.2f} $")
print(f"Subtotal: {subtotal} $")
print(f"Tex(8%) : {tex:.2f} $")
print(f"Discount (10%): -{dicount:.2f} $")
print(f"Total: {total_after_dicount} $")
