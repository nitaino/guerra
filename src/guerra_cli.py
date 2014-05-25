"""
Este es el interface para el terminal.

"""

from argparse import ArgumentParser
from ipadd import genera_ips

if __name__ == '__main__':
    
    parser = ArgumentParser()
    
    parser.add_argument('genera_ips', help='Este genera i printea una lista de IPs con las series dadas. Trata: 0-255.0-255.0-255.0-255')
    args = parser.parse_args()
    
    genera_ips(args.genera_ips)


