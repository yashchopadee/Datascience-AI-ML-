# before pydantic

class Student:
    def __init__(self, name: str, age: int, gpa: float):
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
#error
#s2 = Student(name = 99, age = "Twenty", gpa = False)   # False -> 0 -> 0.0
#print(s2)


# Real world approch , in API data arrives in Dictionary format.

raw_data = {
     "name":"sham",
     "age":20,
     "gpa":3.5

}
s2 = Student(**raw_data)
print(s2)

print("-"*20)

raw_data1 = {
     "name":"sham",
     "age":"21",
     "gpa":"21.5"

}

s3 = Student(**raw_data1)
print(s3)
print(type(s3.name),type(s3.age),type(s3.gpa))

print("-"*20)

#raw_data2 = {
 #    "name":"sham",
  #   "age":21.5,
   #  "gpa":"21.5"

#}

#s4 = Student(**raw_data2)
# print(s4)
# print(type(s4.name),type(s4.age),type(s4.gpa))
# validationError
print("-"*20)
from pydantic import ValidationError

raw_data4 = {
     "name" : 1234,
     "age"  : "Twenty"
}
try: 
   s4 = Student(**raw_data4)
except ValidationError as e:
    print(f"Total number of errors found: {e.error_count()}")
    for err in e.errors():
        print(f"fields : {err['loc']}  , Type : {err['type']} , Message: {err['msg']}")


print("-"*40)







print("-"*40)

from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str


# Required and Non-nullable
#what happens when value is not provide in dict

value = {
    "product_id" : "50"
}
try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Field : {err["loc"]} , Type : {err['type']}, Message: {err['msg']}")


print("-"*50)
# Required and Non-nullable
#what happens if value is None

value = {
    "product_id" : "50",
    "name": None
}
try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Field : {err["loc"]} , Type : {err['type']}, Message: {err['msg']}")



print("-"*40)

from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str | None


# Required and nullable
#what happens when value is not provide in dict

value = {
    "product_id" : "50"
}
try:
    p1 = Product(**value)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Field : {err["loc"]} , Type : {err['type']}, Message: {err['msg']}")




print("-"*40)

# Required and nullable
#what happens when value is None

value = {
    "product_id" : "50",
    "name": None
}
try:
    p1 = Product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Field : {err["loc"]} , Type : {err['type']}, Message: {err['msg']}")


# Try writing a small Product (BaseModel) in your notebook with fields: 
#     product id: int, name: str, price: float, in_stock: bool,
#     and test it with:
# Valid coerced inputs (product_id="50", price="199,99", in_stock="1"),
# A broken input inside try / except ValidationError as et and print e.error_count(),

from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    product_id: int
    name: str 
    price: float
    in_stock: bool
try:
    rr = Product(product_id="50", price="199,99", in_stock="1") # it it use lax mode

except ValidationError as e:
    print(f"total number of error found:{e.error_count()}")
    for err in e.errors():
        print(f"Field : {err["loc"]} , Type : {err['type']}, Message: {err['msg']}")

