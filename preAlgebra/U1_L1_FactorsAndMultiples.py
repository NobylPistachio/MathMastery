#this is to master mathematics
import logging
logging.basicConfig(level=logging.DEBUG)

#Factor Pairs
"Factor = a number that fits into another number, ex. 5 is a factor of 15"
"Factor Pair = 2 numbers that multiply together"
"Multiple ex 15 is a multiple of 3"
def isFactor(a:int,b:int):
    "Is 'a' a factor of 'b'?"
    if b % a == 0:
        return True
    else: return False

def findFactors(n:int):
    factors = []
    for num in range(n):
        # logging.info("checking if %s is a factor of %s",num, n)
        num += 1
        if n % num == 0:
            factors.append(num)
    return factors

def multiply(n:list)->int:
    product = 1
    for num in n:
        product *= num
    return product

def findFactors2(given_n:int)->list:
    factors = []
    # for number in range(n):
    #     number += 1
    #     logging.info("checking if %s is a factor of %s",number, n)
    #     if n % number == 0:
    #         factors.append(number)
    #         n //= number
    #         break
    #     else: number+=1
    for number in range(given_n):
        number += 1
        if given_n % number == 0:
            print(f'im a factor! {number}')
            factors.append(number)
            continue
        print(number)
    return factors

def giveMultiples(n:int):
    "I'm only going to give you first 12 multiples of n as a list"
    multiples = []
    for num in range(12):
        num += 1
        multiples.append(num*n)
    return multiples

def isMultiple(a:int,b:int):
    "Is 'a' a multiple of 'b'?"
    if a % b == 0:
        return True
    else: return False
    