import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=myclient["school"]
mycollection=mydb['student']

my_many_records=[{"name":"Harish"},{"name":"Yash"},{"name":"Jay"},{"name":"Aditya"}]
x = mycollection.insert_many(my_many_records)