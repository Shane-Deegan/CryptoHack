from pwn import xor

message = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

#known bytes for future comaprison
knownFlagPiece = "crypto{"

#we know 7 bytes so xor them with the first 7 bytes of cipher
#xor the first 7 bytes with the rest of the cipher and last piece of known flag piece
key = xor(message[:7], knownFlagPiece) + xor(message[-1] , "}")

#xor the key with our cipher
fullFlag = xor(key, message)

print(fullFlag)