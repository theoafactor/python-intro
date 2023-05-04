def greeting(username):
    print("good morning " + username)
    return "Thank you"



data = input("Please enter your username: ")

feedback = greeting(data)

print(feedback)