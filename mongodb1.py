import pymongo

client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.dyxaeme.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    'name':'sudhanshu',
    'email':'sudhanshu@ineuron.com',
    'surname':'kumar'
}

db1 = client['mongoguest']
coll = db1['test']
coll.insert_one(d)