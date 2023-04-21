#useful prev modules
from U1_L1_FactorsAndMultiples import findFactors
from U1_L2_PrimeAndCompositeNumbers import isPrime

import logging
logging.basicConfig(level=logging.INFO)

#WTF HOW IN THE WORLD DID I GET THIS TO WORK
def primeFactorization(n:int):
    prime_factors = []
    logging.info("looking to prime factorize %s",n)
    logging.info('working with current prime factors %s',prime_factors)
    if isPrime(n) == True:
        prime_factors.append(n)
        return prime_factors
    elif isPrime(n) == False:
        factors = findFactors(n)
        prime_factors.append(factors[1])
        n /= factors[1]
        prime_factors += primeFactorization(int(n))
        return prime_factors

def primeFactorization2(n:int):
    prime_factors = []
    pass

#if you want to see 5^2 or something you might just need to use jupiter or something

def leastCommonDivisibility(a:int,b:int):
    "all numbers divisible by both 'a' and 'b' are also divisible by ..."
    a_primeFactors = primeFactorization(a)
    # print(a_primeFactors)
    b_primeFactors = primeFactorization(b)
    # print(b_primeFactors)
    lcd_factors = []
    for element in a_primeFactors:
        if a_primeFactors[element] in b_primeFactors:
            common = b_primeFactors.index(a_primeFactors[element])
            lcd_factors.append(a_primeFactors[element])
            a_primeFactors.pop(element),b_primeFactors.pop(common)
    return lcd_factors
# print(isPrime(661))
# print(leastCommonDivisibility(12,20))
print(primeFactorization(1000454))