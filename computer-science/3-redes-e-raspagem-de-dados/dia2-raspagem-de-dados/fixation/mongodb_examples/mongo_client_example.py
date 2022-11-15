from pymongo import MongoClient


#Using context:
with MongoClient() as client:
    db = client.catalogue
    for book in db.books.find({"title": {"$regex": "t"}}):
        print(book["title"])

#by default, host is localhost and port 27017
#those values can be modified by passing an URI
#client = MongoClient("mongodb://localhost:27017")
# client = MongoClient()

#create "catalogue" database if doesnt exist:
# db = client.catalogue

#search for a document in a colection (without filters):
# print(db.books.find_one())

# #search with filters:
# for book in db.books.find({"title": {"$regex": "t"}}):
#     print(book["title"])


# documents = [
#     {
#         "title": "A Light in the Attic",
#     },
#     {
#         "title": "Tipping the Velvet",
#     },
#     {
#         "title": "Soumission",
#     },
# ]

# db.books.insert_many(documents)

#"book" represents data got by crawling:
# book = {
#     "title": "A Light in the Attic"
# }

# document_id = db.books.insert_one(book).inserted_id
# print(document_id)

# #create "books" collection if doesnt exist:
# students = db.books

client.close() #closes the connection with database