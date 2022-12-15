from factordb.factordb import FactorDB
from Crypto.Util.number import *

#factorise the number given in text file
db = FactorDB(742449129124467073921545687640895127535705902454369756401331)
db.connect()
db.get_factor_list()

#multiply the 1st and 2nd value on the list to get eulrot toitent
a = (db.get_factor_list()[0] - 1) * (db.get_factor_list()[1] - 1)

#get power of value given modulo eulort toitent result
b = pow(3, -1, a)

#use 2 integers given in output.txt and use the output of "b" as the power
c = pow(39207274348578481322317340648475596807303160111338236677373, b, 742449129124467073921545687640895127535705902454369756401331)

#convert c into bytes for readable fag
print(long_to_bytes(c))