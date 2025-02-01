import hashlib
import random

# Hashing function
def hashing(secret):
    return hashlib.sha256(secret.encode()).hexdigest()

# Prove passkey by hashing the secret
def provePass(secret):
    return hashing(secret)

# Verify passkey by comparing the hashed secret with the expected secret
def verifyPass(hashedSecret, expectedSecret):
    hashExpectedSecret = hashing(expectedSecret)
    return hashExpectedSecret == hashedSecret

# Generate a challenge (random number)
def generateChallenge():
    return random.randint(1, 100)  # Random number as a challenge

# Generate a response based on the challenge and secret
def generateResponse(challenge, secret):
    combined = str(challenge) + secret
    return hashing(combined)

# Verify the response
def verifyResponse(challenge, response, expectedSecret):
    expectedResponse = generateResponse(challenge, expectedSecret)
    return response == expectedResponse

# Main interactive ZKP-like system
expectedSecret = "hello"  # Verifier's known secret
numRounds = 3  # Number of challenge-response rounds
proverSecret = input("Enter your key (prover): ")

if not verifyPass(provePass(proverSecret), expectedSecret):
    print("Initial authentication failed. You don't know the secret!")
else:
    print("Initial authentication passed. Entering ZKP interaction.")
    for i in range(numRounds):
        challenge = generateChallenge()
        print(f"Round {i + 1}: Challenge sent to prover: {challenge}")
        
        response = generateResponse(challenge, proverSecret)  # Prover generates response
        print(f"Prover's response: {response}")
        
        if verifyResponse(challenge, response, expectedSecret):
            print(f"Round {i + 1}: Verification successful!")
        else:
            print(f"Round {i + 1}: Verification failed! Prover doesn't know the secret.")
            break
    else:
        print("All rounds passed. Prover authenticated successfully!")
