from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Student:
    name: str
    age: int
    score: int


s = Student(name="Bob", age= 20, score= 88)
std_data = s.to_json()
print("Dump Student:", std_data)

s1 = Student.from_json(std_data)
print(s1)