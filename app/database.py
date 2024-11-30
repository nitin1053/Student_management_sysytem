from motor.motor_asyncio import AsyncIOMotorClient
import certifi
MONGO_URI = "mongodb+srv://nitinjha1053:1234523@cluster0.ppk4y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = AsyncIOMotorClient(MONGO_URI, tlsCAFile=certifi.where())
database = client.student_management
student_collection = database.get_collection("students")
