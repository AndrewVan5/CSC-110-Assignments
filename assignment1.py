import math
def monkey():
    print('  /~\\')
    print(' C oo')
    print(' _( ^)')
    print('/   ~\\')
    
'''
Prints a picture of a monkey.

>>>monkey()
  /~\
 C oo
  ( ^)
/   ~\

(from: https://www.asciiart.eu/animals/monkeys)
'''
    
def cow():
    print('((...))')
    print('( O O )')
    print(' \\   /')
    print(' (`_`)')
    
'''
Prints a picture of a cow.

>>>cow()
((...))
( O O )
 \   /
 (`_`)
 
 from "cp97" at https://www.asciiart.eu/animals/cows 
 '''
def print_logo():
   
    spacer = '/~~~~~~~~\\'
    
    print(spacer)
    monkey()
    print(spacer)
    cow()
    print(spacer)
    monkey()
    print(spacer)
    cow()
    print(spacer)
    
'''
Prints monkey and cow functions back to back twice with a spacer inbetween.

>>>print_logo()
...

'''

def calculate_surface_area(height: float, diameter: float):
    
    '''
    Takes two values of height and diameter.
    Prints total surface area of a cylinder with those values to one decimal point.
    
    >>>calculate_surface_area(height, diameter)
    cylinder area: x
    
    >>>calculate_surface_area(18.9, 27.3)
    cylinder area: 2791.7
    
    >>>calculate_surface_area(1.9, 2.1)
    cylinder area: 19.5
    '''
    
    circumference = math.pi * diameter
    area_top = (math.pi / 4) * diameter ** 2
    area_side = circumference * height
    print(f'cylinder area: {(area_top * 2) + area_side:.1f}')
    
