fisrt_name = input("Enter your fisrt name: ").strip()  # strip cut spece
last_name = input("Enter your last name: ").strip()  

full_name = f"{fisrt_name} {last_name}"

small_full_name = full_name.title()

char_name = len(full_name.replace(" " , ""))

nickname = (fisrt_name[:3] + last_name[:3]).lower()

print("\nRusulf: ")
print(f"Full Name: {full_name}")
print(f"Full Name in title case: {small_full_name}")
print(f"Number of charcters (excluding specse): {char_name}")
print(f"Nickname: {nickname}")