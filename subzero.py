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
import threading


log = []

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
    global count
    while len(wordlist) > 0:
        target = wordlist.pop() + '.' + domain
        check(target)
        count += 1
        print('\r {} / {}'.format(count, wordlist_size), end='')
        #print('\r {}'.format(target), end='')


    
    
if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Subzero - subdomain bruteforcer')
    parser.add_argument('-d','--domain', help='Domain', required=True)
    parser.add_argument('-w','--wordlist', help='Wordlist', default='names.txt', required=False)
    parser.add_argument('-v','--verbose', help='Verbose', required=False, action='store_true')
    parser.add_argument('-o','--output', help='Output file', required=True, default='log.txt')
    args = vars(parser.parse_args())

    if args['domain']:
        wordlist = open(args['wordlist'], 'r').readlines()
        wordlist = [i.strip() for i in wordlist]
        wordlist.reverse()
        wordlist_size = len(wordlist)
        domain = args['domain']
        count = 0
        logfile = args['output']
        logfile = open(logfile,'a')

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
        
    