import pymongo
from pymongo.client_options import _parse_credentials

client = pymongo.MongoClient("mongodb+srv://matu:avMyb1Wb0DGyAXfD@healty1.aj330.mongodb.net/Todo?retryWrites=true&w=majority")
mydb = client["Todo"]
mycollection = mydb["todo"]

