import socket
import time


def send():
    """
    функция клиента, которая отправляет запрос и ожидает ответ от сервера
    """
    try:
        while True:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # новый сокет для каждого подключения
            client_socket.connect(('127.0.0.1', 12345))
            client_socket.send("ping".encode('utf-8'))
            print("Отправлен запрос: ping")

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
