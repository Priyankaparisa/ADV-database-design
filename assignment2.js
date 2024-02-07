//and logic
db.listingsAndReviews.find({$and: [{amenities: "Washer"}, {amenities: "Dryer"}]}); 

//or logic
db.listingsAndReviews.find({$or: [{amenities: "Internet"}, {amenities: "TV"}]});

//nor
db.listingsAndReviews.find({$nor: [{amenities: "Internet"}, {amenities: "TV"}]});

//not
db.listingsAndReviews.find({$not: [{amenities: "Elevator"}]});

//andoror
db.listingsAndReviews.find({
  $and: [
    { $nor: [{ amenities: "Iron" }, { amenities: "Internet" }] },
    { $nor: [{ amenities: "Hangers" }, { amenities: "Heating" }] },
  ],
});

//elementsmatch
db.listingsAndReviews.find({amenities: {$elemMatch: {$eq: "Wifi"}}});

//find
db.grades.find({ _id: ObjectId("65b9b6f769c4895078585dc0") })

//findArray
db.listingsAndReviews.find({amenities: "Wifi"});

//insertOne() 
db.CreateColelction("SHU")
db.SHU.insertOne({
  student_id: 654321,
  products: [
    {
      type: "exam",
      score: 90,
    },
    {
      type: "homework",
      score: 59,
    },
    {
      type: "quiz",
      score: 75,
    },
    {
      type: "homework",
      score: 88,
    },
  ],
  class_id: 550,
})


//insertMany()
db.SHU.insertMany([
  {
    student_id: 546789,
    products: [
      {
        type: "quiz",
        score: 50,
      },
      {
        type: "homework",
        score: 70,
      },
      {
        type: "quiz",
        score: 66,
      },
      {
        type: "exam",
        score: 70,
      },
    ],
    class_id: 551,
  },
  {
    student_id: 777777,
    products: [
      {
        type: "exam",
        score: 83,
      },
      {
        type: "quiz",
        score: 59,
      },
      {
        type: "quiz",
        score: 72,
      },
      {
        type: "quiz",
        score: 67,
      },
    ],
    class_id: 550,
  },
  {
    student_id: 223344,
    products: [
      {
        type: "exam",
        score: 45,
      },
      {
        type: "homework",
        score: 39,
      },
      {
        type: "quiz",
        score: 40,
      },
      {
        type: "homework",
        score: 88,
      },
    ],
    class_id: 551,
  },
])


//lesserthan
db.SHU.find({ "products.score": { $lt: 59  } })

//lesserthanequalto
db.SHU.find({ "products.score": { $lte: 58  } })

//greaterthan
db.SHU.find({ "products.score: { $gt:59  } })
//greaterthanequalto
db.SHU.find({ "products.score": { $lt: 59  } })
//in
db.grades.find({ student_id: { $in: [654321, 546789] } })
db.grades.find({ _id: { $in: [ObjectId('65b9b75969c4895078585dc1'), ObjectId('65b9b7596
//Mongopy
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://chichilitejagni:January44@cluster0.yxfoxt5.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    '''for db_name in client.list_database_names():
        print(db_name)*/''' #once sucessfully established connection
except Exception as e:
//output
PS C:\Users\priya> & C:/Users/tejag/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/priyag/mongopy.py
Pinged your deployment. You successfully connected to MongoDB!
