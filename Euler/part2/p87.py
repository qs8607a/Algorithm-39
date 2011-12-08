##The smallest number expressible as the sum of a prime square, prime cube, and
##prime fourth power is 28. In fact, there are exactly four numbers below fifty
##that can be expressed in such a way:
##
##28 = 2^2 + 2^3 + 2^4
##33 = 3^2 + 2^3 + 2^4
##49 = 5^2 + 2^3 + 2^4
##47 = 2^2 + 3^3 + 2^4
##How many numbers below fifty million can be expressed as the sum of a prime
##square, prime cube, and prime fourth power?
import math
from Crazy import primes
def p84(n):
    result=set()
    ps=primes(int(n**0.5)+1)
    for c in ps:
        x=c**4
        if x>=n:
            break
        for b in ps:
            y=x+b**3
            if y>=n:
                break
            for a in ps:
                z=y+a**2
                if z>=n:
                    break
                result.add(z)
    return len(result)
print(p84(50000000))
