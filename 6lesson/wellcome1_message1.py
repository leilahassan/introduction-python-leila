def welcome_message(name):
    message =  "Welcome {} to Fairmont hotels. It is a pleasure to serve you".format(name)
    return message
name = input("What is your name?")

output = welcome_message(name)
print(output)