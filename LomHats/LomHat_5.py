
try:
    age = int(input('Enter your age:  '))

    menbership = input('Are you menbership? (yes/no): ')

    menbership_stadule = menbership == 'yes'


    discount = 0

    if age >= 65 and menbership_stadule:
        discount = 15
        print('You are eligible for born the senior and menber discount 15%. Thanks!')
        
    elif age >= 65:
        discount = 10
        print('You are eligible for born the senior discont 10%. Thanks!')
        
    elif menbership_stadule == True:
        discount = 5
        print('You are eligible for menbership discount 5%. Thanks! ')
        
    else:
        discount = 0
        print('You are not eligible for any discount. Thanks!')
except ValueError:
    print('Please enter your age! ')
    

        





