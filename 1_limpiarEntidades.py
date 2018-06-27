#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob

def help():
	sys.stderr.write("""
	PRE:
		1 - Path con archivos ".pipe" y ".text"
		*   Necesario python 3.6 para glob
	POST: Sustituir en los TEXT los puntos y saltos de linea por espacio entre entidades para que las anote bien ann2conll"
		 \n""")

if __name__ == "__main__":
	if(len(sys.argv) == 2):
		filesPath = sys.argv[1] # Path con archivos .ann

		for f_ann in glob.iglob(filesPath+"/**/*.pipe", recursive=True):
			problemas = []
			with open(f_ann) as fa:
				ann =fa.read().splitlines()

			f_t = f_ann[:-4]+"text"
			with open(f_t) as fc:
				text = list(fc.read())

			for a in ann:
				a=a.split('||')
				if(len(a)==5):
					i1 = int(a[3])
					i2 = int(a[4])
					if("\n" in text[i1:i2]):
						aux = list("".join(text[i1:i2]).replace("\n"," "))
						text[i1:i2] = aux
					if("." in text[i1:i2]):
						aux = list("".join(text[i1:i2]).replace("."," "))
						text[i1:i2] = aux

			with open(f_t, 'w') as fc:
				fc.write("".join(text))
	else:
		help()
