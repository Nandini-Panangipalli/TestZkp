import hashlib #importing the hashing lbrary
import random #import the random library for randomly allocating the number

def challenge():
    return random.randrange(0,100) #randomly allocate a number betwwen 0 to 100 random->keyword randrange->the range we want the number to be

def hashing(secret):
    return hashlib.sha256(secret.encode()).hexdigest() #taking in the input secret and hashing it using sha256 and hexadecimal

#proving the passkey
def provePass(secret):
    return hashing(secret) #return the hashing of the secret 

#verifying the passkey
def verifyPass(hashedSecret,expectedSecret):
    flag=0 #initial a variable to 0
    for i in range(0,100):
        hashExpectedSecret = hashing(expectedSecret + str(i)) #here we are hashing the expected secret and storing its value in this variable and also we are
                                                            #concating the i value [a random number] as a string to the expected secret can say as the digital signature kind of
        if(hashExpectedSecret==hashedSecret): #the hashed secret and expected secret to be same
            flag=1 #flag is incremented to 1
            break #break as else is not req as flag is already initialised to 0

    if(flag==1): #means same passkey
        return True 
    else: #diff passkey
        return False
       

#prover
secret = input("Enter your key:") #the prover enters the key to verify
challengeValue = challenge() #giving the function ref of challenge and storing it in this variable
hashedSecret = provePass(secret + str(challengeValue)) #here we are concatinating this random number ka function as a string and givig it as the arugument to the proving 
                                                       #password function

#verifier
expectedSecret = "123"
if(verifyPass(hashedSecret,expectedSecret)): # check if they are same if they are same 
    print("Voila! Both are same and you are authenticated")
else:
    print("Trespassing!!Not authenitcated")