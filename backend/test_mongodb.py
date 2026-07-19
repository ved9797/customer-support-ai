from database.mongodb import chat_collection

test_document = {
    "message": "MongoDB connection successful!"
}

result = chat_collection.insert_one(test_document)

print("Inserted Document ID:", result.inserted_id)