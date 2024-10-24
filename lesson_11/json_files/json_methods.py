import json
from json import JSONDecoder, JSONEncoder # responsible for json transformations
from pprint import pprint # pretty print
from textwrap import indent


def my_parse_float(value):
    print(f"Found FLOAT {value} in json")
    return round(float(value), 5)

def my_parse_int(value) -> float:
    print(f"Found INT {value} in json")

    if  0 <= int(value) <= 100:
        return  int(value) / 100
    else:
        return int(value)

def my_parse_pairs(pair_object):
    print(f"Found PAIRS OBJECTS {pair_object} in json")
    for index, (key, value) in enumerate(pair_object):
        new_key = str(key).upper()
        if isinstance(value, str):
            new_value = value.upper()
        else:
            new_value = value
        pair_object[index] = (new_key, new_value)
    return pair_object

with open("example.json", "r") as json_file:
    json_data = json.load(
        fp=json_file,
        parse_float=my_parse_float,
        parse_int=my_parse_int,
        object_pairs_hook=my_parse_pairs
    )

    pprint(json_data)

python_obj = {
  "int_value": 31221,
  "float_value": 213.2131843274232,
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
  },
  123: "wrong_key?",
  (1, 2, 4): "wrong_key?",
  None: "wrong_key?",
  True: "wrong_key?",
}

with open("new_json_file.json", "w") as json_file:
        json.dump(
            python_obj,
            json_file,
            indent=2,
            separators=(",", ":"),
            skipkeys=True,

        )



