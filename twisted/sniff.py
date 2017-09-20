#!/usr/bin/env python3
from socket import * 

if __name__ == '__main__':
    target = input('Enter host to scan: ')
    targetIP = gethostbyname(target)
    print ('Starting scan on host ', targetIP)

    #scan reserved ports
    for i in range(1, 10010):
        s = socket(AF_INET, SOCK_STREAM)

        result = s.connect_ex((targetIP, i))

        if(result == 0) :
            print ('Port %d: OPEN' % (i,))
        s.close()
