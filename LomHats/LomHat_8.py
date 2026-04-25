numbers = list(map(int, input('Enter Number: ').split()))[:5]
 
evens = []
sum_odds = 0

for num in numbers:  # Note We use Loop We must create object . EX for New_name in Your_object
    if num % 2 == 0:
        evens.append(num)
    else:
        sum_odds = sum_odds + num
        
    print('Evens numbers: ' , evens)
    print('Sun of odd number:' , sum_odds)