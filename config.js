const { MongoClient, ServerApiVersion } = require('mongodb');
const uri = "mongodb+srv://VyomicLLM:AtlasLLM123@clusterllm.sxksl9r.mongodb.net/?retryWrites=true&w=majority&appName=ClusterLLM";

// Create a MongoClient with a MongoClientOptions object to set the Stable API version
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  }
});

async function run() {
  try {
    // Connect the client to the server	(optional starting in v4.7)
    await client.connect();
    // Send a ping to confirm a successful connection
    await client.db("admin").command({ ping: 1 });
    console.log("Pinged your deployment. You successfully connected to MongoDB!");
  } finally {
    // Ensures that the client will close when you finish/error
    await client.close();
  }
}
const userSchema = new mongoose.Schema({
    email: {
      type: String,
      required: true,
      unique: true // Ensures unique email addresses
    },
    password: {
      type: String,
      required: true
    }
  });
  


  // Hash password before saving the user
userSchema.pre('save', async function (next) {
    if (this.isNew || this.isModified('password')) {
      const saltRounds = 10; // Adjust salt rounds as needed
      const hash = await bcrypt.hash(this.password, saltRounds);
      this.password = hash;
    }
    next();
  });
  
  const User = mongoose.model('User', userSchema);
  
  module.exports = User;

// run().catch(console.dir);

