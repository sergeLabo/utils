
"""
Télécharge une url.
Peut aussi l'enregister
"""

from urllib.request import Request, urlopen
from urllib.error import URLError
import socket



class HttpDownload:
    """
    Télécharge une url.

    Retourne
        - un string si text (html)
        - des bytes si fichier
    Enregistre dans un fichier

    Usage:
        hd = HttpDownload()
        # recupère la réponse
        resp = hd.get_response(url, timeout=2)
        # ou enregistre
        hd.save_response(u, timeout=2, name=name)
        # ou les 2
        resp = hd.save_response(u, timeout=2, name=name)
    """

    def request(self, someurl, timeout=2):
        """
        Télécharge une url.
        Retourne des bytes: https://bit.ly/2wau8j1 ou string vide
        """
        print("\nTéléchargement de l'url:", someurl)

        req = Request(someurl)
        # Simulation d'un navigateur
        req.add_header('User-agent', 'Multi lame 1.0')

        response = None
        try:
            response = urlopen(req, timeout=timeout)
            response = response.read()
        except URLError as e:
            if hasattr(e, 'reason'):
                print('Server is unreachable.')
                print('Reason: ', e.reason)
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: ', e.code)
        except socket.timeout as e:
            print('Request connection timeout, no response from server ')
        except:
            print("Final Error with", someurl, "Response None")

        return response

    def decode_or_not(self, response):
        """
        Decode utf-8 si text, rien si fichier.
        Donc text = utf-8, fichier = bytes
        """

        try:
            response = response.decode("utf-8")
        except:
            response = response

        return response

    def save_response(self, someurl, timeout=2, name="toto"):
        """
        Enregistre la réponse de la requête à someurl,
        dans un fichier name
        Retourne aussi la réponse.
        Si réponse None, ne fera rien, retourne None
        """
        response = self.get_response(someurl, timeout=2)

        if isinstance(response, str):
            save_data_in_file(response, name, mode='w')
        elif isinstance(response, bytes):
            save_data_in_file(response, name, mode='wb')
        else:
            print("Ni str ni bytes !")

        return response

    def get_response(self, someurl, timeout=2):
        """
        Retourne la réponse de la requête, decodée si str
        """

        response = self.request(someurl, timeout=timeout)
        response = self.decode_or_not(response)
        return response


def save_data_in_file(data, fichier, mode):
    """
    Mode 'w' écrit un string dans le fichier
    Mode 'wb' écrit des bytes dans le fichier
    donc enregistre un fichier
    w ecrase
    a ajoute
    """
    with open(fichier, mode) as my_file:
        my_file.write(data)
    my_file.close()

def test():
    """
    Download some url, and save.
    """

    from time import sleep

    url = [
        "https://wiki.labomedia.org/images/9/9a/Tablo-motherboard3.jpg",
        "http://ressources.labomedia.org/Accueil",
        "http://www.totoestfou.org",
        "http://jeuxlibres.org",
        "http://ressources.labomedia.org/toto",
        "https://wiki.labomedia.org/index.php/Fichier:Tablo-motherboard3.jpg",
        "https://bit.ly/2wau8j1"
        ]

    name = "z"
    while 1:
        for u in url:

            hd = HttpDownload()

            resp = hd.get_response(u, timeout=2)
            print("url done", u)
            sleep(2)

            name += "z"
            hd.save_response(u, timeout=2, name=name)
            print("url saved", name, u)
            sleep(2)


if __name__ == '__main__':
    test()
