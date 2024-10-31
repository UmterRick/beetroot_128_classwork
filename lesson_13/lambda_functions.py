# lambda functions
import datetime
from pprint import pprint

l = [-1, 132, 6, -4, -2, 3, -4, 5, 6, 7]


def is_positive(n):
    return True if n > 0 else False


# result = list(filter(is_positive, l))
result = list(filter(lambda n: n < 0, l))

print(result)

map_result = list(map(lambda n: (n ** 2) / 10, l))
print(l)
print(map_result)

l_2 = [(1, 1), (2, 2), ("a", "a")]
result = list(map(lambda n: n[0] + n[1], l_2))
print(result)

CONST = 2
result = list(map(lambda n: n // 2 if n % CONST == 0 else n * 2, l))
print()
print(l)
print(result)

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



result = sorted(unsorted_smth, key=lambda item: -len(item["comments"]), reverse=True)
print("\n\n")
pprint(result)
