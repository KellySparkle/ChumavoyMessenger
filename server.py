from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Сервер мессенджера работает!"

@socketio.on("message")
def handle_message(data):
    print(f"{data['name']}: {data['message']}")
    send(data, broadcast=True)  # Отправляем сообщение всем клиентам

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
