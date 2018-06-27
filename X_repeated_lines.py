#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob

def help():
	sys.stderr.write("""
	PRE:
		1 - Path con archivos
		2 - File extension
		*   Necesario python 3.6 para glob
	POST: check if exist repeated lines (recursive)
		 \n""")

if __name__ == "__main__":
	if(len(sys.argv) == 3):
		filesPath = sys.argv[1] # Path con archivos
		fileExten = sys.argv[2]

		for f in glob.iglob(filesPath+"/**/*."+str(fileExten), recursive=True):
			with open(f) as fi:
				text = fi.read().splitlines()

			lines = []
			for l in text:
				if l in lines:
					print(l)
				else:
					lines.append(l)
	else:
		help()
