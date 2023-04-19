#useful prev modules
from U1_L1_FactorsAndMultiples import findFactors

#Prime Number

"Prime Numbers = A Natural Number divisible by exactly 2 Natural Numbers, Itself and 1."
"Composite Numbers = A Natural Number that is divisible by more than 2 Natural Numbers."

def isPrime(n:int):
    factors = findFactors(n)
    if len(factors) == 2:
        return True
    else: return False

def isComposite(n:int):
    factors = findFactors(n)
    if len(factors) > 2:
        return True
    else: return False

def identifyPrimeCompositeNeither(n:int):
    if isPrime(n) == True:
        return "Prime"
    elif isComposite(n) == True:
        return "Composite"
    else: return "Neither"
