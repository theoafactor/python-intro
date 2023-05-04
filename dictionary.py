user = {
    "name": "James",
    "age": 12,
    "email": "james@email.com",
    "ranks": ["entry_level", "junior", "senior"],
    "location": {
        "state": "lagos",
        "lga": "mainland",
        "street": "Oweh",
        "number": 35,
        "country": "Nigeria",
        "accepted_codes": [101, 111, 134, 154]
    }
}

# key : value
print(user["location"]["accepted_codes"][2])
