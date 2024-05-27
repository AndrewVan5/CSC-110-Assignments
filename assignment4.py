import doctest

def get_factors(n: int) -> str:
    
    '''
    Prints all factors for the integer provided in a string seperated by commas.
    
    >>> get_factors(2)
    '1,2'
    
    >>> get_factors(0)
    ''
    
    >>> get_factors(12)
    '1,2,3,4,6,12'
    '''
    
    result = ''
    
    for row in range(1, n+1):
        
        if n % row == 0:
            result += str(row)
        
        if n % row == 0 and row != n:
            result += ','

            
    return result
        

def sum_fibonacci_sequence(n: int) -> int:
    
    '''
    Evaluates sum of fibonacci sequence n numbers in.
    
    >>> sum_fibonacci_sequence(0)
    0
    
    >>> sum_fibonacci_sequence(1)
    0
    
    >>> sum_fibonacci_sequence(2)
    1
    
    >>> sum_fibonacci_sequence(3)
    2
    
    >>> sum_fibonacci_sequence(7)
    20
    '''
    
    current = 1
    previous = 0
    next_num = 0
    sums = 0
    
    if n <= 1:
        sums = 0
    else:
        sums = 1
    
    for column in range(n-2):
            
            next_num = previous + current
            previous = current
            current = next_num
            
            sums += next_num
            
    return sums    


def factorial(n: int) -> int:
    
    '''
    Calculates and returns the sum of the factorial of n.
    
    >>> factorial(0)
    1
    
    >>> factorial(1)
    1
    
    >>> factorial(5)
    120
    
    >>> factorial(10)
    3628800
    '''
    
    result = 1
    
    if n == 0:
        
        result = 1
        
    else:
    
        for row in range(n, 0, -1):
        
            result *= row
        
    return result


def draw_base(size: int, levels: int):
    
    '''
    Prints the base of the clock based on size integer entered.
    '''
    base_size = '___________'
    size_diff_leg = '|' * size
    size_diff_top = size * '__'
    
    top_base = '  ' + base_size + size_diff_top + '\n |' + base_size + size_diff_top + '|\n'
    base_levels = ('  |||||' + size_diff_leg + ' |||||' + size_diff_leg + '\n') * 4
    additional_level = '  |||||' + size_diff_leg + ' |||||' + size_diff_leg + '\n'
    
    for times in range(levels):
        print(top_base, end='')
        print(base_levels, end='')
        
        for base in range(size):
            print(additional_level, end='')
            
def draw_face(size: int):
    
    '''
    Prints the face of the clock based on size integer entered.
    '''
    
    edge = '|-------------' + 2*('-' * size) + '|'
    divider = '|~~~~~~~~~~~~~' + 2*('~' * size) + '|'
    left_side = '|' + '~' * size
    right_side = '~' * size + '|'
    clock_edge = '|-----------|'
    
    face_row = '|-----------|'
    face_row1 = '|@  **^**  @|'
    face_row2 = '|  ** | **  |'
    face_row3 = '| *   @-->* |'
    face_row4 = '|  **   **  |'
    face_row5 = '|@  *****  @|'
    
    print(edge)
    
    for top in range(size):
        print(divider)
        
        
    print(left_side + face_row + right_side)    
    print(left_side + face_row1 + right_side)
    print(left_side + face_row2 + right_side)
    print(left_side + face_row3 + right_side)
    print(left_side + face_row4 + right_side)
    print(left_side + face_row5 + right_side)
    print(left_side + face_row + right_side)
    
    for bottom in range(size):
        print(divider)
        
    print(edge)
    

def draw_top(size: int):
    
    '''
    Prints the top of the clock based on size integer entered.
    '''
    space = size - 1
    side = ' ' * size
    top = '   |*******' + '*' * size * 2 + '|\n'
    row1 = '   |  ' + side + '/ \  ' + side + '|\n'
    row2 = '   | ' + side + '// \\\\ ' + side + '|\n'
    row3 = '   |' + side + '/// \\\\\\' + side + '|\n'
    
    print(top + row1 + row2 + row3, end='')
    
    for row in range(4, size+4, 1):
        
        
        left = '   |' + (space * ' ') + '/' * row + ' '
        right = '\\' * row + (space * ' ') + '|'
        
        space -= 1
        
        print(left + right)
        
        
        
def draw_clock_tower(size: int, levels: int) -> str:
    
    '''
    Prints a clock tower with the desired size and number of base levels.
    '''
    
    face = draw_face(size)
    top = draw_top(size)
    base = draw_base(size, levels)
    
    return face and top and base