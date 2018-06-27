#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob

# PRE: existe por cada pipe un text
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
			f_con = f_ann[:-3]+'conll'

			with open(f_ann) as fa:
				e_ann = len(fa.read().splitlines())
			with open(f_con) as fc:
				text = fc.read()
				e_con = text.count("B-DISORDER")

			if(e_con != e_ann):
				print("ENT CONLL: "+str(e_con)+" VS ENT ANN: "+str(e_ann))
				print("FALLO file "+str(f_ann))

	else:
		help()
