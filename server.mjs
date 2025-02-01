import dotenv from 'dotenv';
import mongoose from 'mongoose';

dotenv.config(); // Load environment variables

mongoose.set('strictQuery', false);

console.log("Loaded MongoDB URI:", process.env.MONGODB_URI); // Debugging line

const mongoURI = process.env.MONGODB_URI;

if (!mongoURI) {
  console.error("MongoDB URI is not set. Check your .env file.");
  process.exit(1);
}

// Add this line to remove the deprecation warning


mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("Connected to MongoDB"))
  .catch(err => console.error("MongoDB connection error:", err));
