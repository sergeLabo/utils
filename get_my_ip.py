

import os, sys
import subprocess, re
from functools import reduce


def get_my_ip():
    """
    Retourne l'adresse ip du pc sur le réseau local.
    Valable pour python 3.x
    Non valable sur android
    """

    #A generator that returns stripped lines of output from "ip address show"
    iplines = (line.strip() for line in subprocess.getoutput("ip address show")\
                                                           .split('\n'))
    #Turn that into a list of IPv4 and IPv6 address/mask strings
    addresses1=reduce(lambda a,v:a+v,(re.findall(r"inet ([\d.]+/\d+)",
                                    line)+re.findall(r"inet6 ([\:\da-f]+/\d+)",
                                    line) for line in iplines))
    #Get a list of IPv4 addresses as (IPstring,subnetsize) tuples
    ipv4s = [(ip,int(subnet)) for ip,subnet in (addr.split('/') for addr in\
                                              addresses1 if '.' in addr)]
    # my IP
    try:
        ip = ipv4s[1][0]
        print("IP =", ip)
    except:
        print("Cet ordinateur n'est pas connecté à un réseau !")
        ip = "127.0.0.1"

    return ip

if __name__ == '__main__':
    get_my_ip()
