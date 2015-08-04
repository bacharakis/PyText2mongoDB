from pymongo import MongoClient
import os

# the location where the text files are stored
location="/Users/christos/Projects/pyScripts/"
try:
    for file in os.listdir(location):
        if file.endswith(".txt"):
            client = MongoClient()
            # use a database called "test_database"
            db = client.test_database
            # and inside that DB, a collection called "files"
            collection = db.files

            try:
                # open a file
                f = open( os.path.join(location, file))
                # read the entire contents, should be UTF-8 text
                text = f.read()
                # check if the file is already stored in the database
                if not collection.find_one({"file_name": file}):
                    # build a document to be inserted
                    text_file_doc = {"file_name": file, "contents" : text }
                    # insert the contents into the "file" collection
                    collection.insert(text_file_doc)
            except IOError:
                print "Error: can't find file or read data "
except:
    print "Couldn't open the directory"
