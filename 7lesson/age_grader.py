def grader(age):
    age = int(age)
    if age < 13:
        return "pimary"
    elif age == 13:
        return "secondary"
    elif age  < 18:
        return "secondary"
    else:
        return "tertiary"
    

user_input = input("What is the students age?:")
computed_age = grader(user_input)
print("The students age is {}".format(computed_age))