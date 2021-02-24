# -*- coding: utf-8 -*-

def example_word_count():
    # This example question requires counting words in the example_string below.
    example_string = "Amy is 5 years old"
    
    # YOUR CODE HERE.
    # You should write your solution here, and return your result, you can comment out or delete the
    # NotImplementedError below.
    result = example_string.split(" ")
    return result

    #raise NotImplementedError()

a = example_word_count()  
print(a) 


#Find a list of all of the names in the following string using regex.
import re
def names():
    simple_string = """Amy is 5 years old, and her sister Mary is 2 years old. 
    Ruth and Peter, their parents, have 3 kids.Eric"""

    # YOUR CODE HERE
    pattern = '[A-Z][\w]*[\W]'#(?=[\W])
    names = re.findall(pattern, simple_string)
    return names

    #raise NotImplementedError()

b = names()  
print(b)
print(len(b))  


def grades():
    with open ("datasets/grades.txt", "r") as file:
        grades = file.read()

    # YOUR CODE HERE
    pattern = "[A-Z][\w]*[\s][A-Z][\w]*(?=[\:][\s][B])" 
    list_of_B = re.findall(pattern, grades) 
    return list_of_B
    #raise NotImplementedError()

c = grades()    

print(c) 


def logs():
    with open("datasets/logdata.txt", "r") as file:
        logdata = file.read()
    
    # YOUR CODE HERE
    """example_dict = {"host":"146.204.224.152", 
                "user_name":"feest6811", 
                "time":"21/Jun/2019:15:45:24 -0700",
                "request":"POST /incentivize HTTP/1.1"}"""
    
   

    #146.204.224.152 - feest6811 [21/Jun/2019:15:45:24 -0700] "POST /incentivize HTTP/1.1" 302 4622
    log_list = []

    pattern="""
    (?P<host>.*) #host
    (\s\S*\s)
    (?P<user_name>\S*)
    (\s\[)
    (?P<time>.*)
    (\]\s)
    (")
    (?P<request>.*) #request
    (")"""

    for item in re.finditer(pattern,logdata,re.VERBOSE):
        # We can get the dictionary returned for the item with .groupdict()
        #print(item.groupdict())
        log_list.append(item.groupdict())


    return log_list
    #raise NotImplementedError() 
     
print(logs())
print(len(logs()))  