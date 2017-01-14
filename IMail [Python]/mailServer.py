import socketserver
import time

print(' This is the mailServer ! ')
print(' This Server recives all your mail !')
print(' Keep this running at all times to get your mail !')
print(' ')

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip().decode('utf8')
        self.dataArray = self.data.split('[/-split-\]')
        print("{} wrote: ".format(self.client_address[0]) + self.data)
        print(" ")
        with open('Mail/m-' + time.strftime("%H-%M-%S") + 'mail.txt', "a+") as f:
            f.write("<Imail>\n \n Sender : " + self.dataArray[1] + '\n \n Message : ' + self.dataArray[0] + '\n  \n Network : ' + self.client_address[0])

if __name__ == "__main__":
    HOST, PORT = "localhost", 350

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
