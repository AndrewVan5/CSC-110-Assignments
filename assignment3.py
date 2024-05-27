import doctest

def get_rectangle_area(length: float, width: float) -> float:
    
    '''
    Returns the area of a rectange with length and width as given arguments.
    >>> get_rectangle_area(10, 5)
    50
    >>> get_rectangle_area(5, 10)
    50
    >>> get_rectangle_area(5, 5)
    25
    '''
    return length * width


def get_median(num1: float, num2: float, num3: float) -> float:
    
    '''
    This function takes 3 arguments. It then returns the value that is the 
    median of the 3 numbers provided.
    
    >>> get_median(1, 1, 1)
    1
    
    >>> get_median(1, 1, 2)
    1
    >>> get_median(2, 1, 1)
    1
    >>> get_median(2, 1, 2)
    2
    
    >>> get_median(1, 2, 3)
    2
    >>> get_median(3, 2, 1)
    2
    >>> get_median(1, 3, 2)
    2
    >>> get_median(3, 1, 2)
    2
    '''    
    
    if num1 >= num2 and num1 <= num3 or num1 >= num3 and num1 <= num2:
        return num1
        
    elif num2 >= num1 and num2 <= num3 or num2 <= num1 and num2 >= num3:
        return num2
        
    else:
        return num3
    

def get_average(num1: float, num2: float, num3: float) -> float:
    
    '''
    This function takes 3 arguments. It then returns the value that is the 
    average of the 3 numbers provided.
    
    >>> get_average(1, 5, 10)
    5.333333333333333
    
    >>> get_average(10, 5, 1)
    5.333333333333333
    
    >>> get_average(1, 10, 5)
    5.333333333333333
    
    >>> get_average(5, 5, 5)
    5.0
    '''
    
    return (num1 + num2 + num3) / 3


def compare_median_average(num1: float, num2: float, num3: float):
    
    '''
    This function calculates both the median and the average of the numbers
    provided and prints which is bigger or if they're approximately the same.
    
    >>> compare_median_average(1, 5.48, 10)
    the median is 0.013333333333332753 smaller than the average
    
    >>> compare_median_average(1, 4.52, 8)
    the median is 0.013333333333332753 higher than the average
    
    >>> compare_median_average(5, 5, 5.01)
    the median and average are approximately the same
    '''
    
    median = get_median(num1, num2, num3)
    average = get_average(num1, num2, num3)
    
    if median > 0.01 + average:
        print(f'the median is {median - average:.2f} higher than the average')
        
    elif median + 0.01 < average:
        print(f'the median is {average - median:.2f} smaller than the average')
        
    else:
        print('the median and average are approximately the same')
        
        
def is_multiple(num1: int, num2: int) -> bool:
    
    '''
    This function takes 2 numbers. It then evaluates and returns if the first 
    number provided is a multiple of the second number.
    
    >>> is_multiple(10,5)
    True
    
    >>> is_multiple(5,10)
    False
    
    >>> is_multiple(5,5)
    True
    '''
    if num2 != 0:
        return num1 % num2 == 0
    
    elif num1 == 0 and num2 == 0:
        return True
    
    else:
        return False


def convert_to_multiple(n1: int, n2: int) -> int:
    
    '''
    This function checks whether or not n1 is a multiple of n2. And if it's not
    a multiple it multiplies n1 and n2 together to create a multiple of both.
    
    >>> convert_to_multiple(10,5)
    10
    
    >>> convert_to_multiple(5,10)
    50
    
    >>> convert_to_multiple(5,5)
    5
    
    '''
    
    if is_multiple(n1, n2) == True:
        return n1
    
    else:
        return (n1 * n2)
    
    
def acronym(str1: str, str2: str) -> str:
    
    '''
    This function takes 2 strings and returns the first letter of each string
    in a new string with no spaces.
    >>> acronym('Hello', 'There')
    'HT'
    
    >>> acronym('There', 'Hello')
    'TH'
    
    >>> acronym('hello', 'hello')
    'hh'
    '''
    
    if str1 == '' and str2 == '':
        first_str1_letter = str1
        first_str2_letter = str2
        
    elif str1 == '':
        first_str1_letter = str1
        first_str2_letter = str2[0]
        
    elif str2 == '':
        first_str1_letter = str1[0]
        first_str2_letter = str2
        
    else:
        first_str1_letter = str1[0]
        first_str2_letter = str2[0]
    
    return first_str1_letter + first_str2_letter


def get_shipping_cost(weight: float, length: float, width: float) -> float:
    
    '''
    This function returns the shipping cost of a letter based on the information
    about the letter entered. Weight, length, and width.
    
    >>> get_shipping_cost(0.24, 12, 10)
    2.5999999999999996
    
    >>> get_shipping_cost(0.05, 12, 10)
    1.4500000000000002
    
    >>> get_shipping_cost(0.05, 282, 1)
    1.4500000000000002
    
    >>> get_shipping_cost(0.05, 283, 1)
    1.9
    
    >>> get_shipping_cost(0.06, 282, 1)
    1.9
    
    >>> get_shipping_cost(0.1, 282, 1)
    1.9
    
    >>> get_shipping_cost(0.5, 282, 1)
    3.9
    '''
    
    area = get_rectangle_area(length, width)
    
    if area <= 282 and weight <= 0.05:
        if weight <= 0.05 and weight >= 0.03:
            cost = 1.05 + (0.02*((weight-0.03) * 1000))
        else:
            cost = 1.05
                
    else:
        if weight > 0.1:
            cost = 1.9 + (0.005*((weight-0.1) * 1000))
        else:
            cost = 1.9
                
    return cost
        