from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
import os

def hash_data(data):
    """Hashes the provided data using SHA-256."""
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data)
    return digest.finalize()

def authenticate_user(private_key, public_key):
    """Simulates authentication using Schnorr protocol with elliptic curve operations."""
    # SECP256R1 curve order (constant value for SECP256R1)
    curve_order = ec.SECP256R1().order
    print("Curve Order:", curve_order)

    # Step 1: Server generates a challenge
    challenge = os.urandom(16)
    print("Server Challenge:", challenge.hex())

    # Step 2: User generates ephemeral key pair
    ephemeral_private_key = ec.generate_private_key(ec.SECP256R1())
    ephemeral_public_key = ephemeral_private_key.public_key()

    # Combine challenge and ephemeral public key
    ephemeral_public_bytes = ephemeral_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    print("Ephemeral Public Key Bytes:", ephemeral_public_bytes.decode())
    combined_data = challenge + ephemeral_public_bytes
    hashed_data = hash_data(combined_data)
    print("Hashed Data:", hashed_data.hex())

    # User computes response (proof)
    ephemeral_private_value = ephemeral_private_key.private_numbers().private_value
    user_private_value = private_key.private_numbers().private_value
    hashed_int = int.from_bytes(hashed_data, "big")

    response = (ephemeral_private_value + hashed_int * user_private_value) % curve_order
    print("Response (Proof):", response)

    # Step 3: Server reconstructs the combined point
    # Perform elliptic curve operations using the generator point (from SECP256R1)
    curve = ec.SECP256R1()
    generator = curve.generator  # Use the generator for curve point operations

    # Reconstruct the combined point: R + e * P
    reconstructed_point = generator * hashed_int + ephemeral_public_key.public_numbers().x * generator
    print("Reconstructed Combined Point (X, Y):", reconstructed_point)

    # Verify response: compare reconstructed point with expected point (in response)
    is_valid = (response == reconstructed_point.x)  # Simplified for testing
    print("\nAuthentication Result:", "Success" if is_valid else "Failed")

# Simulate private and public key generation for testing
private_key = ec.generate_private_key(ec.SECP256R1())
public_key = private_key.public_key()

authenticate_user(private_key, public_key)
