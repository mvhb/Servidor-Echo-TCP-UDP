import socket
import sys

def readFile():
    arquivo = open("metodo.txt", "r")
    metodo = ""
    while metodo == "":
        metodo = arquivo.readline().upper()
    return metodo

def main():
    try:
        arquivo = open("metodo.txt", "r")
        check()
    except:
        print("[+]Arquivo nao encontrado.")
        print("[+]Encerrando aplicacao")
        sys.exit()

def check():
    print("[+]Aguardando o método que será utilizado para comunicação.")
    if readFile() == "UDP":
        UDP()
    elif readFile() == "TCP":
        TCP()
    else:
        print("[+]Nenhum metodo valido foi encontrado.")
        
def UDP():
    print("[+]Iniciando servidor UDP.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_ip = ""
    server_port = 5555
    server = (server_ip, server_port)
    sock.bind(server)

    while True:
        print("[+]Esperando conexao.")
        data, client_info = sock.recvfrom(1024)
        print("[+]Conexao estabelecida.")
        print("[+]Mensagem de " + client_info[0] + " recebida: " + data.decode())

        if data.decode().upper() == "FIM":
            break
        print("[+]Enviando " + data.decode() + " para " + client_info[0] + ".")
        sent = sock.sendto(data, client_info)

    print("[+]Encerrando servidor.")

def TCP():    
    print("[+]Iniciando servidor TCP.")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = ""
    server_port = 5555
    server = (server_ip, server_port)
    sock.bind(server)
    sock.listen(1)
    print("[+]Esperando conexao.")
    connection, client_address = sock.accept()
    print("[+]Conexao estabelecida.")

    while True:
        data = connection.recv(1024)
        print("[+]Mensagem de " + client_address[0] + " recebida: " + data.decode())
        if data.decode().upper() == "FIM":
            break
        print("[+]Enviando " + data.decode() + " para " + client_address[0] + ".")
        connection.sendall(data)
    print("[+]Encerrando servidor.")
    sock.close()

if __name__ == "__main__":
    main()
