import urllib.request
import json
blog_content = urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts").read()
print(blog_content)
str_blog_content = blog_content.decode("utf-8")
list_blog_content=json.loads(str_blog_content)
print(list_blog_content)
 
values = range(23)
for i in values:
    print(i)
    n = ("what is the number?:")
    
def user_id(number):
    number = int(number)
    return user_id
    
user_number = input("what is the id?:")
calculated_id = user_id(user_number)
print("The user id of {} is {}".format(user_number,calculated_id))




    
