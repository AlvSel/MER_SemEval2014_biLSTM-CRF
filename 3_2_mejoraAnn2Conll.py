#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob

def help():
	sys.stderr.write("""
	PRE:
		1 - Path con archivos ".ann" y ".conll"
		*   Necesario python 3.6 para glob
	POST: check if exist repeated lines
		 \n""")

if __name__ == "__main__":
	if(len(sys.argv) == 2):
		filesPath = sys.argv[1] # Path con archivos .ann

		for f_ann in glob.iglob(filesPath+"/**/*.ann", recursive=True):
			problemas = []
			with open(f_ann) as fa:
				ann =fa.read().splitlines()

			prevOff = 0
			for a in ann:
				curOff=int(a.split('\t')[1].split()[1])
				if(curOff == prevOff+1):
					problemas.append(curOff)

				prevOff = int(a.split('\t')[1].split()[-1])

			if(len(problemas)>0):
				f_con = f_ann[:-3]+"conll"
				with open(f_con) as fc:
					text =fc.read().splitlines()

				for l in range(0, len(text)):
					line = text[l]
					if('-DOCSTART-' not in line and len(line)>0):
						off = int(line.split()[2])
						if(off in problemas):
							text[l] = " ".join(line.split()[:-1])+' B-DISORDER'
						elif(off > problemas[-1]):
							break
				with open(f_con, 'w') as fc:
					fc.write("\n".join(text))
	else:
		help()
