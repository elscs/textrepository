from socket import socket,AF_INET,SOCK_DGRAM
serve_socket=socket(AF_INET,SOCK_DGRAM)
serve_socket.bind(('127.0.0.1',8888))
while True:
    client_date,add=serve_socket.recvfrom(1024)
    print(client_date.decode('utf-8'))
    if client_date.decode('utf-8')=='bye':
        break
    serve_date=input('input date')
    serve_socket.sendto(serve_date.encode('utf-8'),add)
serve_socket.close()