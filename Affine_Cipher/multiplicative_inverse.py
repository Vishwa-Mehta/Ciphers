# assuming gcd(A,n) = 1
# here n is the total number of letters in the list ALPHABET -> 26


def eucledian_algo(A: int, n: int) -> [[int]]:
    dividend = []
    divisor = []
    quotient = []
    remainder = []
    r = n % A
    while r != 0:
       dividend.append(n)
       divisor.append(A)
       quotient.append(n//A)
       remainder.append(r)
       n = A
       A = r
       r = n % A
    return [remainder, dividend, divisor, quotient]

print(eucledian_algo(20,97))
y = pow(20, -1, 97)
print(y)
