import pymongo

client = pymongo.MongoClient("mongodb+srv://Sunny:Sunny1997@cluster0.xqvmr.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "sunny",
    "emailid": "srocks023@gmail.com",
    "surname": "gupta"
}
db1 = client["mongotest"]
coll = db1["test"]
coll.insert_one(d)