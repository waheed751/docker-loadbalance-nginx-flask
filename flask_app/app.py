from flask import Flask
from flask import request
import socket

app = Flask(__name__)

@app.route("/")
def index():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return "Server IP address: " + host_ip

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

