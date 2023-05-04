email = input("Enter your email: ")


registeredUsers = [
        {
            "firstname": "James",
            "lastname": "Jerry",
            "id": 123,
            "email": "james@email.com"
        },

          {
            "firstname": "Mary",
            "lastname": "Joseph",
            "id": 125,
            "email": "mary@email.com"
        }

]

def loginUser(email):
    for user in registeredUsers:
        if user["email"] == email:
            print("Welcome "+user["firstname"] + "!")
            break
    else:
        print("You are not registered")


## call the function 
loginUser(email)