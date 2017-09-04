#!/usr/bin/env python3
import argparse
import subprocess
import os
if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='tlds', formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('domain', help='target to scan, like domain.com')
	args = vars(parser.parse_args())
	tlds = open('tlds.txt').readlines()
	
	completed = os.listdir('logs')
	for tld in tlds:
		target = '{}{}'.format(args['domain'].strip(),tld.strip())
		print('TARGET: {}'.format(target))
		if target+'.txt' not in completed:
			subprocess.check_call('subzero {}{}'.format(args['domain'],tld),shell=True)
		else: 
			print('logfile "{}" exists for target. delete logfile and retry.'.format(target))
