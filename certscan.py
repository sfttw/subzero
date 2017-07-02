#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
''' subdomain discovery using Certificate Search, Threat Crowd, and VirusTotal to fetch subdomains for a target within a few seconds. '''
import bs4, io, json, pycurl, queue, sys, threading
import argparse
__author__ = 'e7v'
__version__ = '0.1'
__url__='https://github.com/e7v/subzero/certscan'
__description__='''\
___________________________________________
certscan.py is subd fork. It's a subdomain discovery tool that utilizes Certificate Search, Threat Crowd, and VirusTotal to fetch subdomains for a target within a few seconds. It's meant to be used to get quick results and not a complete replacement for subdomain enumerating. 
Version: '''+__version__+'''
Author: '''+__author__+'''
Github: '''+__url__+'''
___________________________________________
'''
__epilog__='''
example:
  certscan.py domain.com
  '''

global url_list
global args
global vt_api_key
domain = 'example.com'
q = queue.Queue()
subdomains = []
__all__ = ['main']

def get_url(current_url):
    buffer = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, current_url)
    c.setopt(c.WRITEFUNCTION, buffer.write)
    c.perform()
    if 'https://crt.sh' in current_url:
        body = buffer.getvalue()
        soup = bs4.BeautifulSoup(body, "html.parser")
        for subs in soup.find_all('td',style=False,class_=False):
            sub = ''.join(subs.findAll(text=True))
            if domain in sub:
                if "*" not in sub:
                    subdomains.append(sub)
    else:
        body = json.loads(buffer.getvalue().decode('utf8'))
        try:
            subs = body["subdomains"]
            for sub in subs:
                subdomains.append(sub)
        except: pass

def get_subdomains():
    while True:
        current_url = q.get()
        get_url(current_url)
        q.task_done()

def main(domain='example.com', verbose=False):
    global subdomains
    global args
    try: 
        if args['verbose']:verbose = args['verbose']
    except: pass

    try: 
        if args['domain']: 
            domain = args['domain']
    except: pass
    vt_api_key = open('keys.txt').read().strip()
    url_list = [
                'https://crt.sh/?q=%25.{}'.format(domain),
                'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'.format(domain),
                'https://www.virustotal.com/vtapi/v2/domain/report?apikey={}&domain={}'.format(vt_api_key, domain)
                ]
    for i in range(3):
        t = threading.Thread(target=get_subdomains)
        t.daemon = True
        t.start()
    for current_url in url_list:
        q.put(current_url)
    q.join()
    subdomains = sorted(set([domain.lower() for domain in subdomains]))
    try:
        if verbose:
            for subdomain in subdomains:
                print(subdomain)
    except: pass   
    return subdomains
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__description__,
                                    prog='certscan',
                                    formatter_class=argparse.RawTextHelpFormatter,
                                    epilog=__epilog__)
    #parser.add_argument('-d','--domain', help='Domain', required=True)
    parser.add_argument('domain', help='target to scan, like example.com') 
    parser.add_argument('-v','--verbose', help='Verbose', required=False, action='store_true')

    args = vars(parser.parse_args())
    
    main()