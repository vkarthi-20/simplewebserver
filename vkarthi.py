from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>Karthi</title>
    </head>
    <body>
        <enter><center>
            Device Specifications - 25017522
        </center>
            
        </enter>
        <hr>
        <table border="5" cellspacing="5" cellpadding="10">
            <tr bgcolor="yellow">
                <td>Device Name</td>
                <td>Processor</td>
                <td>Storage</td>
                <td>Graphics Card</td>
                <td>RAM</td>
            </tr>
            <tr>
                <td>TMP215-75-G2</td>
                <td>Intel(R) Core(TM) Ultra 5 125H (1.20 GHz)</td>
                <td>954 GB</td>
                <td>128 MB</td>
                <td>16.0 GB</td>
            </tr>
        </table>
    </body>
</html>    
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