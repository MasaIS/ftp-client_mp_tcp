import socket
import time


host = '127.0.0.1'
port = 50000
buff = 1024

# create TCP Stream socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# reuse socket of TIME_WAIT 
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#  bind socket
soc.bind((host, port))

while True:
    # wait some connections (Maxinum connection)
    soc.listen(1)
    print("Waiting...")

    # accept new connection and refuse another connections
    conn, addr = soc.accept()
    print("Accepted new connection.")

    while True:
        try:
            # recieve massage
            rx_msg = conn.recv(buff) # bytes
            print(rx_msg.decode("UTF-8")) #decode(byte to utf-8)
            conn.send('Getting message.'.encode())
            time.sleep(1)
            # When rx_msg is null
            if rx_msg == "".encode():
                break

        except socket.error:
            conn.close()
            break