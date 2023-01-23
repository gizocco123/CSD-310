students.find()
MongoDB: insert_one()
John = {
    "first_name": "John"
}
john_student_id = "1010"

MongoDB: find_one()
doc = db.collection_name.find_one({"student_id": "1010"})
print(doc["student_id"])

MongoDB: delete_one()
db.collection_name.remove({"student_id":"1010"})
print(doc["john_student_id"])