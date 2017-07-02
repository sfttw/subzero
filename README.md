Subzero
======

Subzero is a very-fast python wordlist-based DNS subdomain scanner.

Usage
-----

dnscan.py -d \<domain\> -o \<output\> [OPTIONS]

#### Mandatory Arguments
	-d  --domain                              Target domain

#### Optional Arguments
	-w --wordlist <wordlist>                  Wordlist of subdomains to use
	-t --threadcount                          Threads (1-100), default=100
	-o --output                               Output to a text file
	-v --verbose                              Verbose output
	-h --help                                 Display help text

Wordlists
---------

A number of wordlists are supplied with Subzero, courtesy of dnscan.

The first four (**subdomains-100.txt**, **subdomains-500.txt**, **subdomains-1000.txt** and **subdomains-10000.txt**) were created by analysing the most commonly occuring subomdains in approximately 86,000 zone files that were transferred as part of a separate research project. These wordlists are sorted by the popularity of the subdomains (more strictly by the percentage of zones that contained them in the dataset).

The **subdomain-uk-500.txt** and **subdomain-uk-1000.txt** lists are created using the same methodology, but from a set of approximately 180,000 zone transfers from ".uk" domains.

The final (and default) wordlist (**subdomains.txt**) is based on the top 10000 subdomains by popularity and the top 10000 UK subdomains, but has had a number of manual additions made based on domains identified during testing.

This list is sorted alphabetically and currently contains approximately **10443** entries.

# Requirements: 

pip install dns



# certscan.py
certscan is a fork of subd. It's a subdomain discovery tool that utilizes Certificate Search, Threat Crowd, and VirusTotal to fetch subdomains for a target within a few seconds. It's meant to be used to get quick results and not a complete replacement for subdomain enumerating.

## Requirements
- VirusTotal API Key (`vt_api_key = 'INSERT API KEY HERE'`).
- BeautifulSoup4 `pip3 install beautifulsoup4`
- aiohttp `pip3 install aiohttp`

## Usage
	python3 certscan.py domain.com
	
	

# Acknowledgements 

Thanks to these projects:

[@rbsec](http://github.com/rbsec/dnscan) - parts of the README and the subdomains are from here

[@haccer](https://github.com/haccer/subd/blob/0c4f1c7880cbd3b2d74d046971f042cfc4a12781/subd.py) - I incorporated parts of subd