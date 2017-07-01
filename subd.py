#!/usr/bin/env python3
import bs4, io, json, pycurl, queue, sys, threading

domain = sys.argv[1]
vt_api_key = 'ef3449d0cbfe7f0da2af4585956dc4e127e06f62c2b6d88a5aaaec5ef9cdcac5'
url_list = [
            'https://crt.sh/?q=%25.{}'.format(domain),
            'https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={}'.format(domain),
            'https://www.virustotal.com/vtapi/v2/domain/report?apikey={}&domain={}'.format(vt_api_key, domain)
            ]

q = queue.Queue()
subdomains = []

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

if __name__ == "__main__":
    for i in range(3):
        t = threading.Thread(target=get_subdomains)
        t.daemon = True
        t.start()
    for current_url in url_list:
        q.put(current_url)
    q.join()
    subdomains = sorted(set([domain.lower() for domain in subdomains]))
    for subdomain in subdomains:
        print(subdomain)
