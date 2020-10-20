arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sumOdds():
    total = 0
    for number in arr:
        if number % 2 == 1:
            total = total + number 
    return total       

print(sumOdds())

