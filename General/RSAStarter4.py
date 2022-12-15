a = 857504083339712752489993810777
b = 1029224947942998075080348647219

c = 65537

#facorise the modulus (use -1 as the power)
print(pow(c, -1, (a-1)*(b-1)))
