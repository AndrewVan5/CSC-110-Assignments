import doctest

def multiply_by(lov: list[str], mult: int) -> list:
    
    '''
    Multiplies all items in the entered list by the entered mult ineger.
    >>> multiply_by([4, -2, 'hi'], 5)
    [20, -10, 'hihihihihi']
    
    >>> multiply_by(['hello'], 2)
    ['hellohello']
    
    >>> multiply_by([4], 2)
    [8]
    '''
    new_list = []
    
    for cur_num in lov:
        
        new_list.append(cur_num * mult)
        
    return new_list


def get_below(loi: list[int], thresh: int) -> list:
    
    '''
    Takes a list of integers and threshold value. Returns a new list with all
    values from the list that are below the threshold value.
    
    >>> get_below([2,4,6,8], 7)
    [2, 4, 6]
    
    >>> get_below([2,41,6,8], 8)
    [2, 6]
    
    >>> get_below([2,-41,-6,-3], -3)
    [-41, -6]
    
    
    '''

    new_list = []
    
    for cur_num in loi:
        if cur_num < thresh:
            new_list.append(cur_num)
            
        
    return new_list
        

def remove_negatives(loi: list[int]) -> list:
    
    '''
    Takes a list of integers and returns a new list that contains the values of
    the entered list which are positive.
    
    >>> remove_negatives([2,-4,6,-8])
    [2, 6]
    
    >>> remove_negatives([2,-14,56,-8, 0, 1, -1])
    [2, 56, 0, 1]
    '''
    new_list = []
    
    for cur_num in loi:
        
        if cur_num >= 0:
            
            new_list.append(cur_num)
            
    return new_list
        

def contains_above(lon: list[float], thresh: float) -> float:
    
    '''
    Takes a list of numbers and threshold. Determines whether or not there is a
    value in the list that is greater than the threshold.
    
    >>> contains_above([2,4,6,8], 8)
    False
    
    >>> contains_above([2,4,6,8], 7.99)
    True
    
    >>> contains_above([3.4,-63.43, 54.33], 54.32)
    True
    '''
    index = 0
    for value in lon:
        
        if value>thresh:
            index+=1
            
    return index > 0
        
    
    
    #index = 0
    
    #while index < len(lon) and lon[index] <= thresh:
        
        #index += 1
        
    #return index < len(lon)


def get_smallest(lon: list[float]) -> float:
    
    '''
    Takes a list of numbers and returns the smallest value in the list.
    
    >>> get_smallest([3.63,24,-3.99])
    -3.99
    
    >>> get_smallest([3.63,24,3.99])
    3.63
    
    >>> get_smallest([5])
    5
    '''
    
    smallest = lon[0]
    
    if len(lon) == 1:
        return lon[0]
    
    else:
    
        for cur_num in lon[1:]:
            
            if smallest > cur_num:
                
                smallest = cur_num
                
            
    return smallest
            
        
            
            
            

def count_ends_with(los: list[str], add_str: str) -> int:
    
    '''
    Takes a list of strings and additional string as arguments. Determines how
    many of the strings in the list's endings are the same as the additional
    string (not case sensitive).
    
    >>> count_ends_with(['hello', 'hi', 'jello', 'zebra'], 'ELLO')
    2
    
    >>> count_ends_with(['hello', 'hi', 'hotel', 'HOTEL'], 'el')
    2
    
    >>> count_ends_with(['money', 'soccer', 'jello', 'hay'], 'eY')
    1
    '''
    
    count = 0
    
    if add_str == '':
        return len(los)
    else:
    
        for cur_str in los:
        
            if cur_str[-(len(add_str)):].lower() == add_str.lower():
            
                count += 1
            
    return count
            
            
