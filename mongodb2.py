import pymongo
client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.asv9hix.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

a = {
    'name':'Ram',
    'email':'ram@ineuron.com',
    'surname':'Kumar'
    }, {
        'name':'raman',
        'email':'raman@inuron.com',
        'surname':'feku'
    }

new_data = client['new_data1']
collection = new_data['detail1']
collection.insert_many(a)

'''record = collection.find()
for i in record:
    print(i) '''