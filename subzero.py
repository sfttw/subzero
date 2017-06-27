#!/usr/bin/env python3

import dns.resolver #import the module
import argparse
global wordlist
global domain
global log
import threading


log = []
logfile = 'log.txt'
logfile = open(logfile,'a')

def check(target):
    myResolver = dns.resolver.Resolver() #create a new instance named 'myResolver'
    try:
        myAnswers = myResolver.query(target, "A") #Lookup the 'A' record(s) for google.com
        for rdata in myAnswers: #for each response
            answer = target + ' ' + rdata.to_text() + '\n'
            #print(answer)
            logfile.write(answer)
            #print(rdata) #print the data
    except:
        pass
    try:
        myAnswers = myResolver.query(target, "CNAME") #Lookup the 'A' record(s) for google.com
        for rdata in myAnswers: #for each response
            answer = target + ' ' + rdata.to_text() + '\n'
            #print(answer)
            logfile.write(answer)
            #print(rdata) #print the data
    except: 
        pass    

def main():
    while len(wordlist) > 0:
        target = wordlist.pop() + '.' + domain
        check(target)
        print('\r {}'.format(target), end='')


    
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Subzero - subdomain bruteforcer')
    parser.add_argument('-d','--domain', help='Domain', required=True)
    parser.add_argument('-w','--wordlist', help='Wordlist', default='names.txt', required=False)
    parser.add_argument('-v','--verbose', help='Verbose', required=False, action='store_true')
    parser.add_argument('-o','--output', help='Output file', required=False)
    args = vars(parser.parse_args())

    if args['domain']:
        wordlist = open(args['wordlist'], 'r').readlines()
        wordlist = [i.strip() for i in wordlist]
        wordlist.reverse()
        domain = args['domain']
        threads = []
        for i in range(1000):
            try:
                t = threading.Thread(target=main)
                threads.append(t)
                t.start()
            except:
                print('threading error')
    else:
        print("Usage: subzero.py -d [domain]")
        
    