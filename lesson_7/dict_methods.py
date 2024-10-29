dict_1 = {
    "key_1": "value_1",
    "key_2": "value_2",
    "key_3": "value_3",
    "key_4": "value_4",
}
print(dict_1)

# dict_1.clear()
# print(dict_1)


x = dict_1.pop("key_2")
print(x)
print(dict_1)

print('------' * 10)
some_key = "key_10"
print(">>>", dict_1.get(some_key, "This key does not exists in dict"))
# print(dict_1[some_key])
print(dict_1)

dict_1.update({"key_a": "value_a", "key_b": "value_b"})
print(dict_1)



dict_2 = {
    "user_1_id": {
        "first_name": "User",
        "last_name": "Test",
        "email": "test-user@gmail.com",
        "address": {
            "country": "Neverland",
            "city": "City",
            "home": {
                "block": 1,
                "floor": 3,
                "apart": 100
            }

        }
    },
    "user_2_id": {}
}


apart_num = dict_2["user_1_id"]["address"]["home"]["apart"]
# Step by step
# user_1 = dict_2["user_1_id"]
# user_address = user_1["address"]
# user_home = user_address["home"]
# apart_num = user_home["apart"]
print("#", apart_num)

