import socket

class Client:
    def __init__(self, port):
        self.mysoc = socket.socket()
        self.mysoc.bind(('localhost',port))
        self.mysoc.listen()

    def wait4msg(self):
        self.conn, self.addr = self.mysoc.accept()

    def sendmsg(self, data):
        data = str(data)
        self.msg = bytes(data,'utf8')
        self.conn.send(self.msg)
