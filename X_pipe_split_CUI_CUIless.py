#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob
from os.path import basename

# PRE: existe por cada pipe un text
def help():
	sys.stderr.write("""
	PRE:
		1 - Path con archivos ".pipe"
		2 - OutPath
		*   Necesario python 3.6 para glob
	POST: dividir las entidades CUI y CUI-less en dos archivos
		 \n""")

if __name__ == "__main__":
	if(len(sys.argv) == 3):
		filesPath = sys.argv[1] # Path con archivos .pipe
		outPath   = sys.argv[2] # Path guardar output

		for filename_pipe in glob.iglob(filesPath+"/**/*.pipe", recursive=True):
			cuiList 	= []
			cuilessList = []
			filename 	= basename(filename_pipe)

			with open(filename_pipe) as f:
				text = f.read().splitlines()

			for i,line in enumerate(text):
				lineSplit = line.split('||')
				cui  = lineSplit[2]

				if cui.lower() == 'CUI-less'.lower():
					with open(outPath+'/'+filename+'.cuiless', 'a') as fo:
						fo.write(line+'\n')
				else:
					with open(outPath+'/'+filename+'.cui', 'a') as fo:
						fo.write(line+'\n')
	else:
		help()
