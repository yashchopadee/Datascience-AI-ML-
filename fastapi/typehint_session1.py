st = "ram"
print(type(st))

a = 10
print(type(a))
a = '10'
print(type(a))

print("*"*20)
text: str = "ram"
text1: str = 100
print(type(text))
print(type(text1))

text2: str = 100
print(type(text2))
print("-"*20)

def fun(param):
    param.reverse()
    return param
print(fun(["1","2"]))


def fun1(param: list[str]) ->list[str]:
    param.reverse()
    return param
print(fun1(['1','2']))

def full_name(first_name,last_name):
    return first_name.title() + " " + last_name.title()
print(full_name("ram","patil"))

def full_name1(first_name:str, last_name:str) -> str:
   return first_name.title() + " " + last_name.title()
print(full_name("sham","patil"))

print("-"*20)

"""
types in type int
1.str
2.int
3.bool
4.bytes
5.float
"""
def get_items(items_a: str,items_b: int,items_c: bool,items_d: bytes,items_e: float):
    return items_a,items_b,items_c,items_d,items_e
print(get_items('ram',100,True,b"a",10.2))

print("-"*20)

from typing import Any

def random_fun(data: Any):
    return data
print(random_fun(100))
print(random_fun("Ram"))

print("_"*20)

"""Generic type
1.list[str]
2.tuple[int,int,itn]
3.set[bytes]
4.dicts[str,str]
"""

def process_list(items: list[str]):
    for items in items:
        print(items)
process_list(['1','2','3'])

print("-"*20)
def process_tuple_and_set(items_t: tuple[int,int,str],items_s: set[bytes]):
    return items_t,items_s

print(process_tuple_and_set((1,2,'a'),{b'a'}))

def process_dict(prices: dict[str, int]):
    for item_name, item_price in prices.items():
        print(item_name," -> ",item_price)
process_dict({"chair":100,"table":250})

print("-"*20)
"""Union
Declare variable accepting multiple types using "|"
"""
def process_id(item: str | int):
    print("ID : ",item, "of type : ", type(item))
process_id(100)
process_id("ram")   

def bwt_hi(name: str | None = None):
    if name is not None:
        print("hello",name)

    else:
        print("hello BWT Class...!")
bwt_hi("ram")
bwt_hi()

print("-"*20)

from collections.abc import Iterable

def reverse_array(items: Iterable[str]) -> list[str]:
    return list(items)[::-1]

print(reverse_array(['1','2']))

print("-"*20)

class Person:
    def __init__(self, name: str):
         self.name = name
def get_person_name(one_person: Person)-> str:
    return one_person.name
p = Person("ram")

print(get_person_name(p))

# Literal in typeHint

from typing import Literal


def set_access(name: str, role: Literal["admin","editor","viewer"]) -> str:
    return f"{name} has a {role} permission"

print(set_access("ram","admin"))
print(set_access("sham","viewer"))
print(set_access("kiran","xyz"))


print("_"*20)

# Enum in typeHint

from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

def assign_role(user: str,role: Role) -> str:
    return f"{user} has a role name = {role.name}, role value  = {role.value}"

print(assign_role("Ram", Role.ADMIN))


