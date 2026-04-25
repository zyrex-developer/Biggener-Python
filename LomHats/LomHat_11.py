


def get_word():
    
    print("Enter your strings one at a time. Press Enter on an empty line to finish.")

    words = []

    while True:
        word = input("Enter word (or press Enter to finish): ").strip()
        if word == "":
            break
        words.append(word)    
        
    return words

def choose_sort_option():
    
    print("\nChoose a sorting option: ")
    print("1. Alphabetical order (case-sesitive)")
    print("2. Alphabetical order (ignoring case)")
    print("3. Reverse Alphabetical order ")
    print("4. By length (shortest to longest)")

    while True:
        try:
            option = int(input("Enter option number (1-4): "))
            if option in [1 , 2 , 3 , 4]:
                return option               
            else:
                print("Invaild option. Please choose a number between 1 and 4.")
                
        except ValueError:
            print("Invaild input. Please enter a vaild number.")

def sort_words(words , option ):
    
    if option == 1:
        # ALphabetical order (case-sensisive)
        words.sort()
        
    elif option == 2:
        # Alphabecail order (ignoring case)
        words.sort(key=str.lower)
        
    elif option == 3:
        # Reverse alphabecail order
        words.sort(reverse=True)
        
    elif option == 4:
        # Sort by length
        words.sort(key=len)
        
    return words


def main():
    words = get_word()
    if not words:
        print("No words were entered. Exiting...")
        return
    
    option = choose_sort_option()
    
    sorted_words = sort_words(words=words, option=option)
    
    print("\nSorted list:")
    
    for word in sorted_words:
        print(word)
        
if __name__ == "__main__":
    main()