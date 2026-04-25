import random

number = random.randint(1, 10)

Play = 3

print(' ===Welcome to Number Guessing Game=== ')


while Play > 0:
    try:
        guess = int(input('Enter your number (1-10): '))
    except ValueError:
        print('Please enter a number (1-10)! ')
        continue
        
    if guess == number:
        print(f'You are Winwer! with number " {number} "')
        break           
    else:
        Play -= 1
        if guess < number:
            print(f'Too low! ({Play} left)')
        else:
            print(f'Too high! ({Play} left)')
           
else:
    print(f'The number was : {number} Try later.')
    
            
        

    
    