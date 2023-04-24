#useful prev modules
from U1_L1_FactorsAndMultiples import findFactors
from U1_L2_PrimeAndCompositeNumbers import isPrime

import logging
logging.basicConfig(level=logging.INFO)

#WTF HOW IN THE WORLD DID I GET THIS TO WORK
def primeFactorization(n:int):
    prime_factors = []
    # logging.info("looking to prime factorize %s",n)
    # logging.info('working with current prime factors %s',prime_factors)
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

def commonList(a:list,b:list) -> list:
    common = a
    #need to count the occurances in the list of factors
    for num in b:
        if b.count(num) > common.count(num):
            difference = b.count(num) - common.count(num)
            for repeat in range(difference):
                common.append(num)
    return sorted(common)


def leastCommonDivisibility(a:int,b:int):
    "all numbers divisible by both 'a' and 'b' are also divisible by ..."
    a_primeFactors = primeFactorization(a)
    # print(f"Prime factors of A is {a_primeFactors}")
    b_primeFactors = primeFactorization(b)
    # print(f"Prime factors of B is {b_primeFactors}")
    lcd_factors = commonList(a_primeFactors,b_primeFactors)
    return lcd_factors

def alsoDivisibleBy(factors:list)->list:
    "this will give a list of all possible numbers able to be made with the given list of factors"
    raise Exception("function alsoDivisibleBy() is not yet done")