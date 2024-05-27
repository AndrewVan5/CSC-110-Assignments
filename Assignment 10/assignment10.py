import doctest
from pet import Pet
from date import Date

# represents a pet as (name, species)
PetNameSpecies = tuple[str,str]

# columns of values within input file row and within PetNameSpecies tuple
NAME    = 0
SPECIES = 1
MONTH   = 2
DAY     = 3
YEAR    = 4

def read_file(filename: str) -> list[Pet]:
    ''' returns a list of Pets populated with data from filename
    
    Preconditions: filename exists.
    If filename is not empty, each row has a single Pet's information
    separated by commas with expected values at columns:
    NAME, SPECIES, MONTH, DAY and YEAR.

    >>> read_file('empty.csv')
    []
    >>> read_file('pet_data.csv')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    '''
    new_list = []
    
    file_handle = open(filename, 'r')
    read_line = file_handle.readline()
    
    
    if read_line == '':
        return []
    
    else:
    
        while read_line != '':
            
            line = read_line.split(',')
            
            date = Date(int(line[2]), int(line[3]), int(line[4].rstrip('\n')))
            
            self = Pet(line[0], line[1], date)
            
            new_list.append(self)
            
            read_line = file_handle.readline()
            
    return new_list    

def find_pet(lopets: list[Pet], name: str) -> int:
    ''' returns the position of pet with given name in lopets
    Returns -1 if name not found
    Returns the position of the first found if there >1 Pet with the given name
    
    Precondition: name must match case exactly
    ie. 'rover' does not match 'Rover'

    >>> find_pet([], 'Fred')
    -1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    1
    >>> find_pet([Pet('Rover', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Bowser')
    -1
    >>> find_pet([Pet('Red', 'Dog', Date(12, 22, 2020)), \
Pet('Red', 'Cat', Date(1, 2, 2019))], 'Red')
    0
    '''
    index = 0
    test = -1
    count = 0
    
    for pet in lopets:
        
        if pet.get_name() == name:
            count += 1
    if count == 0:
        return -1
    
    else:
        while test == -1:
            
            if lopets[index].get_name() == name:
                test = index
            
            index += 1
            
        return test

def get_all_of_species(lopets: list[Pet], species: str) -> list[Pet]:
    ''' returns a list of all pets of the given species.
    Result list is not necessarily unique, if >1 Pet in lopets has the same name.
    
    Precondition: species must match case exactly
    ie. 'dog' does not match 'Dog'
    
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_all_of_species([], 'Dog')
    []
    >>> get_all_of_species(pets, 'Dog')
    [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_all_of_species(pets, 'Tiger')
    []
    >>> get_all_of_species(pets, 'Hamster')
    [Pet('Chewie', 'Hamster', Date(1, 23, 2009))]
    '''
    new_list = []
    
    for pet in lopets:
        
        if pet.get_species() == species:
            new_list.append(pet)
            
    return new_list


def get_latest_birthdate(lopets: list[Pet]) -> Date:
    ''' returns the latest Date of all birthdates of Pet instances in lopets
    Precondition: lopets is not empty
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]

    >>> get_latest_birthdate([Pet('Rover', 'Dog', Date(12, 31, 2010))])
    Date(12, 31, 2010)
    >>> get_latest_birthdate(pets)
    Date(9, 15, 2016)
    '''
    latest = 0
    index = 0
    
    for pet in lopets:
        latest_birthdate = lopets[latest].get_birthdate()
        current_birthdate = pet.get_birthdate()
        if Date.is_after(current_birthdate, latest_birthdate) == True:
            latest = index
              
        index += 1
        
    birthdate = lopets[latest].get_birthdate()
    
    return birthdate
        
        


def get_youngest_pets(lopets: list[Pet]) -> list[PetNameSpecies]:
    ''' returns a list of PetNameSpecies of all the youngest pets in lopets
    >>> pets = [Pet('Rover', 'Dog', Date(12, 31, 2010)), \
Pet('Red', 'Cat', Date(9, 15, 2016)), \
Pet('Chewie', 'Hamster', Date(1, 23, 2009)), \
Pet('Sam', 'Budgie', Date(3, 29, 1990)), \
Pet('Ollie', 'Dog', Date(2, 8, 2009)), \
Pet('Scout', 'Dog', Date(9, 15, 2016))]
    >>> get_youngest_pets([])
    []
    >>> get_youngest_pets(pets)
    [('Red', 'Cat'), ('Scout', 'Dog')]
    '''
    latest = 0
    index = 0
    new_list = []
    
    if lopets == []:
        return []
    
    else:
    
        for pet in lopets:
            latest_birthdate = lopets[latest].get_birthdate()
            current_birthdate = pet.get_birthdate()
            if Date.is_after(current_birthdate, latest_birthdate) == True:
                latest = index
                  
            index += 1
            
        birthdate = lopets[latest].get_birthdate()
        
        for pet in lopets:
            pet_birthdate = pet.get_birthdate()
            if pet_birthdate == birthdate:
                tuple = (pet.get_name(), pet.get_species())
                new_list.append(tuple)
                
        return new_list
            