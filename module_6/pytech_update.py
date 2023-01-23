students.find{()}
MongoDB: update_one
result = db.collection.update_one({"student_id": 1007}, {$"set": {"last_name": "John"}})
MongoDB: find_one()
doc = db.collection_student.find_one({"student_id": "1007"})
print(doc["student_id"])