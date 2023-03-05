# Tags: prime divisors, prime factors
from collections import defaultdict
def prime_divisors(n):
    """
    Returns a list of prime divisors of n.
    """
    i = 2
    divisors = defaultdict(int)
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            divisors[i] += 1
    if n > 1:
        divisors[n] += 1
    return divisors

# ==============================================
from collections import Counter
n = 8
res = Counter(prime_divisors(n))
print(f"res --> {res}")
n = 20
res2 = Counter(prime_divisors(n))
print(f"res --> {res2}")
print(f"============================================")
final_output = res - res2
final_output = res + res2
print(f"total dict--> {final_output}")

# ======================================================
# Approach 2

import math
mx = 10**2
spf = [i for i in range(mx+1)]
for i in range(2,int(math.sqrt(mx))+1):
    if spf[i]==i:
        for j in range(i*i,mx+1,i):
            spf[j]=min(spf[j],i)
            
def getPrimeFactors(x):
    while x!=1:
        yield spf[x]
        x//=spf[x]

res = getPrimeFactors(90)
for j in res:
    print(j)