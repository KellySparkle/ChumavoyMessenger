import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print("Подключено к серверу мессенджера!")

@sio.on('message')
def on_message(data):
    print(f"Новое сообщение: {data}")

sio.connect('http://localhost:5000')  # Укажи свой IP или домен для раздачи

while True:
    msg = input("Введите сообщение: ")
    if msg.lower() == "exit":
        break
    sio.send(msg)

sio.disconnect()