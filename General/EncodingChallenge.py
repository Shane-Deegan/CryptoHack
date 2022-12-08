from calendar import c
from this import d
from pwn import *
import json
import base64
import codecs
from Crypto.Util.number import *


#remote connection to crytphack
r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

def list_to_string(s):
    output = ""
    return(output.join(s))

#loop for flag levels

for x in range(0,101):

    #get encoded line from cyrpto.org and store it in a variable
    stringFromSourceCode = json_recv()

    #each encode type as a varible for flag finding logic
    a = "hex"
    b = "rot13"
    c = "base64"
    d = "utf-8"
    e = "bigint"
    
    if "flag" in stringFromSourceCode:
        print("Challenge complete, Flag= ", stringFromSourceCode["flag"])

    print("Level=", x)
    print("Encode type= ", stringFromSourceCode["type"])
    print("Encoded value=", stringFromSourceCode["encoded"])

    encodedString = stringFromSourceCode["encoded"]
    recievedType = stringFromSourceCode["type"]

    #logic to decode any potential data value type
    if recievedType == a:
        decode = (bytes.fromhex(encodedString)).decode("utf-8")

    elif recievedType == b:
        decode = codecs.decode(encodedString, 'rot_13')

    elif recievedType == c:
        decode = base64.b64decode(encodedString).decode("utf-8")

    elif recievedType == d:
        decode = list_to_string([chr(a) for a in encodedString])

    elif recievedType == e:
        decode = unhex(encodedString.replace("0x", "")).decode("utf-8")

    print("Decoded message= ", decode)

    #send decoded message back to crypto.org server for validation
    to_send = {
        "decoded": decode
    }
    json_send(to_send)