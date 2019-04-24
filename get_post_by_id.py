import pymongo


def get_post():
    """ Establish a connection to the db. Get a post by id. """
     # Set the connection to db
    uri = "mongodb://127.0.0.1:27017"
    client = pymongo.MongoClient(uri)

    # Set the collection and db to work on
    db = client['blog']
    collection = db['posts']

    id = "5cb0939271806b6b41599077"
    post = collection.find_one({"_id": id})

    # return only one field from mongo db chosen post
    return post
