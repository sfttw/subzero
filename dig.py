#!/usr/bin/env python3
__description__ = 'Return A and CNAME records.'

import dns.resolver
import argparse
global args

def check(target, showTarget=False, verbose=True):
	log = []
	try: 
		showTarget = args['showTarget']
		verbose = args['verbose']
	except: pass
	myResolver = dns.resolver.Resolver() 
	try:
		myAnswers = myResolver.query(target, "A") 
		for rdata in myAnswers: 
			if showTarget: 
				answer = target + ' ' + rdata.to_text()
				if verbose: print('\r'+answer+'\n',end='')
				log.append(answer)
			else: 
				answer = rdata.to_text() 
				log.append(answer)
			
	except:
		pass
	try:
		myAnswers = myResolver.query(target, "CNAME") 
		for rdata in myAnswers: 
			if showTarget: 
				answer = target + ' ' + rdata.to_text()
				if verbose: print('\r'+answer+'\n',end='')
			else: 
				answer = rdata.to_text() 
			log.append(answer)
	except: 
		pass
	try:
		if args['verbose']: 
			for i in log:
				print(i)
	except: pass
	return log 
		
if __name__ == "__main__": 
	parser = argparse.ArgumentParser(description=__description__,
									prog='dig',
									formatter_class=argparse.RawTextHelpFormatter)
	#parser.add_argument('-d','--domain', help='Domain', required=True)
	parser.add_argument('domain', help='target to scan, like domain.com')
	parser.add_argument('-v','--verbose', help='Verbose', required=False, action='store_true', default=True)
	parser.add_argument('-s','--showTarget', help='show target', required=False, action='store_true', default=False)

	args = vars(parser.parse_args())
	check(args['domain'], args['showTarget'])