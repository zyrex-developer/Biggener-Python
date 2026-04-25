age_input = input('Enter you age: ')

try:
    age = int(age_input)
    
    if age <= 0:
        print('Catagory : Invaild input')
    else:
        if age <= 12:
            catagory = 'Child'
            print(f'Your Catagory: {catagory}')
        elif age <= 19:
            catagory = 'Teen'
            print(f'Your Catagory: {catagory}')
        elif age <= 64:
            catagory = 'Adult'
            print(f'Your Catagory: {catagory}')
        else:
            print('Your Catagory: Senior')
except ValueError:
    print('Please enter your age !')