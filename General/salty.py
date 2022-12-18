from Crypto.Util.number import long_to_bytes

#number exported from txt file
a = 44981230718212183604274785925793145442655465025264554046028251311164494127485

#salty.py provided by cvryptohack used this method
print(long_to_bytes(a))
