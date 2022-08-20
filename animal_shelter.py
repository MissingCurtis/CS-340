from pymongo import MongoClient
from bson.objectid import ObjectId


    
class AnimalShelter (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:41488' % (username, password), authSource='AAC')
        self.database = self.client['AAC']
        
        
    # Complete this create method to implement the C in CRUD
    def create(self, data):
        try:
            if data is not None:
                return self.database.animals.insert_one(data).acknowledged  
            else:
                return False
        except:
            return False
        
    # Complete this create method to implement the R in CRUD
    def read(self, criteria=None):
        try:
            if criteria is not None:
                data = self.database.animals.find(criteria,{"_id": False})
                return data
                for document in data:
                    print(document)
            else:
                print("Error: Either query or values are empty")
        except:
            print("Error: Either query or values are empty")
    
    # Complete this create method to implement the U in CRUD
    def update(self, query, new_values):
        try:
            if query is not None and new_values is not None:
                data = self.database.animals.update_one(query, new_values)
                return data
            else:
                print("Error: Either query or values are empty")
        except:
            print("Error: Either query or values are empty")
        
    # Complete this create method to implement the D in CRUD
    def delete(self, criteria=None):
        try:
            if criteria is not None:
                data = self.database.animals.delete_one(criteria)
                return data
            else:
                print("Error: The query data is empty.")
        except:
            print("Error: The query data is empty.")