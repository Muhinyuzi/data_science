# -*- coding: utf-8 -*-

import re

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
(?P<host>.*)
(\s+)
(?:\S+)
(\s+)
(?P<user_name>\S+)
(\s+)
\[(?P<time>.*)\]\
(\s)
(?P<request>"(.)*")"""

print("Claude")
for item in re.finditer(pattern,logdata,re.VERBOSE):
    # We can get the dictionary returned for the item with .groupdict()
    #print(item.groupdict())
    print(item.groupdict(default="-"))
    log_list.append(item.groupdict())  

print(log_list)
print(len(log_list))    


"""def logs():
    logs = []
    w = '(?P<host>(?:\d+\.){3}\d+)\s+(?:\S+)\s+(?P<user_name>\S+)\s+\[(?P<time>[-+\w\s:/]+)\]\s+"(?P<request>.+?.+?)"'
    with open("datasets/logdata.txt", "r") as f:
        logdata = f.read()
    for m in re.finditer(w, logdata):
        logs.append(m.groupdict())
    return len(logs)

d = logs()
print(d)"""



import re
def logs():
    mydata = []
    with open("datasets/logdata.txt", "r") as file:
        logdata = file.read()
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
        new_item = (item.groupdict())
        mydata.append(new_item)
    return(mydata)

d = logs()
print(logs())
print(len(d))
