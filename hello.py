#!/usr/bin/env python3

import os 
import json
import templates
import sys
import secret

print(json.dumps(dict(os.environ), indent= 2))

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)

if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(posted)
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")

    username = posted.split("=")[1].split("&")[0]
    print(username)
    password = posted.split("=")[-1]
    print(password)

    if (secret.username == username and secret.password == password):

        print("Set-Cookie: login = true")


print('Content-Type: text/html')
if (os.environ['QUERY_STRING'] != ''):
    
    print("")
    
    print("""
    <!doctype html>
    <html>
    <body>
    <h1>Hello I am html</h1>
    """)
    print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']} </p>")
    print("<ul>")
    for parameter in os.environ['QUERY_STRING'].split('&'):
        (name, value) = parameter.split('=')
        print(f"<li><em>{name}</em> = {value}</li>")
    print("</ul>")
    # print(os.environ['HTTP_COOKIE'].split("=")[1])

    
    if (os.environ['HTTP_COOKIE']):
        print(templates.secret_page("HELLO", "HELLO"))
    print("</body></html>")

# # curl -i localhost:8080/hello.py
# # What environment variable contains the query parameter data?

# #  Question 3: What environment variable contains information about the user’s browser?
# # Brower "HTTP_USER_AGENT": "curl/7.64.1",
# print(f"<p> HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']} </p>")



# Question 4: How does the POSTed data come to the CGI script?

print(templates.login_page())



       
        
    




# Refrence to https://www.tutorialspoint.com/setting-up-cookies-in-python#:~:text=We%20use%20Set%2DCookie%20HTTP,%5Cn%5Cr%5Cn. on Jan 25, 2021
# Question 5: What is the HTTP header syntax to set a cookie from the server?


# Question 6: What is the HTTP header syntax the browser uses to send the cookie back?

# Question 7: In your own words, what are cookies used for?
