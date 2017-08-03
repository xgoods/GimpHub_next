#!/usr/bin/python
import websocket
import _thread, threading
import time

from socketIO_client import SocketIO, BaseNamespace

class ChatNamespace(BaseNamespace):

    def on_aaa_response(self, *args):
        print('on_aaa_response', args)
        #self.emit('bbb')

class test(object):

    def __init__(self):
        #websocket.enableTrace(True)
        # self.ws = websocket.WebSocketApp("ws://echo.websocket.org/",
        #                             on_message=self.on_message,
        #                             on_error=self.on_error,
        #                             on_close=self.on_close)
        # self.ws.on_open = self.on_open
        self.running = True





        self.socketIO = SocketIO('localhost', 5000)
        chatNamespace = self.socketIO.define(ChatNamespace, '/chat')
        self.socketIO.emit('connect', self.on_update)
        #chatNamespace.on('connect', self.on_update)
        # chatNamespace.emit('joined', 'test', 'test')
        # chatNamespace.on('joined', self.on_joined)
        chatNamespace.on('imgupdate', self.on_joined)
        chatNamespace.on('echo2', self.on_echo)
        # self.socketIO.on('echo', self.on_echo)
        # chatNamespace.emit('joined', 'test', 'test')

        threading.Thread(target=self.run_th).start()
        time.sleep(1)
        chatNamespace.emit('echo')
        # self.socketIO.emit('echo')
        print("echo sent")
        #self.socketIO.wait(seconds=2)
        #

    def run_th(self):

        self.socketIO.wait(seconds=5)

    def on_echo(self, *args):
        print("echo received")

    def on_update(self, *args):
        print("update")
        print(args)

    def on_joined(self, *args):
        print("joined")
        print(args)



    # def on_error(self, ws, error):
    #     print error
    #
    # def on_close(self, ws):
    #     print "### closed ###"

    def on_open(self, ws):
        def run(*args):
            ws.send("joined", )
            for i in range(30000):
                if self.running is False:
                    ws.close()
                    return None
                time.sleep(1)
                ws.send("Hello %d" % i)
            time.sleep(1)
            ws.close()
            print("thread terminating...")
        _thread.start_new_thread(run, ())


if __name__ == "__main__":
    t = test()
