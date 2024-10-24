import json

# json.dump
# json.dumps


python_object = {
    "int_from_python": 31221,
    "float_from_python": 213.21312,
    "str_from_python": 'from_python',
    "list_from_python": (
        1,
        1.321,
        "list_element",
        [
            1,
            2,
            3
        ]
    ),
    "object_'';from_python": {
        'name': 'Nam',
        'last_name': "Last Name",
        "age": 100
    }
}

python_object_2 = (1, 2, 3, 4, 5, "Item")

with open("new_json_file.json", "w") as json_file:
    dump_resuls =  json.dump(python_object_2, json_file)
    print(dump_resuls)
    json_string =  json.dumps(python_object)
    print(json_string)
    print(type(json_string))
