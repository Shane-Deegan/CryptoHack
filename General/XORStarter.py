#string provided on crytpohack
str = "label"

#loop each character, turn to unicode xor by 13, convert back into strings
print("crypto{")

for x in str:
    print(chr(ord(x)^13))

    
    