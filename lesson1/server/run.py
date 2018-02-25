# -*- coding: utf-8 -*-
import socket
import os
import re

def parse_http_user_agent(request):
    result = re.search(r'User-Agent: ([^\n]+)', request_string)
    if result:
        return result.group(1)
    else:
        return "None"

def main_message(request):
    return "Hello mister!\nYou are: " + parse_http_user_agent(request)

def parse_http_method(request):
    result = re.search("\S+", request)
    if result:
        return result.group(0)
    else:
        return


def parse_by_request_code(code):
    protocol = "HTTP/1.1 "
    if code == 200:
        return protocol + " 200 OK\n\n"
    elif code == 404:
        return protocol + " 404 Not found\n" + "\nPage not found\n"
    elif code == 400:
        return protocol + " 400 Bad Request\n" + "\nBad request\n"
    elif code == 405:
        return protocol + " 405 Method Not Allowed\n" + "\nMethod not allowed\n"
    else:
        return protocol + " 500 Internal Server Error\n" + "\nInternal Server Error\n"


def get_list_of_files():
    result = "Index of /media:\n"
    list = os.listdir("files")
    for f in range(len(list)):
        result += list[f] + "\n"
    return result


def get_file(name):
    path = "files/" + name
    if os.path.exists(path):
        file = open(path, 'r')
        result = file.read()
        file.close()
        return parse_by_request_code(200) + result + "\n"
    else:
        return "HTTP/1.1 " + " 404 Not found\n" + "\nFile not found\n"

def get_response(request):
    if parse_http_method(request) != "GET":
        return parse_by_request_code(405)
    command = re.search(" (\S*)", request)
    result = command.group(1)
    file_name = re.search("/media/(\S+)", result)
    if result:
        if result == "/":
            return parse_by_request_code(200) + main_message(request)
        elif result == "/media" or result == "/media/":
            return parse_by_request_code(200) + get_list_of_files()
        elif file_name:
            return get_file(file_name.group(1))
        elif result == "/test" or result == "/test/":
            return parse_by_request_code(200) + request
        else:
            return parse_by_request_code(404)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #связываем сокет с хостом localhost и портом 8000
server_socket.listen(0)  #слушаем сокет(параметр - максимальное кол-во подключений в очереди)

print 'Started'
while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #выводим адрес клиента
        request_string = client_socket.recv(2048)  #получаем через сокет 2048 байт
        client_socket.send(get_response(request_string))  #отправляем клиенту ответ
        client_socket.close()
    except KeyboardInterrupt:  #обработка клавишы завершения
        print 'Stopped'
        server_socket.close()  #закрытие соединения
        exit()
