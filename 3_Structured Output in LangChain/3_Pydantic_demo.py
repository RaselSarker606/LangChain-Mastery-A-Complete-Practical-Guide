from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'rasel'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=5, default=2.5, description = "A decimal value representing the cgpa of the student")

new_student = {'age':32, 'email':'sarker15@diu.edu.bd'}

student = Student(**new_student)

#======================================
student_dict = dict(student)
student_json = student.model_dump_json()
