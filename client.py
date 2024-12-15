import socket
import time
import argparse

def send(client_index):
    """
    Функция клиента, которая отправляет запрос и ожидает ответ от сервера.
    """
    try:
        while True:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Новый сокет для каждого подключения
            client_socket.connect(('127.0.0.1', 12345))
            client_socket.send(f"ping от клиента {client_index}".encode('utf-8'))  # Отправляем ping с индексом клиента
            print(f"Отправлен запрос: ping ")

            response = client_socket.recv(256).decode('utf-8').strip()
            print(f"Получен ответ: {response}")

            if response.startswith("pong"):
                print("Тест пройден успешно.")
            else:
                print("Ошибка: получен неверный ответ.")

            client_socket.close()
            time.sleep(1)  # Задержка между запросами
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('index', type=int)

    args = parser.parse_args()
    send(args.index)
