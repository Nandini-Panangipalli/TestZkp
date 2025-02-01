// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ZKPAuth {
    struct User {
        address userAddress;
        bytes32 publicKey; // User's public key hash
        bool isRegistered; // Tracks registration status
    }

    mapping(address => User) public users;

    event UserRegistered(address indexed user, bytes32 publicKey);
    event UserUpdated(address indexed user, bytes32 newPublicKey);
    event ProofVerified(address indexed user, bool success);

    // User registration function
    function register(bytes32 publicKey) public {
        require(!users[msg.sender].isRegistered, "User already registered");

        // Register the user
        users[msg.sender] = User({
            userAddress: msg.sender,
            publicKey: publicKey,
            isRegistered: true
        });

        emit UserRegistered(msg.sender, publicKey);
    }

    // Update public key function
    function updatePublicKey(bytes32 newPublicKey) public {
        require(users[msg.sender].isRegistered, "User not registered");

        users[msg.sender].publicKey = newPublicKey;

        emit UserUpdated(msg.sender, newPublicKey);
    }

    // Function to verify ZKP proof (dummy for now)
    function verifyProof(bytes32 proof, bytes32 expectedProof) public {
        require(users[msg.sender].isRegistered, "User not registered");

        // Simulated proof verification
        bool isValid = (proof == expectedProof);

        emit ProofVerified(msg.sender, isValid);
    }

    // Get user information
    function getUser(address user) public view returns (User memory) {
        require(users[user].isRegistered, "User not registered");
        return users[user];
    }
}
