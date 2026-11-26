# before pydantic

class Student:
    def __int__(self,name: str,age: int,gpa: float):
        self.name = name
        self.age = age
        self.gpa = gpa

s = Student(name = 99,age = "Twenty", gpa = False)
print(s.name, " " , s.age," ", s.gpa)

print("-"*20)

# after pydantic

from pydantic import BaseModel

class Student(BaseModel):
      name:str
      age:int
      gpa:float

s1 = Student(name = "Ram", age= 21, gpa=2.9)
print(s1)

print("-"*20)

s2 = Student(name = 99, age = "Twenty", gpa = False)
print(s2)