from Crypto.PublicKey import RSA

key = RSA.importKey(open('privacy_enhanced_mail_1f696c053d76a78c2c531bb013a92d4a (1).pem', "rb").read())

print(key.d)