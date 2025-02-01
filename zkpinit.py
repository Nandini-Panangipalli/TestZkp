import hashlib #importing the hashing lbrary

def hashing(secret):
    return hashlib.sha256(secret.encode()).hexdigest() #taking in the input secret and hashing it using sha256 and hexadecimal

#proving the passkey
def provePass(secret):
    return hashing(secret) #return the hashing of the secret 

#verifying the passkey
def verifyPass(hashedSecret,expectedSecret):
    hashExpectedSecret = hashing(expectedSecret) #here we are hashing the expected secret and storing its value in this variable
    if(hashExpectedSecret==hashedSecret): #the hashed secret and expected secret to be same
        return True
    else:
        return False


#prover
secret = input("Enter your key:") #the prover enters the key to verify
hashedSecret = provePass(secret) 

#verifier
expectedSecret = "hello"
if(verifyPass(hashedSecret,expectedSecret)): # check if they are same if they are same 
    print("Voila! Both are same and you are authenticated")
else:
    print("Trespassing!!Not authenitcated")