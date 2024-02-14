from socket import *
import threading

def handleClient(connectionSocket,addr):
    print(addr[0])
    keep_communacating = True

    while keep_communacating:
        sentence = connectionSocket.recv(1024).decode()
        print(sentence)
        if sentence.strip()== "close":
            keep_communacating = False
        else:
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode)
           
    connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print('From server: ')
while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()

    
