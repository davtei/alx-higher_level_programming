0x10. Python - Network #0
BashPythonScriptingBack-endAPI

    By: Guillaume
    Weight: 1
    Project will start Jun 27, 2023 6:00 AM, must end by Jun 28, 2023 6:00 AM
    Checker was released at Jun 27, 2023 12:00 PM
    An auto review will be launched at the deadline

Resources

Read or watch:

- [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html) (except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation)
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
General

    What a URL is
    What HTTP is
    How to read a URL
    The scheme for a HTTP URL
    What a domain name is
    What a sub-domain is
    How to define a port number in a URL
    What a query string is
    What an HTTP request is
    What an HTTP response is
    What HTTP headers are
    What the HTTP message body is
    What an HTTP request method is
    What an HTTP response status code is
    What an HTTP Cookie is
    How to make a request with cURL
    What happens when you type google.com in your browser (Application level)

Copyright - Plagiarism

    You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
    You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
    You are not allowed to publish any content of this project.
    Any form of plagiarism is strictly forbidden and will result in removal from the program.

Requirements
General

    Allowed editors: vi, vim, emacs
    - A README.md file, at the root of the folder of the project, is mandatory
    All your scripts will be tested on Ubuntu 20.04 LTS
    All your Bash scripts should be exactly 3 lines long (wc -l file should print 3)
    All your files should end with a new line
    All your files must be executable
    The first line of all your bash files should be exactly #!/bin/bash
    The second line of all your Bash scripts should be a comment explaining what is the script doing
    All curl commands must have the option -s (silent mode)
    All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
    The first line of all your Python files should be exactly #!/usr/bin/python3
    Your code should use the pycodestyle (version 2.8.*)
    All your modules should be documented: python3 -c 'print(__import__("my_module").__doc__)'
    All your classes should be documented: python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    All your functions (inside and outside a class) should be documented: python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

Quiz questions
Question #0

What is the curl option to set a body key-value parameter?

    -b

    -d

    -X

Question #1

What is the curl option to follow all redirects?

    -s

    -L

    -X

Question #2

When you are typing https://intranet.hbtn.io in your browser, which HTTP verb is used?

    GET

    POST

    PUT

    DELETE

Question #3

What is the curl option to disable the progression display?

    -b

    -s

    -p

    -c

Question #4

What is the name of the HTTP response header used to define the size, in bytes, of the body of the response?

    Length

    Body-Size

    Content-Length

    Content-Size

Question #5

What will be the port number requested by this URL?

http://www.google.com/apply

    443

    8080

    22

    80

Question #6

What’s the status code number for a permanent redirection (moved permanently)?

    301

    201

    304

    302

    300

Question #7

In the following URL, how many parameters are in the query string?

https://www.google.com/apply?batch=89&location=SF&name=John%20do%20is%20the%20best%20%3D%20c%20is%20fun

    1

    3

    5

    4

    2

Question #8

What’s the status code number for a web page that can’t be found?

    404

    500

    405

Question #9

What’s the status code number for an invalid HTTP request (server can’t understand it)?

    500

    400

    404

Question #10

In the following URL, what’s the protocol?

http://www.google.com

    http

    ftp

    https

Question #11

In the following URL, what’s the resource path?

https://www.google.com/index.html

    /

    www.google.com/index.html

    index.html

Question #12

In the following URL, what’s the name of the parameter in the query string?

https://www.google.com/apply?batch=89

    batch

    89

    apply

Question #13

What is the curl option that defines the HTTP method used?

    -d

    -s

    -X

Question #14

When an HTTP response indicates a redirection, which header defines the URL the client should be redirected to?

    Next-Location

    Redirect-URI

    Redirect

    Redirect-Location

    Location

Question #15

Which HTTP request header indicates the browser used by the client sending the request?

    I-Am

    Origin

    Browser-Name

    User-Agent

Question #16

In the following URL, what’s the resource path?

https://api.google.com/v1/auth/new

    v1/auth/new

    v1

    v1/auth/new/index.html

    v1/auth

Question #17

What is the name of the HTTP response header used to define the formatting of the body? (This header gives details to the client on how to interpret the data received.)

    Format

    Type

    Content-Type

    Content-Format

Question #18

What is the curl option to set a cookie with a key-value pair?

    -a

    -d

    -c

    -b

Question #19

What will be the port number requested by this URL?

https://www.google.com:8080/apply

    80

    8888

    8080

Question #20

In the following URL, how many parameters are in the query string?

https://www.google.com/apply?batch=89&location=SF

    2

    1

    3

Question #21

In this following HTML code, which HTTP verb will be used when you will submit this form?

