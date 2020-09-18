from socket import *

sockfd = socket()
sockfd.bind(("0.0.0.0",8000))
sockfd.listen(5)

while True:
    connfd,addr = sockfd.accept()
    print("connect from ",addr)

    data = connfd.recv(1024).decode()

    if not data:
        continue

    info  = data.split(" ")[1]
    print(info)

    if info == "/first.html":
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        with open("first.html") as f:
            response += f.read()

    else:
        response = "HTTP/1.1 400 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>Sorry...<h1>"

    connfd.send(response.encode())


connfd.close()
sockfd.close()




