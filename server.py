import socket
import signal
import sys

def request(client_socket):
    """
    Функция принимает один параметр — сокет клиента, через который сервер получает запросы и отправляет ответы.
    """
    try:
        request = client_socket.recv(256).decode('utf-8').strip()  # Получаем запрос
        print(f"Получен запрос: {request}")

        if request.startswith("ping"):
            client_index = request.split()[1]  # Получаем индекс клиента
            response = f"pong"
        else:
            response = "error: Неверный запрос"

        client_socket.send(response.encode('utf-8'))  # Отправляем ответ
        print(f"Отправлен ответ: {response}")

    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")
        client_socket.send("error".encode('utf-8'))
    finally:
        client_socket.close()  # Закрываем соединение

def signal_handler(sig, frame):
    print("Закрытие сервера...")
    server_socket.close()  # Закрываем сокет сервера
    sys.exit(0)  # Завершаем программу

def server():
    """
    Функция запускает сервер и создает сокет для входящих подключений от клиентов.
    """
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Создаем TCP-сокет

    try:
        server_socket.bind(('127.0.0.1', 12345))
    except OSError as e:
        print("Ошибка: Порт уже занят. Убедитесь, что другой сервер не запущен.")
        sys.exit(1)
    server_socket.listen()
    print("Сервер ожидает подключения...")

    signal.signal(signal.SIGINT, signal_handler)  # Обработка сигнала прерывания 

    while True:
        try:
            client_socket, client_address = server_socket.accept()  # Принимаем подключение
            print(f"Подключен клиент: {client_address}")
            request(client_socket)
        except Exception as e:
            print(f"Ошибка при принятии подключения: {e}")

if __name__ == "__main__":
    server()
