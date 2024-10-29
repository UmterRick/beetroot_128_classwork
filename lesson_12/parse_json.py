"""
JSON support:
int
float
str
list
bool (true/false <-> True/False)
object - dict
null - None

JSON Rules:
key - double-quoted strings
No single-quoted values
No comma after last element
"""
import json
import datetime

json_data_string = '''
{
  "id": 12321321412,
  "name": "User",
  "email": "user@gmail.com",
  "token": "almdskdmnjbdfako21321njnds",
  "courses": [3212421, 12422, 321343, 42131],
  "links": {
    "github": "www.com",
    "linkedin": "www.com"
  }
}
'''

json_data = {
  "id": 12321321412,
  "name": 'User',
  "email": """user@gmail.com""",
  24312: '''almdskdmnjbdfako21321njnds''',
  "courses": [3212421, 12422, 321343, 42131, ],
  "links": {
    "github": "www.com",
    "linkedin": "www.com"
  },
}


with open("example.json") as json_file:
    parsed = json.load(json_file) # expect file object

print(parsed)
print(type(parsed))
print(parsed.get("token"))


parsed_2 = json.loads(json_data_string) # expect string object
print(parsed_2)
print(type(parsed_2))
print(parsed_2.get("token"))



with open("example_dump.json", "w") as json_file:
    json.dump(json_data, json_file, indent=2)


json_dumped_string = json.dumps(json_data)
print(json_dumped_string)
print(type(json_dumped_string))
# print(json_dumped_string.get("token"))

def get_user_data():
  with open("example.json") as user_data_file:
      user_data = json.load(user_data_file)
      return user_data


def set_user_data(data):
  with open("example.json", "w") as user_data_file:
    json.dump(data, user_data_file, indent=2)



user = get_user_data()

user["birth_date"] = datetime.date(1999, 1, 15).isoformat()
user["email"] = "user_new@gmail.com"


try:
    if "3801232131" in user:
        user.pop("3801232131")
    else:
        print(">>> Not found")
except KeyError:
    print("Not found")


print(">>>", user)

set_user_data(user)