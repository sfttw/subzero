#!/usr/bin/env python3
'''subdomain bruteforcer. uses dns.resolver to check for results. 

i kept getting too many false positives using other scripts so i made my own

--elv'''
import dns.resolver #import the module
import argparse

global wordlist
global wordlist_size
global domain
global log
global logfile
global count
global verbose
import threading

log = []

def check(target):
    myResolver = dns.resolver.Resolver() #create a new instance named 'myResolver'
    try:
        myAnswers = myResolver.query(target, "A") #Lookup the 'A' record(s) for google.com
        for rdata in myAnswers: #for each response
            answer = target + ' ' + rdata.to_text()
            if verbose: print('\r[+] '+answer)
            log.append(answer)
    except:
        pass
    try:
        myAnswers = myResolver.query(target, "CNAME") #Lookup the 'A' record(s) for google.com
        for rdata in myAnswers: #for each response
            answer = target + ' ' + rdata.to_text()
            if verbose: print('\r[+] '+answer)
            log.append(answer)
    except: 
        pass    

def main():
    global count
    while len(wordlist) > 0:
        target = wordlist.pop() + '.' + domain
        check(target)
        count += 1
        print('\rComplete: {} / {}'.format(count, wordlist_size), end='')
        #print('\r {}'.format(target), end='')


    
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Subzero - subdomain bruteforcer')
    parser.add_argument('-d','--domain', help='Domain', required=True)
    parser.add_argument('-w','--wordlist', help='Wordlist', default='subdomains-10000.txt', required=False)
    parser.add_argument('-v','--verbose', help='Verbose', required=False, action='store_true')
    parser.add_argument('-o','--output', help='Output file', required=False, default='log.txt')
    parser.add_argument('-t','--threadcount', help='Number of Threads', required=False, default=50)    
    
    args = vars(parser.parse_args())
    threads = []
    
    if args['domain']:
        verbose = args['verbose']
        wordlist = open(args['wordlist'], 'r').readlines()
        wordlist = [i.strip() for i in wordlist]
        wordlist.reverse()
        wordlist_size = len(wordlist)
        domain = args['domain']
        count = 0
        logfile = args['output']
        threadcount = int(args['threadcount'])
        logfile = open(logfile,'a')

        
        for i in range(threadcount):
            try:
                t = threading.Thread(target=main, daemon=True)
                threads.append(t)
                t.start()
            except:
                print('threading error')
    else:
        print("Usage: subzero.py -d [domain]")
        
        
    while True:
        if count < wordlist_size: pass
        else:
            if args['output']:
                for i in log: logfile.write(i)
            print('\r\n')
            break