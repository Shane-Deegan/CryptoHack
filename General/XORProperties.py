#imports
from pwn import xor

#keys from website
key1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'
key2 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'
key3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'
key4 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

#xor 1st key with 2nd key to get realKey1
realKey1 = xor(bytes.fromhex(key2),bytes.fromhex(key1))

#xor realKey1 with 2nd key to get realKey2
realKey2 = xor(bytes.fromhex(key3),realKey1)

#xor realKey2 with 2nd key to get realKey3
realKey3 = xor(bytes.fromhex(key2),realKey2)

#xor realKey3 with 4th key to get realKey4 / the flag
realKey4 = xor(bytes.fromhex(key4),realKey3)

#decode realKey4 / FLAG from hex to string
print(realKey4.decode())

#my logic: realKey3^key4 - given my previous xor's

#cryptohacks logic: FLAG ^ key1 ^ key3 ^ key2