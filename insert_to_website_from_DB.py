def get_post(collection, id):
    # get a jason structure by id
    post = collection.find_one({"_id": id})
    return post
