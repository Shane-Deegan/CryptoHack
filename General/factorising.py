#install factordb-pycli and import library
from factordb.factordb import FactorDB

#user factor db to insert an int to factorise
a = FactorDB(510143758735509025530880200653196460532653147)

#connect to the data base
a.connect()

#print the minimum factor on the factor list compiled by FactorDB
print(min(a.get_factor_list()))