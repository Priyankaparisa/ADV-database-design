//use sample_training
db.zips.aggregate({})

//Sort.js
db.zips.aggregate([
  {
    $sort: {
      pop: -1
     }
}
//outinprojection
db.zips.aggregate([
    {
      $group: {
        _id: "$state",
        total_pop: { $sum: "$pop" }
      }
    },
    {
      $match: {
        total_pop: { $lt: 1000000 }
      }
    }
])
  [
    { _id: 'WY', total_pop: 453588},
    { _id: 'DC', total_pop: 606900},
    { _id: 'DE', total_pop: 666168},
    { _id: 'VT', total_pop: 562758},
    { _id: 'SD', total_pop: 696004},
    { _id: 'MT', total_pop: 799065},
    { _id: 'AK', total_pop: 550043},
    { _id: 'ND', total_pop: 638800}
  ]
db.zips.aggregate([
  {
		$group:{
					_id: "$state",
					total_pop: { $sum:"$pop"}
        }
  },
  {
		$match: {
				totla_pop:{$lt:1000000}
			}
		},
  {
			$out: "small_states"
}
]
)
//project.js
db.zips.aggregate([
{
	$project: {
	state:1,
	zip:1,
	population:"$pop",
	_id:0
  }
}
])
//set.js
db.zips.aggregate([
{
	$project: {
	state:1,
	zip:1,
	population:"$pop",
	pop_2022: { $round: { $multiply: [1.0031, "$pop"]}},
	_id:0
}
}
])
//count.js

db.zips.aggregate([
{ $count: "total_zips"}

])


##$match
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # inserting one product
    new = [
    {
        "$group": {
            "_id": "$city",
            "total_pop":{"$sum":"$pop"}
        }
    }
]

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    #result = accounts_collection.insert_one(new)
    result = list(accounts_collection.aggregate(new))

    #document_id = result.inserted_id
    #pprint(f"_id of inserted document: {document_id}")
    if result:
        print(result)
    else:
        print("No documents in the collection")
except Exception as e:
    print(e)
finally:
  client.close()

#$group
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net//"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # inserting one product
    new = [
    {
        "$group": {
            "_id": "$state",
            "total_pop":{"$sum":"$pop"}
        }
    }
]

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    #result = accounts_collection.insert_one(new)
    result = list(accounts_collection.aggregate(new))

    #document_id = result.inserted_id
    #pprint(f"_id of inserted document: {document_id}")
    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
  client.close()

  ##sort.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import poplib
import datetime
from pprint import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # inserting one product
    new = [
    {
        "$sort": {
            "pop": -1
        }
    }
]

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    #result = accounts_collection.insert_one(new)
    result = list(accounts_collection.aggregate(new))

    #document_id = result.inserted_id
    #pprint(f"_id of inserted document: {document_id}")
    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
  client.close()

##limit.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # inserting one product
    new = [
    {
        "$sort": {
            "pop": -1,
        }
    },
    {"$limit": 3}
]

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    #result = accounts_collection.insert_one(new)
    result = list(accounts_collection.aggregate(new))

    #document_id = result.inserted_id
    #pprint(f"_id of inserted document: {document_id}")
    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
  client.close()

##Count.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import poplib
import datetime
from pprint import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # inserting one product
    new = [
    { "$count": "total_zips" }
]

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    #result = accounts_collection.insert_one(new)
    result = list(accounts_collection.aggregate(new))

    #document_id = result.inserted_id
    #pprint(f"_id of inserted document: {document_id}")
    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
  client.close()

##sset.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # inserting one product
    new = [
    {
        "$sort": {
            "pop": -1,
        }
    },
    {"$limit": 3}
]

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    #result = accounts_collection.insert_one(new)
    result = list(accounts_collection.aggregate(new))

    #document_id = result.inserted_id
    #pprint(f"_id of inserted document: {document_id}")
    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
  client.close()

  from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import poplib
import datetime
from pprint import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # inserting one product
    new = [
    {
	"$project": {
	"state":1,
	"zip":1,
	"population":"$pop",
	"_id":0
  }
}
]

    # Write an expression that inserts the 'new_product' document into the 'products' collection.
    #result = accounts_collection.insert_one(new)
    result = list(accounts_collection.aggregate(new))

    #document_id = result.inserted_id
    #pprint(f"_id of inserted document: {document_id}")
    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
  client.close()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
from pprint import pprint

uri = "mongodb+srv://swathireddy:swathireddy@cluster0.55uldwr.mongodb.net/"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    # Define the aggregation pipeline
    pipeline = [
        {
            "$group": {
                "_id": "$state",
                "total_pop": {"$sum": "$pop"}
            }
        },
        {
            "$match": {
                "total_pop": {"$lt": 1000000}  # Corrected typo in "$lt"
            }
        },
        {
            "$out": "small_states"
        }
    ]

    # Execute the aggregation pipeline
    result = list(accounts_collection.aggregate(pipeline))

    # Print the result of the aggregation pipeline or a message if no documents match the criteria
    if result:
        pprint(result)
    else:
        print("No documents in the collection")

    # Retrieve the list of collections after the aggregation pipeline has executed
    collection_names = db.list_collection_names()

    # Print the list of collections
    print("Collections:")
    for collection_name in collection_names:
        print(collection_name)

except Exception as e:
    print(e)

finally:
    # Close the MongoDB client connection
  client.close()
