import socket
import time

host = '127.0.0.1'
port = 50000
buff = 1024

# create TCP Stream socket 
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# reuse socket of TIME_WAIT 
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# connect TCP server
soc.connect((host, port))

while True:
    ### Send ###
    # input message
    tx_msg = input("Input stream: ")
    #print("From Client: ", tx_msg)
    # send message (transfer binary)
    soc.send(tx_msg.encode())

    ### Recieve ###
    rx_msg = soc.recv(buff)
    print(rx_msg.decode("UTF-8"))

    ### Close ###
    if tx_msg == "q":
        # close socket
        soc.close()
        break
