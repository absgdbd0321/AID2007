from socket import *

sockfd = socket()
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(5)

connfd,addr = sockfd.accept()
print("Connect from",addr)


# 接受到的是来自浏览器的HTTP请求
data = connfd.recv(1024*1024)
print(data.decode())

with open("jj.jpg","br") as f:
    data = f.read()

# 将数据组织为响应格式
response = "HTTP/1.1 200 OK\r\n"
response += "Content-Type:image/jpeg\r\n"
response += "\r\n"
response = response.encode() + data


connfd.send(response)


connfd.close()
sockfd.close()