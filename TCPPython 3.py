from socket import *
import threading

def handleClient(connectionSocket,addr):
    print(addr[0])
    keep_communacating = True

    while keep_communacating:
        sentence = connectionSocket.recv(1024).decode()
        print(sentence)
        response = "error, please send a proper message"
        if sentence.strip()== "close":
            keep_communacating = False
            response ="closing the connection"
        elif sentence.startswith("lower "):
            sentence = sentence[6:]
            response = sentence.lower
        elif sentence.startswith("upper "):
            sentence = sentence[6:]
            response = sentence.upper()
        # elif sentence.startswith("count "):
        #     sentence = sentence[6:]
        #     response = sentence.count(sentence)
        elif sentence.strip()=="time":
            response = "i can't tell the time yet"
        connectionSocket.send(response.encode()) 
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('From server: ')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()