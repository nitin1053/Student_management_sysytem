from fastapi import APIRouter, HTTPException, status
from app.models import Student
from app.database import student_collection
from bson import ObjectId

router = APIRouter()

# Helper functions
def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "class": student["class_name"],
        "subjects": student["subjects"],
    }

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_student(student: Student):
    student_dict = student.dict(by_alias=True)
    result = await student_collection.insert_one(student_dict)
    return {"id": str(result.inserted_id)}

@router.get("/{id}")
async def get_student(id: str):
    student = await student_collection.find_one({"_id": ObjectId(id)})
    if student:
        return student_helper(student)
    raise HTTPException(status_code=404, detail="Student not found")

@router.get("/")
async def list_students():
    students = []
    async for student in student_collection.find():
        students.append(student_helper(student))
    return students

@router.put("/{id}")
async def update_student(id: str, student: Student):
    student_dict = student.dict(exclude_unset=True, by_alias=True)
    result = await student_collection.update_one({"_id": ObjectId(id)}, {"$set": student_dict})
    if result.modified_count:
        return {"message": "Student updated successfully"}
    raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(id: str):
    result = await student_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count:
        return
    raise HTTPException(status_code=404, detail="Student not found")
