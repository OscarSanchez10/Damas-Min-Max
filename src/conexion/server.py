import socket
from _thread import *
import sys

server = "10.0.0.36"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(f"Error al enlazar el socket: {e}")

s.listen(2)
print("Esperando conexion...")


def threaded_client(conn):
    conn.send(str.encode("Conectado"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Conexion Perdida")
                break
            else:
                print("Recibiendo: ", reply)
                print("Enviando: ", reply)

            conn.sendall(str.encode(reply))
        except Exception as e:
            print(f"Error en la comunicación: {e}")
            break

    print("Conexion Perdida")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Conectado a:", addr)

    start_new_thread(threaded_client, (conn,))
