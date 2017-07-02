#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''not yet ready for prime time'''
import argparse
import socket
import threading
count = 0
global args
global domain
from contextlib import closing
ports = []
log = []
ports.extend(range(65536))
ports.reverse()
def check(host, port):
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        try:sock.settimeout(args['timeout'])
        except:sock.settimeout(.3)
        if sock.connect_ex((host, port)) == 0:
            print('\nOpen: '+str(port))
            log.append(str(port))
        else:
            pass





def main(target='example.com'):
    try:target=args['domain']
    except:pass
    global count
    while len(ports) > 0:
        check(target, ports.pop())
        count += 1
        print('\rComplete: {} / {}'.format(count, 65535), end='')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='scan.py')
    parser.add_argument('domain', help='target to scan, like domain.com')
    parser.add_argument('-p','--ports', help='Ports (0-65355)', default='0-65355', required=False)
    parser.add_argument('-v','--verbose', help='Verbose', required=False, action='store_true')
    parser.add_argument('-o','--output', help='Output file', required=False, default='log.txt')
    parser.add_argument('-t','--threadcount', help='Number of Threads', required=False, default=50, type=int)    
    parser.add_argument('-to','--timeout', help='socket timeout', required=False, default=.3)
    threads =[]
    args = vars(parser.parse_args())
    for i in range(50):
        t = threading.Thread(target=main)
        threads.append(t)
        t.start()  
    
    