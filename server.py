import socketserver
import os
import datetime
import time
import utils

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # handling logic
        id, data = str(self.data.split("-"))
        timestamp = round(time.time() * 1000)
        self.logging(id, {"event": data, "time": timestamp})
        self.request.sendall({"event": data, "time": timestamp})


    def logging(self, id, data):
        """
        append the latest event in the log file 
        data format is {"time": ...., "event":...}
        """
        folder = 'tcp_logs'
        # Check folder exists
        if not os.path.exists(folder):
            os.makedirs(folder)

        file_path = utils.get_file_path(id)                

        with open(file_path, "a+") as f:
            text = f.read()
            if not text:
                f.write("time,event\n")
            f.write(str(data["time"]) + "," + str(data["event"]) + "\n")
        
        return file_path

if __name__ == "__main__":
    HOST, PORT = "", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        print("Server is up at port 9999")
        server.serve_forever()


