#################################################
exNumber = 5
# Code:

import math

# Function counts elements of geometric progression

def GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):

    # a1        - first element
    # factor    - geometric factor 
    # index     - index of element to count 

    value = a1 * pow(factor, index - 1)
    return value

# Function counts value of geometrical progression factor from firs and second element

def GiveFactorForGeomSeq(term, nexterm):
    
    # term      - firs term's value
    # next term - second term's value

    tmpFactor = nexterm / term
    return tmpFactor

# Function sums up n elements of geometrical progression

def GiveSumOfNElementsGeomSeq(a1 = 2, factor = 2, n = 2):
    
    # a1        - first element
    # factor    - geometric factor
    # n         - number of elements to sum

    summary = (a1 * (1 - pow(factor, n)))/(1 - factor)
    return summary

#################################################



