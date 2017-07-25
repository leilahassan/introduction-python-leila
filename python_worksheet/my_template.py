template_str="My name is {} and I am {} years old.I am currently studying {}"
name=input("what is your name?:")
age=input("what is your age?:")
unit=input("what are you studying?:")
print(template_str.format(name,age,unit))