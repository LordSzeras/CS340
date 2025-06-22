from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user='aacuser', password='password'):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = password
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30716
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            # data should be a dictionary
            insert_result = self.database.animals.insert_one(data)
            
            if insert_result.inserted_id:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            results_list = list(self.database.animals.find(data))
            if results_list:
                return results_list
            else:
                return list()
        
        else:
            results = list(self.database.animals.find())
            return results

#Both update and delete have been written to iterate through the cursor created from the
#PyMongo find() function.  Update could be written with just the update_one or update_many
#since it has a query arg built into it.  The same could be done for delete_one and
#delete_many.   

# Create method to implement the U in CRUD

    def update(self, findData, updateData):
        if findData is not None and updateData is not None:
            results = self.database.animals.find(findData)
            updatedDocs = 0
            for doc in results:
                self.database.animals.update_one(doc, updateData)
                updatedDocs+=1
            return updatedDocs
        else:
            raise Exception("Nothing to find, or nothing to change")
            
# Create method to implement the D in CRUD
    def delete(self, data):
        if data is not None:
            results = self.database.animals.find(data)
            deletedDocs = 0
            for doc in results:
                self.database.animals.delete_one(doc)
                deletedDocs+=1
            return deletedDocs
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
