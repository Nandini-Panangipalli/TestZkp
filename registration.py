from cryptography.hazmat.primitives.asymmetric import ec #imports ec module that provides functions to work with 
# elliptic curve cryptography (ECC), which we use to generate public-private key pairs for both the user and the server.
from cryptography.hazmat.primitives import serialization #helps to convert the keys to save them as files[.pem] after generation
import os #imports os module that helps in interacting with the os such as the file operations

def generate_keys():
    ###Generates elliptic curve public-private key pairs.
    # Generate private key using SECP256R1 curve
    private_key = ec.generate_private_key(ec.SECP256R1())
    # Get the corresponding public key
    public_key = private_key.public_key()

    # Serialize both private and public keys to PEM format
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem

def save_keys(user_private_key, user_public_key, server_private_key, server_public_key):
    """Save keys to files."""
    with open("user_private_key.pem", "wb") as f:
        f.write(user_private_key)
    with open("user_public_key.pem", "wb") as f:
        f.write(user_public_key)
    
    with open("server_private_key.pem", "wb") as f:
        f.write(server_private_key)
    with open("server_public_key.pem", "wb") as f:
        f.write(server_public_key)

def registration_process():
    """Handles the registration phase for both user and server."""
    print("Starting Registration Phase...\n")

    # Generate keys for the user and server
    user_private_key, user_public_key = generate_keys()
    server_private_key, server_public_key = generate_keys()

    # Print keys for verification (just for debugging)
    print("User Public Key (PEM):\n", user_public_key.decode())
    print("Server Public Key (PEM):\n", server_public_key.decode())

    # Save keys to files for future use
    save_keys(user_private_key, user_public_key, server_private_key, server_public_key)

    print("\nKeys have been saved successfully!\n")

# Run the registration process
registration_process()
