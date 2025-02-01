import mongoose from 'mongoose';

const userSchema = new mongoose.Schema({
  firstName: { type: String, required: true },
  lastName: { type: String, required: true },
  username: { type: String, required: true, unique: true },
  email: { type: String, required: true, unique: true },
  publicKey: { type: String, required: true },
  walletInfo: { type: String, required: true },
  passwordHash: { type: String, required: true },
});

const User = mongoose.model('User', userSchema);

export default User;  // Use export default to export the User model
