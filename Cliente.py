import socket
import sys

def dell_method():
    open('metodo.txt', 'w').close() #apaga o que está escrito no arquivo  
    return

def readMethod():
    arquivo = open("metodo.txt","r")
    metodo = arquivo.read().upper()
    return metodo
    
def main():
    try:
        arquivo = open("metodo.txt", "w")
        servico = input("[+]Digite TCP ou UDP para confirmar o protocolo de transporte:\nPara encerrar a conexão digite FIM\n")
        arquivo.write(servico)
        arquivo.close()
        check()
    except:
        print("[+]Arquivo nao encontrado.")
        print("[+]Encerrando aplicacao")
        sys.exit()
        
def check():       
    if readMethod() == "FIM":
        dell_method()
        print("Conexão encerrada")
    elif readMethod() == "UDP":
        UDP()
    elif readMethod() == "TCP":
        TCP()
    else:
        print("[+]Nenhum metodo valido foi encontrado.")
        
def UDP():
    
    print("[+]Iniciando cliente.")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_ip = 'localhost'
    server_port = 5555

    server = (server_ip, server_port)
    dell_method()
    while True:
        print("[+]Digite sua mensagem: ")
        message = input()

        print("[+]Iniciando conexao e enviando mensagem.")

        sent = sock.sendto(message.encode("utf-8"), server)
        if message.upper() == "FIM":
            break
        data, server_info = sock.recvfrom(1024)
        print("[+]Conexao estabelecida e aguardando mensagem resposta do servidor.")
        print("[+]Mensagem do servidor recebida: " + data.decode())

    print("[+]Encerrando cliente.")

def TCP ():

    print ("[+]Iniciando cliente.")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = 'localhost'
    server_port = 5555

    server = (server_ip, server_port)
    dell_method()

    try:
        sock.connect(server)
    except:
        print("[+]O servidor TCP nao pode ser encontrado.")
        print("[+]Encerrando cliente.")
        sock.close()
        sys.exit()

    print("[+]Conexao estabelecida.")

    while True:
        print("[+]Digite sua mensagem: ")
        message = input()
        sock.send(message.encode("utf-8"))
        data = sock.recv(1024)
        if message.upper() == "FIM":
            break

        print("[+]Aguardando mensagem resposta do servidor.")
        print("[+]Mensagem do servidor recebida: " + data.decode())

    print("[+]Encerrando cliente.")
    sock.close()
    print("[+]Cliente encerrado.")

if __name__ == "__main__":
    main()
