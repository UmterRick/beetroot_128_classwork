my_dict = {
    "hello": "standard word to greet someone",
    "bye": "standard word to end meeting",
    "1": "a",
    "2": "b",
    "3": "c",
    "4": "d",
}
x = [1, 2, 3]
x[0] = -99
print(hash("hello"))
print(hash("1"))


print(hash(1))
print(hash(111))
print()
print(hash("hello"))


print(len(my_dict))
print(my_dict)
print()
print(my_dict["1"])
print(my_dict["2"])
print(my_dict["3"])
print(my_dict["4"])


my_dict_2 = {
    "key_1": [1, 2, 3],
    100: "100 apples",
    (1, 2, 3): "tuple value",
    # [1, 2, 3]: "listvalue"
    (1, 2, 3, "Hello", ("a", "b", "c")): "tuple 2 value"

}
print(my_dict_2["key_1"])
print(my_dict_2[100])
print(my_dict_2[(1, 2, 3)])
# "key_1": "value_1"


x = dict(
    [
        ("a", "value"),
        ("a", "value_2"),
        ("b", "value"),
        ("key", "key_value")

    ]
)
print(x["a"])

empty_dict = {}
print(empty_dict)
empty_dict["key_0"] = "0 value"
print(empty_dict)
for i in range(1, 11):
    empty_dict[f"key_{i}"] = f"{i} value"
print(empty_dict)

print("-----" * 20)
print(empty_dict.items(), type(empty_dict.items()))

for element in empty_dict.items():
    key = element[0]
    value = element[1]
    print(element)

for k, v in empty_dict.items():
   print(k, " -----> ", v)

print("\n END OF CODE")






