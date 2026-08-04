
# Pydantic 


from pydantic import BaseModel 

class Student(BaseModel):

    name: str = 'nitist'

new_Students =  {}
Student = Student(**new_Student)

print(type(Student))


# Optional 


from pydantic import BaseModel
from typing import Optional  

class Student(BaseModel):

    name: str = 'nitist'
    age : Optional{int} = None  

new_Students =  {}
Student = Student(**new_Student)

print(type(Student))