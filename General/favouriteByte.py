#cipher
cipher = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')

#every possible byte
bytRng = range(255)

#byte / flag
favByte = ''

#search each byte and xor it with our fromhex cipher
for x in bytRng:

    #compare each character in our cipher with every byte
    search = (chr(y^x) for y in cipher)
    
    #concatenate/join each matched byte together
    favByte="".join(search)
    
    #if the byte comparison matches "c" print comparison
    if favByte.startswith("cry"):
        print(favByte)
        