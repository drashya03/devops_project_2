from flask import Flask, jsonify, request, render_template
import socket
import datetime
import platform

app = Flask(__name__)

# Home route with a form
@app.route("/", methods=["GET", "POST"])
def home():
    user_name = None
    if request.method == "POST":
        user_name = request.form["name"]
    return render_template("index.html", name=user_name)

# Health check route
@app.route("/health")
def health():
    return jsonify(status="OK", message="App is healthy")

# Server time
@app.route("/time")
def time():
    return jsonify(server_time=str(datetime.datetime.now()))

# System info
@app.route("/info")
def info():
    return jsonify(
        hostname=socket.gethostname(),
        ip=socket.gethostbyname(socket.gethostname()),
        os=platform.system(),
        platform=platform.platform()
    )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
