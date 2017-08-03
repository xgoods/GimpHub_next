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

        self.socketIO.emit('connect', self.on_update)

        time.sleep(2)
        self.socketIO.emit('echo')

        #threading.Thread(target=self.run_th).start()
        time.sleep(2)
        self.socketIO.emit('echo')
        time.sleep(2)
        self.socketIO.emit('echo')
        print("echo sent")
        self.socketIO.wait(seconds=2)
        time.sleep(2)
        #

    def run_th(self):

        self.socketIO.wait()

    def on_echo(self):
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
