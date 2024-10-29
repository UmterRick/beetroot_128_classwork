import json
from json import JSONDecodeError

# json - java script object notation
# key - value
# no single quotes, only double quotes
# no comma after last item


# json.load
# json.loads
json_string = """
{
  "int_value": 31221,
  "float_value": 213.21312,
  "str_value": "value",
  "list_value": [
    1,
    1.321,
    "list_element",
    [
      1,
      2,
      3
    ]
  ],
  "object_value": {
    "name": "Name",
    "last_name": "Last Name",
    "age": 100
  }
}


"""
json_content = json.loads(json_string)
print(type(json_content))
print(json_content)

print("---------" * 20)

json_file_name = "new_json_file.json"
with open(json_file_name, "r") as json_file:
    try:
        # json_content = json.load(json_file)
        json_content = json.loads(json_file.read())
        print(json_content, type(json_content))
    except JSONDecodeError:
        print("check your json file")
        exit()
    for key, value in json_content.items():
        print(f"Key -> {key} ({type(key)}) | Value -> {value} ({type(value)})")
    # json_content = json_file.read()
    # print(json_content)
    # print(type(json_content))
    