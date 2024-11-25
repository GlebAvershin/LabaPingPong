import socket


def request(client_socket):
    """
    Функция принимает один параметр — сокет клиента, через который сервер получает запросы и отправляет ответы.
    """
    try:
        request = client_socket.recv(256).decode('utf-8').strip() # Получаем запрос
        print(f"Получен запрос: {request}")

        if request == "ping": # Если ping, отправляем pong
            response = "pong"
        else:
            response = "error"

        client_socket.send(response.encode('utf-8')) # Отправляем ответ
        print(f"Отправлен ответ: {response}")

    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")
        client_socket.send("error".encode('utf-8'))

    finally:
        client_socket.close() # Закрываем соединение


def server():
    """
    функция запускает сервер и создает сокет для входящих подключений от клиентов.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем TCP-сокет

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Для повторного использование адресов

    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen()
    print("Сервер ожидает подключения...")

    while True:
        client_socket, client_address = server_socket.accept() # Принимаем подключение
        print(f"Подключен клиент: {client_address}")
        request(client_socket)

if __name__ == "__main__":
    server()
