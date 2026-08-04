
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
    email : Emailstr
    cgpa : float = Field(gt=0,lt=10,default=5,description='a decimal value repracnting the cgpa of the Student')

new_Students =  {'age ' : '32' ,'email': 'abc@gmail.com', 'cgpa':5}

Student = Student(**new_Student)

print(Student)