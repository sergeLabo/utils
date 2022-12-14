
import socket
from time import sleep



class TcpClient3:
    """
    Uniquement python 3
    Envoi et réception sur le même socket en TCP.
    """

    def __init__(self, ip, port):

        self.ip = ip
        self.port = port
        self.server_address = (ip, port)
        self.data = None
        self.sock = None
        self.connected = 0
        self.create_socket()

    def create_socket(self):
        """Création du socket sans try, et avec connexion."""

        # Création
        if not self.sock:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.settimeout(0.05)
            print("    Création du socket client {}".format(self.server_address))
            self.connect_sock()

    def connect_sock(self):
        sleep(1)
        try:
            self.sock.connect(self.server_address)
            self.connected = 1
            print("Connexion du client sur {}".format(self.server_address))
        except:
            self.connected = 0
            self.sock.close()
            print("Connexion impossible du client sur {}".format(self.server_address))

    def re_connect_sock(self):
        try:
            self.sock.send(b'hello')
        except socket.error as e:
            self.connected = 0
            self.sock.close()
            self.sock = None
            print("Déconnecté", e)
            self.create_socket()

    def send(self, msg):
        """Envoi d'un message, avec send, msg doit être encodé avant."""

        # Création d'un socket si besoin
        if not self.sock:
            self.create_socket()

        # Envoi
        try:
            self.sock.send(msg)
        except:
            print("Envoi raté: {}".format(msg))
            # Nouvelle création d'une socket
            self.sock.close()
            self.sock = None

    def reconnect(self):
        """Reconnexion."""

        self.sock = None
        self.create_socket()

    def close_sock(self):
        """Fermeture de la socket."""

        try:
            self.sock.close()
        except:
            print("La socket client est déjà close")

        self.sock = None

    def listen(self, buff):
        """Retourne les data brutes reçues, et vide le buffer TCP"""

        raw_data = None
        raw_data = self.sock.recv(buff)

        return raw_data

    def clear_buffer(self, buff):
        try:
            while self.sock.recv(buff):
                print("Vidange du buffer")
        except:
            print("Buffer vide")


if __name__ == "__main__":

    ip = "127.0.0.1"
    port = 8000

    clt = TcpClient3(ip, port)

    while 1:
        clt.re_connect_sock()
        try:
            data = clt.listen(8000)
            clt.send("ping".encode("utf-8"))
        except:
            data = None
            print("Pas de réception sur le client TCP")

        if data:
            print("test.jpg enregistré")

    clt.close_sock()
