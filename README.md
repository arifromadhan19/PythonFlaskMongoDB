# PythonFlaskMongoDB

product collection structure

{
    "_id" : ObjectId("59fd7f1d41a8ead25dfe067b"),
    "name_product" : "buku",
    "qty" : 10
}


MongoDump
mongodump --host localhost --port 27017 --db db_product --out /home/arif/...(your directory)

MongoRestore
mongorestore --host localhost --port 27017 --db db_product /home/arif/...(your directory)

