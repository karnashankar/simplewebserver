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
