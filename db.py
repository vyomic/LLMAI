from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Replace placeholders with your actual values
username = "VyomicLLM"
password = "AtlasLLM@123"
cluster_string = "clusterllm.sxksl9r.mongodb.net/"  # From Atlas connection details
database_name = "users"

# Construct the connection URI
uri = f"mongodb+srv://VyomicLLM:AtlasLLM123@clusterllm.sxksl9r.mongodb.net/?retryWrites=true&w=majority&appName=ClusterLLM"
client = MongoClient(uri, server_api=ServerApi('1'))
# ping connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
# Connect to MongoDB Atlas

# Access the database
db = client["users"]  # Replace with the actual database name

# Now you can use the `db` object to interact with your MongoDB Atlas database
# (e.g., create collections, insert/update/delete data, etc.)

# Example: Insert a document into a collection
collection = db["my_collection"]
document = {"name": "John Doe", "age": 30}
collection.insert_one(document)

# Close the connection after use
client.close()