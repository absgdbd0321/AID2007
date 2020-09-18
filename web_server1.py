"""
    web server
    完成一个类，提供给别人
    让他能用这个类快速的搭建后端web服务
    IO多路复用和http训练
"""

from socket import *
from select import select
import re





class WebServer:
    def __init__(self,host="0.0.0.0",port = 80,html = None):
        self.host = host
        self.port = port
        self.html = html
        self.create_sock()
        self.bind()
        self.rlist = []
        self.wlist = []
        self.xlist = []

    def create_sock(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host,self.port)
        self.sock.bind(self.address)


    def start(self):
        self.sock.listen(5)
        print("Listen the port %d"%self.port)
        # 首先加入监听套接字
        self.rlist.append(self.sock)
        while True:
            rs,ws,xs = select(self.rlist,self.wlist,self.xlist)
            for r in rs:
                if r is self.sock:
                    connfd,addr = self.sock.accept()
                    connfd.setblocking(False)
                    self.rlist.append(connfd)
                else:
                    self.handle(r)

    def handle(self,connfd):
        request = connfd.recv(1024).decode()
        print(request)

        pattern = r"[A-Z]+/s+(?P<info>/\s*)"
        result = re.match(request,pattern)
        if result:
            info = result.group("info")
            print("请求内容：",info)
            self.send_reponse()
        else:







if __name__ == '__main__':
    httpd = WebServer(host="0.0.0.0",port = 8000,html = "./static")
    httpd.start()