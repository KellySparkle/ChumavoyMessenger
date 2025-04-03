import tkinter as tk
from tkinter import simpledialog, scrolledtext
import socketio

# Подключение к серверу
sio = socketio.Client()

# Функция для подключения
def connect():
    try:
        sio.connect("http://127.0.0.1:5000")
        print("Подключено к серверу!")
    except Exception as e:
        print("Ошибка подключения:", e)

# Создаём окно чата
root = tk.Tk()
root.title("Чумавой Мессенджер")
root.geometry("400x500")

# Запрашиваем имя пользователя
user_name = simpledialog.askstring("Введите имя", "Как вас зовут?", parent=root)
if not user_name:
    user_name = "Аноним"

# Поле для отображения сообщений
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled", height=20, width=50)
chat_display.pack(pady=10)

# Поле для ввода сообщений
msg_entry = tk.Entry(root, width=40)
msg_entry.pack(pady=5)

# Функция для отправки сообщений
def send_message():
    message = msg_entry.get()
    if message:
        sio.send({"name": user_name, "message": message})
        msg_entry.delete(0, tk.END)

send_button = tk.Button(root, text="Отправить", command=send_message)
send_button.pack()

# Функция для обновления чата при получении новых сообщений
@sio.on("message")
def on_message(data):
    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"{data['name']}: {data['message']}\n")
    chat_display.config(state="disabled")
    chat_display.yview(tk.END)

# Подключение к серверу и запуск чата
connect()
root.mainloop()
