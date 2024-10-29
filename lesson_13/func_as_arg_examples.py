# sorted()
import datetime
from pprint import pprint


def element_transform(element):
    return element ** 3


list_1 = [1, 2, 3, 4, 5]

list_2 = []
for i in list_1:
    list_2.append(element_transform(i))

list_3 = [element_transform(i) for i in list_1]

result = list(map(element_transform, list_1))
print(list_2)
print(list_3)
print(result)

unsorted_list = [3, -34, 8, -9, 0, 1]
unsorted_smth = [
    {
        "name": "Item 1", "price": 10, "comments": [
        {
            "user": 1,
            "text": "Nice!",
            "date": datetime.date(2000, 1, 10)
        },
        {
            "user": 2,
            "text": "Bad!",
            "date": datetime.date(2000, 5, 2)
        }

    ]

    },
    {"name": "Item 2", "price": 11, "comments": [
        {
            "user": 2,
            "text": "Normalno...",
            "date": datetime.date(2001, 2, 10)
        },

    ]
     },
    {"name": "Item 3", "price": 34, "comments": []},
    {"name": "Item 4", "price": 66, "comments": []},
    {"name": "Item 5", "price": 99, "comments": [
        {
            "user": 2,
            "text": "Normalno...",
            "date": datetime.date(2000, 2, 10)
        },

    ]},

]


def sort_items(item):
    def sort_comments_by_date(c):
        return c["date"]

    comments = item["comments"]
    sorted_comments = sorted(comments, key=sort_comments_by_date, reverse=True)
    if sorted_comments:
        return sorted_comments[0]["date"]

    return datetime.date(1000, 1, 1)


print(sorted(unsorted_list))
for item in sorted(unsorted_smth, key=sort_items, reverse=True):
    print(item)
    print("-----" * 10)



def filter_with_comments(item):
    return bool(item["comments"]) and item["price"]

print("========" * 10)
items_with_comments = filter(filter_with_comments, unsorted_smth)
for item in items_with_comments:
    print(item)
    print("-----" * 10)