<FORM action="/12/update.php" method="put">
    <INPUT type="text" name="first_name" value="Bob"/>
    <INPUT type="text" name="last_name" value="Dylan"/>
    <INPUT type="submit" name="update" value="Update" />
<FORM>

    POST

    GET

    PUT

    UPDATE

Question #22

What is the curl option to save the body of the resulting response to a file?

    -r

    -d

    -o

    -b

Question #23

In the following URL, what’s the resource path?

https://www.google.com/assets/scripts/main.js

    assets/scripts/main.js

    assets/scripts

    main.js

Question #24

What is the name of the HTTP response header that defines a list of available HTTP methods for this URL?

    Verbs

    Verbs-Allowed

    Allow

Question #25

What is the name of the HTTP response header used to define the status code of the response?

    Code

    Status

    Http-Status

    Status-Code

Question #26

In this following HTML code, which HTTP verb will be used when you will submit this form?

<FORM action="/login.php" method="post">
    <INPUT type="email" name="email" placeholder="Email" required/>
    <INPUT type="password" name="password" placeholder="Password" required/>
    <INPUT type="submit" name="submit" value="Login" />
<FORM>

    SUBMIT

    POST

    GET

    ENTER

    FORM

Question #27

In the following URL, what’s the sub domain?

https://api-dev.google.com/v1/auth/new

    api-dev

    /v1

    /v1/auth/new

Question #28

Which curl option is used to set an HTTP header to a specific value?

    -H

    -s

    -X

Question #29

In the following URL, what’s the hostname?

http://www.google.com

    www.google.com

    google

    www.google

    google.com

Question #30

What is the name of the HTTP request header that defines the size (in bytes) of the message body?

    Content-Size

    Content-Length

    Size

    Length

Question #31

What is the first digit of status codes that indicate a server error?

    3xx

    1xx

    5xx

    4xx

    2xx

Question #32

What will be the port number requested by this URL?

afp://www.google.com/access_in_port_543

    543

    548

    80

Question #33

In the following URL, what’s the sub domain?

https://api.google.com/v1/auth

    .com

    api

    api.google

Question #34

What is the name of the HTTP request header used to send cookies from the client?

    Cookie

    Set-Cookie

    Cookies

    Send-Cookie

Question #35

What is the name of the HTTP response header used to send cookies to the client from the server?

    Send-Cookies

    Cookie-Setter

    Set-Cookie


Tasks
0. cURL body size
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

    The size must be displayed in bytes
    You have to use curl

Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x10-python-network_0
    File: 0-body_size.sh

1. cURL to the end
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response

    Display only body of a 200 status code response
    You have to use curl

Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x10-python-network_0
    File: 1-body.sh

2. cURL Method
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response

    You have to use curl

Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x10-python-network_0
    File: 2-delete.sh

3. cURL only methods
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.

    You have to use curl

Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x10-python-network_0
    File: 3-methods.sh

4. cURL headers
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response

    A header variable X-School-User-Id must be sent with the value 98
    You have to use curl

Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello School!
guillaume@ubuntu:~/0x10$

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x10-python-network_0
    File: 4-header.sh

5. cURL POST parameters
mandatory
Score: 0.0% (Checks completed: 0.0%)

Write a Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response

    A variable email must be sent with the value test@gmail.com
    A variable subject must be sent with the value I will always be here for PLD
    You have to use curl

Please test your script in the sandbox provided, using the web server running on port 5000

guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x10-python-network_0
    File: 5-post_params.sh

6. Find a peak
mandatory
Score: 0.0% (Checks completed: 0.0%)

Technical interview preparation:

    You are not allowed to google anything
    Whiteboard first

Write a function that finds a peak in a list of unsorted integers.

    Prototype: def find_peak(list_of_integers):
    You are not allowed to import any module
    Your algorithm must have the lowest complexity (hint: you don’t need to go through all numbers to find a peak)
    6-peak.py must contain the function
    6-peak.txt must contain the complexity of your algorithm: O(log(n)), O(n), O(nlog(n)) or O(n2)
    Note: there may be more than one peak in the list

guillaume@ubuntu:~/0x10$ cat 6-main.py
#!/usr/bin/python3
""" Test function find_peak """
find_peak = __import__('6-peak').find_peak

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))

guillaume@ubuntu:~/0x10$ ./6-main.py
6
3
2
None
2
4
guillaume@ubuntu:~/0x10$ wc -l 6-peak.txt
2 6-peak.txt
guillaume@ubuntu:~/0x10$

Repo:

    GitHub repository: alx-higher_level_programming
    Directory: 0x10-python-network_0
    File: 6-peak.py, 6-peak.txt

