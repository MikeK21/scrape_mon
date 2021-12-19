#!/usr/bin/python3
# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import scrape_mon
import urllib.request
import json
from datetime import date
from datetime import timedelta
import os

hostName = "localhost"
serverPort = 8080

APIKEY = "C227WD9W3LUVKVV9"

try:
    resultSet = scrape_mon.getEnvRequest()
except:
    print("Could not contact scrape_mon")  
    
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        hello_world = scrape_mon.scrape_json(os.getenv("STOCKSYMBOL"),os.getenv("NDAYS"))
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes(f"<p>{hello_world}.</p>", "utf-8"))
        #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

if __name__ == "__main__":    
     
 
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
        

    webServer.server_close()
    print("Server stopped.")
