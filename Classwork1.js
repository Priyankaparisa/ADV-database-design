
//Query 1
db.classwork.insertOne({
    "_id": 123,
    "Emp_ID": "10025AE336",
    "Personal_details": {
        "First_Name": "Radhika",
        "Last_Name": "Sharma",
        "Date_Of_Birth": "1995-09-26"
    },
    "Contact": {
        "e-mail": "radhika_sharma.123@gmail.com",
        "phone": "9848022338"
    },
    "Address": {
        "city": "Hyderabad",
        "Area": "Madapur",}}


//Query 2
db.Class.insertMany({
    "id": "POST_ID",
    "title": "TITLE_OF_POST",
    "description": "POST_DESCRIPTION",
    "by": "POST_BY",
    "url": "URL_OF_POST",
    "tags": ["TAG1", "TAG2", "TAG3"],
    "likes": "TOTAL_LIKES",
    "comments": [
        {
            "user": "COMMENT_BY",
            "message": "TEXT",
            "dateCreated": "DATE_TIME",
            "like": "LIKES"
        },
        {
            "user": "COMMENT_BY",
            "message": "TEXT",
            "dateCreated": "DATE_TIME",
            "like": "LIKES"
        }
    ]
}
)

//Query 3
db.Class.insertMany([
   {
      "_id": ObjectId("52ffc33cd85242f436000001"),
      "contact": 987654321,
      "dob": "01-01-1991",
      "name": "Tom Benzamin",
      "address": [
         {
            "building": "22 A, Indiana Apt",
            "pincode": 123456,
            "city": "Los Angeles",
            "state": "California"
         },
         {
            "building": "170 A, Acropolis Apt",
            "pincode": 456789,
            "city": "Chicago",
            "state": "Illinois"
         }
      ]
   }
])
