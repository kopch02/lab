from pymongo import MongoClient


def find_document(collection, elements, multiple=False):
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        #у коллекции вызываем функции mongodb
        return collection.find_one(elements)


def delete_document(collection, query):
    collection.delete_one(query)


def update_document(collection, query_elements, new_values):
    collection.update_one(query_elements, {'$set': new_values})


def insert_document(collection, data):
    return collection.insert_one(data).inserted_id


client = MongoClient('localhost', 27017)

# подключение к бд
db = client['semestrov']

# найти коллекцию
collection_corpuses = db['corpuses']
collection_rooms = db['rooms']
collection_customers = db['customers']
collection_organizations_booking = db['organizations_booking']
collection_complaints = db['complaints']

#поиск