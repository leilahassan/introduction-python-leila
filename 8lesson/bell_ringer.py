import urllib.request
bell_information = urllib.request.urlopen("http://date.jsontest.com/").read()
print(bell_information)