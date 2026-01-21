capitals = {"Ukraine": "Kyiv",
           "Russia": "Moscow",
           "France": "Paris"}

print(capitals["Ukraine"])    # prints value by key "Ukraine"

for key, value in capitals.items():
    print(key, "-", value)

# capitals.clear()     # deletes all items from dict
capitals.pop(key)    # deletes item by its key
capitals.popitem()  # deletes last item in dict

print(capitals.keys())
print(capitals.values())
print(capitals.items())

capitals["Ukraine"] = "Kharkiv"     # reassign value by "Ukraine" key

users = {
    "user_1": {
        "nickname": "wythquan",
        "email": "wythquan@gmail.com",
        "subscribers": 46,
        "collabs": {"glizzy": 3, "wh1teblade": 1}
    },
    "user_2": {
        "nickname": "zeran",
        "email": "zeran@gmail.com",
        "subscribers": 22,
        "collabs": {}
    }
}

for key, value in users.items():
    if type(value) == dict:
        for key2, value2 in value.items():
            if type(value2) == dict:
                if not value2:
                    print(f"{key2}: None")
                for key3, value3 in value2.items():
                    print(f"{key3}: {value3}")
            else:
                print(f"{key2}: {value2}")
    # print(f"{key}: {value}")