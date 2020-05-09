from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

clients = {}
addresses = {}

HOST = "127.0.0.1"
PORT = 1234
BUFFERSIZE = 1024
ADDR = (HOST, PORT)
SOCK = socket(AF_INET, SOCK_STREAM)
SOCK.bind(ADDR)


def incoming_connections(): #handlin incoming client connection
   
    while True:
        client, client_address = SOCK.accept()
        print("%s:%s has connected." % client_address)
        client.send("Type your name to recognize yourself! Type Again".encode("utf8"))
        addresses[client] = client_address
        Thread(target=handle_client, args=(client, client_address)).start()

def handle_client(conn, addr):  #client socket passes as an argument.
    
    name = conn.recv(BUFFERSIZE).decode("utf8")               
    msg = "%s from [%s] has joined, type quit to exit " % (name, "{}:{}".format(addr[0], addr[1]))
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name
    while True:
        msg = conn.recv(BUFFERSIZE)
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name + ": ")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes("%s has left the chat." % name, "utf8"))
            break

def broadcast(msg, prefix=""): 
     for sock in clients: #broadcast message to everyone
        sock.send(bytes(prefix, "utf8") + msg)

if __name__ == "__main__":
    SOCK.listen(3)  # Listen to 3 connection
    print("Server Running")
    print("Waiting for connections...")
    ACCEPT_THREAD = Thread(target=incoming_connections)
    ACCEPT_THREAD.start()  
    ACCEPT_THREAD.join()
    SOCK.close()
