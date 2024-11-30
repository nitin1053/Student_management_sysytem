from pydantic import BaseModel, Field
from typing import Optional

class Student(BaseModel):
    id: Optional[str] = Field(None, alias="id")
    name: str
    age: int
    class_name: str = Field(..., alias="class")
    subjects: list[str]

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 15,
                "class": "10th Grade",
                "subjects": ["Math", "Science"]
            }
        }
