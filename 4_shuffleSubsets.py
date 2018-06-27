#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob
from random import shuffle

def help():
	sys.stderr.write("""
	PRE:
		1 - Path con archivos Train ".conll"
		2 - Path con archivos Dev ".conll"
		3 - OutPath
		*   Necesario python 3.6 para glob
	POST: extraer subconjuntos\n""")

if __name__ == "__main__":
	if(len(sys.argv) == 4):
		filesPathTrain = sys.argv[1] # Path con archivos TRAIN .conll
		filesPathDev = sys.argv[2] # Path con archivos DEV .conll
		outPath = sys.argv[3]
		pathTrain, pathDev = [], []

		pathTrain = list(glob.iglob(filesPathTrain+"/**/*.conll", recursive=True))
		pathDev   = list(glob.iglob(filesPathDev+"/**/*.conll", recursive=True))

		shuffle(pathTrain)
		shuffle(pathDev)

		with open(outPath+'/SemEval_train.conll', 'w') as ftrain:
			for f in pathTrain:
				with(open(f)) as ftext:
					text = ftext.read()
					ftrain.write(text+'\n')

		with open(outPath+'/SemEval_dev.conll', 'w') as fdev:
			for f in pathDev:
				with(open(f)) as ftext:
					text = ftext.read()
					fdev.write(text+'\n')
	else:
		help()
