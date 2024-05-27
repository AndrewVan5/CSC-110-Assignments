import doctest

def print_qualification_status(time: float, qualitime: float):
    
    '''
    This function takes time achieved and minimum qualification time. 
    It then prints if competitor qualified or not, and by how much.
    The result is rounded to 2 decimals.
    
    >>> print_qualification_status(29.99, 30)
    You qualified at 0.01 seconds below qualifying time
    
    >>> print_qualification_status(30, 30)
    You qualified at 0.00 seconds below qualifying time
    
    >>> print_qualification_status(30.01, 30)
    You missed qualifying by 0.01 seconds
    '''
    
    pass_difference = qualitime - time
    fail_difference = time - qualitime
    
    if qualitime >= time:
        print(f'You qualified at {pass_difference:.2f} seconds below qualifying time')
        
    else:
        print(f'You missed qualifying by {fail_difference:.2f} seconds')
        
    
def print_median(num1: float, num2: float, num3: float):
    
    '''
    This function takes 3 numbers. It then prints the value that is the median
    of the 3 numbers provided.
    
    >>> print_median(1, 1, 1)
    1
    
    >>> print_median(1, 1, 2)
    1
    >>> print_median(2, 1, 1)
    1
    >>> print_median(2, 1, 2)
    2
    
    >>> print_median(1, 2, 3)
    2
    >>> print_median(3, 2, 1)
    2
    >>> print_median(1, 3, 2)
    2
    >>> print_median(3, 1, 2)
    2
    '''
    
    if num1 >= num2 and num1 <= num3 or num1 >= num3 and num1 <= num2:
        print(num1)
        
    elif num2 >= num1 and num2 <= num3 or num2 <= num1 and num2 >= num3:
        print(num2)
        
    else:
        print(num3)
        
        
def print_triangle_type(a: float, b: float, c: float):
    
    '''
    This function takes 3 numbers which represent the sides of a triangle. 
    It then prints what type of triangle is formed with those side lengths.
    
    >>> print_triangle_type(5, 5, 5)
    equilateral
    
    >>> print_triangle_type(5, 5, 4)
    isosceles
    >>> print_triangle_type(4, 5, 5)
    isosceles
    >>> print_triangle_type(5, 4, 5)
    isosceles
    
    >>> print_triangle_type(4, 5, 6)
    scalene
    >>> print_triangle_type(4, 6, 5)
    scalene
    >>> print_triangle_type(6, 4, 5)
    scalene
    >>> print_triangle_type(6, 5, 4)
    scalene
    '''
    
    if a == b and b == c:
        print('equilateral')
        
    elif a == b or b == c or a == c:
        print('isosceles')
        
    else:
        print('scalene')

        
def is_multiple_of(n1: int, n2: int):
    
    '''
    This function takes 2 numbers. It then evaluates if the first number
    provided is a multiple of the second number.
    
    >>> is_multiple_of(10, 5)
    10 is a multiple of 5
    >>> is_multiple_of(50, 2)
    50 is a multiple of 2
    
    >>> is_multiple_of(10, 4)
    10 is not a multiple of 4
    >>> is_multiple_of(50, 3)
    50 is not a multiple of 3
    '''
    
    if n1 % n2 == 0:
        print(f'{n1} is a multiple of {n2}')
    
    else:
        print(f'{n1} is not a multiple of {n2}')
        

def print_roadside_penalty(alcohol_percent: int, incident_number: int, breath_sample: bool):
    
    '''
    This function takes blood alcohol percent, incident number, and a boolean
    for if the breath sample was denied or not.
    It then evaluates the appropriate penalty for the crime committed.
    
    >>> print_roadside_penalty(49, 2, True)
    no penalty
    
    >>> print_roadside_penalty(49, 2, False)
    Driving Prohibition Length: 90 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1430
    
    >>> print_roadside_penalty(80, 1, True)
    Driving Prohibition Length: 90 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1430
    
    >>> print_roadside_penalty(50, 1, True)
    Driving Prohibition Length: 3 days
    Vehicle Impoundment Length: 3 days
    Penalties and fees: $600
    
    >>> print_roadside_penalty(79, 2, True)
    Driving Prohibition Length: 7 days
    Vehicle Impoundment Length: 7 days
    Penalties and fees: $780
    
    >>> print_roadside_penalty(50, 3, True)
    Driving Prohibition Length: 30 days
    Vehicle Impoundment Length: 30 days
    Penalties and fees: $1330
    '''
        
    if alcohol_percent >= 80 or breath_sample == False:
        print('Driving Prohibition Length: 90 days\nVehicle Impoundment Length: 30 days\nPenalties and fees: $1430')
        
    elif alcohol_percent < 50:
        print('no penalty')    
    
    elif incident_number == 1:
        print('Driving Prohibition Length: 3 days\nVehicle Impoundment Length: 3 days\nPenalties and fees: $600')
        
    elif incident_number == 2:
        print('Driving Prohibition Length: 7 days\nVehicle Impoundment Length: 7 days\nPenalties and fees: $780')
        
    elif incident_number >= 3: 
        print('Driving Prohibition Length: 30 days\nVehicle Impoundment Length: 30 days\nPenalties and fees: $1330')
        

    
    
