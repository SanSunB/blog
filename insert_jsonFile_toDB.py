import pymongo
import json
from insert_to_website_from_DB import *

def get_title():
    # Set the connection to db
    uri = "mongodb://127.0.0.1:27017"
    client = pymongo.MongoClient(uri)

    # Set the collection and db to work on
    db = client['blog']
    collection = db['posts']

    # Load the jason file
    with open('posts.json') as template:
        template_dct = json.load(template)

    #collection.insert(template_dct)

    id = "5cb0939271806b6b41599077"
    post = get_post(collection,id)

    # return only one field from mongo db chosen post
    return post['title']
