def is_armstrong_number(number):
    p = 0
    s = 0
    n = number
    a = n
    
    # 1. Count the number of digits using integer division (//)
    while n != 0:
        n = n // 10
        p = p + 1 
        
    # 2. Calculate the Armstrong sum using exponents (**)
    while a != 0:
        r = a % 10
        s = s + (r ** p)
        a = a // 10
        
    # 3. Return True or False for Exercism to pass
    return number == s