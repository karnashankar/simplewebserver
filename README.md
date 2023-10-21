# Developing a Simple Webserver
## Date: 23.09.23
## AIM:
To develop a simple webserver to serve html pages.

## DESIGN STEPS:
### Step 1: 
HTML content creation
### Step 2:
Design of webserver workflow
### Step 3:
Implementation using Python code
### Step 4:
Serving the HTML pages.
### Step 5:
Testing the webserver

## PROGRAM:
```
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body bgcolor="yellow">
<h1>Top 5 highest revenue companies!<h1>
    <ol>
        <li>Apple</li>
        <li>Microsoft</li>
        <li>Saudi Aramco</li>
        <li>Alphabet (Google)</li>
        <li>Amazon</li>  
      </ol>
</body>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()

```

## OUTPUT:
![image](out.png)

![image](output1.png)

## RESULT:
The program for implementing simple webserver is executed successfully.
