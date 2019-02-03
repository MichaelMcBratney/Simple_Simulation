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
    if Gender == 'male':
        firstnames = load_names('male_firstnames.txt')
    elif Gender == 'female':
        firstnames = load_names('female_firstnames.txt')
    lastnames = load_names('lastnames.txt')
    # Sizes of the firstnames and lastnames lists:
    fnamesize = len(firstnames) - 1
    lnamesize = len(lastnames) - 1
    first = firstnames[random.randint(0, fnamesize)]
    last = lastnames[random.randint(0, lnamesize)]
    fullname = ''.join((first,' ', last))
    return fullname 
           

