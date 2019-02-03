import random

def load_names(filename):
    """
    Input: Name of file that contains a single name per line (string)
    Output: List of all the names in file with \n removed from the end (string list)
    """
    namelist = []
    with open(filename, 'r') as f:
        for line in f:
            namelist.append(line.strip('\n'))
    return namelist

def get_name(Gender):
    """
    Input: Gender, one of : 'male' , 'female'
    Output: A random full name  (string)
    Example use:
    get_name('female') will return a female name as string.
    """
    if Gender.lower() == 'male':
        firstnames = load_names('male_firstnames.txt')
    elif Gender.lower() == 'female':
        firstnames = load_names('female_firstnames.txt')
    else:
        return "NO GENDER"
    lastnames = load_names('lastnames.txt')
    # Sizes of the firstnames and lastnames lists:
    first = random.choice(firstnames)
    last = random.choice(lastnames)
    fullname = ''.join((first,' ', last))
    return fullname


