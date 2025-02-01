import mongoose from 'mongoose';

const uri = "mongodb+srv://Nandini:Nandini9*@zkpauth.iulwy.mongodb.net/?retryWrites=true&w=majority&appName=ZKPAUTH";

const clientOptions = { 
  serverApi: { version: '1', strict: true, deprecationErrors: true }
};

// Connect to MongoDB Atlas
mongoose.connect(uri, clientOptions)
  .then(() => console.log("✅ Successfully connected to MongoDB Atlas"))
  .catch(err => console.error("❌ MongoDB Connection Error:", err));

// Use export default instead of module.exports
export default mongoose;
