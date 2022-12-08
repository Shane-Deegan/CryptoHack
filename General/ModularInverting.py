#import inverting tool
from Crypto.Util.number import inverse

#inverse number given with modulo given
a = inverse(3, 13)

print("Flag =", a)