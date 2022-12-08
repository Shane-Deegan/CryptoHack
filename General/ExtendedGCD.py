#function
def egcd(p,q):
    
    #logic to dictate if the answer will just be 1
    if p == 0:
        return q, 0, 1
    
    #if p=! 0 preform euchlids algorithm to find integers
    else:
        #bind values to function
        gcd, u, v = egcd(q % p, p)
        #preform euchlids algorithm until we get a remainder of 1 via long division
        return gcd, v - (q // p) * u, u

p = 26513
q = 32321

#print answers of function and get flag
print("Flag = lower integer ", egcd(p,q))

#ensure correct answer
print(p * 10245 + q * -8404)

