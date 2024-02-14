from socket import *

def handleClient(connectionSocket,addr):
    print(addr[0])

    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode)
    connectionSocket.close()
    print(addr)
    print(sentence)

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.bind((serverName, serverPort))
serverSocket.listen(1)
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server: ', modifiedSentence.decode())
clientSocket.close()

    
