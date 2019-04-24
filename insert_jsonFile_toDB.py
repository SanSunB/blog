import pymongo
import json


def insert_json():
    """ Insert a json file to the DB """
    # Set the connection to db
    uri = "mongodb://127.0.0.1:27017"
    client = pymongo.MongoClient(uri)

    # Set the collection and db to work on
    db = client['blog']
    collection = db['posts']

    # Load the jason file
    with open('posts.json') as template:
        template_dct = json.load(template)

    collection.insert(template_dct)


