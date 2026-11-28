from pydantic import BaseModel , ValidationError

class product(BaseModel):
    product_id: int
    name: str = "yash"

#Optional and non-nullable
# what happen when value is not provided in dict
value = {
    "product_id" : "50"
}

try:
   p1 = product(**value)
   print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc'] }, Type : {err['type']} , Message: {err['msg']}")

print("-"*50)

# optiona and non-nullable
# what happens if value is None
value = {
    "product_id" : "50",
    "name" : None
}

try:
    p1 = product(**value)
    print(p1)
except ValidationError as e:
    print(f"Total number of error: {e.error_count()}")
    for err in e.errors():
        print(f"Fields : {err['loc']} , Type : {err['type']} , Message: {err['msg']}")



print("-"*60)



from pydantic import BaseModel, ValidationError

class product(BaseModel):
    product_id: int
    name: str | None = None

#Optional and nullable
#what happens when value is not passed
value = {
    "product_id" : "50"
}

try:
    p1 = product(**value)
    print(p1)
except ValidationError as e:
    print(f"total numbers of error: {e.error_count()}")
    for err in e.errors():
        print(f"Field : {err['loc']} , Type : {err['type']} , message: {err['msg']}")

print("->"*50)

from pydantic import BaseModel, ValidationError

class product(BaseModel):
    product_id: int
    name: str | None = None

#Optional and nullable
#what happens if value is none
value = {
    "product_id" : "50",
    "name" : None
}

try:
    p1 = product(**value)
    print(p1)
except ValidationError as e:
    print(f"total numbers of error: {e.error_count()}")
    for err in e.errors():
        print(f"Field : {err['loc']}, Type : {err['type']} , message: {err['msg']}")

print("-"*50)

# pydantic does not validate deffault value by itself.
class product(BaseModel):
    product_id: int = "abc"

p = product()
print(p)

print("-"*70)

from datetime import datetime, UTC

class BadExample(BaseModel):
    created_dt: datetime = datetime.now(UTC)

b1 = BadExample()
b2 = BadExample()

print(b1)
print(b2)

print("-"*90)


from datetime import datetime, UTC
import time
class BadExample(BaseModel):
    created_dt: datetime = datetime.now(UTC)

b1 = BadExample()
time.sleep(2) # in BadExample it always true bcz this time not change it will be always same
b2 = BadExample()

print(b1)
print(b2)
print(b1.created_dt == b2.created_dt) # always True (using time.sleep)


print("-"*90)

#correct example
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
import time


class GoodExample(BaseModel):
    request_id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory = lambda: datetime.now(UTC))

g1 = GoodExample()
time.sleep(2) # import the time and use this time.sleep(2) to different output give as per time
g2 = GoodExample()

print(g1)
print(g2)
print(g1.created_at == g2.created_at) # always false


print("-"*60)

from datetime import datetime, UTC
from uuid import UUID, uuid4
from pydantic import BaseModel, Field

class LLMChatRequest(BaseModel):
    #Required
    prompt: str

    #Optional with sensible prodution defaults
    model:str = "gpt-40-mini"
    temperture: float = 0.7
    max_tokens: int | None = None      #None = let provider use model default
    system_prompt: str | None = None   #Optional system instruction
    stop_sequences: list[str] = Field(default_factory =list)

    # Auto-generated metadata per request
    trace_id: UUID = Field(default_factory = uuid4)
    created_at: datetime = Field(default_factory = lambda: datetime.now(UTC))

req = LLMChatRequest(prompt="Explain RAG in 2 sentences.")
print(req)

req.stop_sequences.append("hello stop") # it gives the value of given list in stop_sequences

print(req)

print("-"*70)

class prompt(BaseModel):
    text: str = Field(description="User text value")
    user_id:  str  = Field(..., description="Caller user id") # ..., make this field mandatory
    value: str | None = Field(default=None, description="random value") # it is optional

print(prompt(text="abc",user_id="pqr",value=None))


print("<->"*60)
#How to validate default value
class ValidateVal(BaseModel):
    product_id: int = Field(default="xyz" , validate_default=True)# it will check this value is actual int or not check with Field 

try:
    ValidateVal()
except ValidationError as e:
    print(e.errors()[0]['msg'])

print("<->"*60)

#Dynamic data asingn
class ModelData(BaseModel):
    model_name : str
    version: int = 1
    attribute_val: str = Field(
        default_factory=lambda data:f"{data['model_name']}:{data['version']}") # it will be dynacmicaly assing this model_name and version 
    

a= ModelData(model_name="gpt")
print(a)

print(">-<"*60)

'''"""
Create an ExperimentRun(BaseModel) for an ML training tracker with:

experiment_name: str (required, non-nullable)
parent_run_id: str | None (required key, can be None)
learning_rate: float = 0.001 (optional, non-nullable)
run_id: UUID (auto-generated fresh UUID per instance via default_factory)
metrics: dict[str, float] (defaults to a fresh empty dict {} via
default_factory)


Test creating 2 separate runs and verify run1.run_id != run2.run_id!
"""'''
from pydantic import BaseModel,Field
from uuid import UUID, uuid4

class ExperimentRun(BaseModel):
    experiment_name: str
    parent_run_id: str | None
    learning_rate: float = 0.001
    run_id: UUID = Field(default_factory=uuid4)
    metrics: dict[str, float] = Field(default_factory=dict)


run1 = ExperimentRun(
    experiment_name="Model Training",
    parent_run_id=None
)

run2 = ExperimentRun(
    experiment_name="Model Testing",
    parent_run_id="RUN101"
)

print(run1)
print(run2)

print(run1.run_id != run2.run_id)


