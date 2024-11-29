import socket
import time

def send():
    """
    Функция клиента, которая отправляет запрос и ожидает ответ от сервера.
    """
    try:
        while True:
            # Запрашиваем у пользователя ввод сообщения
            message = input("Введите сообщение для отправки (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                print("Выход из программы.")
                break
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Новый сокет для каждого подключения
            client_socket.connect(('127.0.0.1', 12345))
            client_socket.send(message.encode('utf-8'))
            print(f"Отправлен запрос: {message}")

            response = client_socket.recv(256).decode('utf-8').strip()
            print(f"Получен ответ: {response}")

            if response == "pong":
                print("Тест пройден успешно.")
            else:
                print("Ошибка: получен неверный ответ.")

            client_socket.close()
            time.sleep(1)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    send()