import express from 'express';
import bcrypt from 'bcryptjs';
import crypto from 'crypto';
import User from '../models/user.js';  // Ensure using .js extension
import jwt from 'jsonwebtoken';

const router = express.Router();

// Generate key pair
function generateKeyPair() {
  const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
    modulusLength: 2048,
    publicKeyEncoding: {
      type: 'pkcs1',
      format: 'pem',
    },
    privateKeyEncoding: {
      type: 'pkcs1',
      format: 'pem',
    },
  });
  return { publicKey, privateKey }; // Store private key securely on client side
}

// Registration Route
router.post('/register', async (req, res) => {
  try {
    const { firstName, lastName, username, email, walletInfo, password } = req.body;

    // Validate required fields
    if (!firstName || !lastName || !username || !email || !walletInfo || !password) {
      return res.status(400).json({ message: 'All fields are required' });
    }

    // Check if username or email already exists
    const existingUser = await User.findOne({ $or: [{ username }, { email }] });
    if (existingUser) {
      return res.status(400).json({ message: 'Username or email already taken' });
    }

    // Generate key pair
    const { publicKey, privateKey } = generateKeyPair();

    // Hash password before storing
    const passwordHash = await bcrypt.hash(password, 10);

    // Create new user and store public key
    const newUser = new User({
      firstName,
      lastName,
      username,
      email,
      publicKey,
      walletInfo, // Store encrypted wallet info in the database
      passwordHash,
    });

    await newUser.save();

    res.status(201).json({ message: 'User registered successfully', publicKey });
  } catch (err) {
    console.error('Error registering user:', err);  // Log the actual error
    res.status(500).json({ message: 'Error registering user', error: err.message });
  }
});

// Generate JWT Token
function generateToken(userId) {
  const payload = { userId };
  return jwt.sign(payload, process.env.JWT_SECRET, { expiresIn: '1h' });
}

// Login Route
router.post('/login', async (req, res) => {
  const { username, password, challenge } = req.body;

  try {
    const user = await User.findOne({ username });

    if (!user) {
      return res.status(400).json({ message: 'User not found' });
    }

    // Verify password
    const isPasswordValid = await bcrypt.compare(password, user.passwordHash);

    if (!isPasswordValid) {
      return res.status(400).json({ message: 'Invalid password' });
    }

    // Challenge verification (the user should sign the challenge using their private key)
    const verified = verifyChallenge(user.publicKey, challenge);
    if (!verified) {
      return res.status(400).json({ message: 'Challenge verification failed' });
    }

    // Generate JWT Token
    const token = generateToken(user._id);

    res.status(200).json({ message: 'Login successful', token });
  } catch (err) {
    console.error('Error logging in:', err);  // Log the actual error
    res.status(500).json({ message: 'Error logging in', error: err.message });
  }
});

// Function to verify challenge
function verifyChallenge(publicKey, challenge) {
  // Use public key to verify the challenge (e.g., using the 'crypto' library)
  // For this example, assume challenge is a signed message, and we'll just simulate success here.
  // In a real case, you'll verify the challenge signed by the private key corresponding to the public key.
  return true; // Simulating challenge verification
}

export default router;
