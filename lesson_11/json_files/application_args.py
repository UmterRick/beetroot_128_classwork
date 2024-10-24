import  argparse
import os
import pathlib
from fileinput import filename

parser = argparse.ArgumentParser()

parser.add_argument("--filename", help="name of the phonebook file")
parser.add_argument("--username", help="name of the phonebook file")

my_args = parser.parse_args()

file_name = "new_json_file_222.json"

print("Does file exists?",  os.path.exists(file_name))


if not os.path.exists(file_name):
    ...