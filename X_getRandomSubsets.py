#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob
import numpy as np
from random import shuffle

def help():
	sys.stderr.write("""
	PRE:
		1 - Path con archivos ".conll"
		2 - OutPath
		*   Necesario python 3.6 para glob
	POST: extraer subconjuntos\n""")

if __name__ == "__main__":
	if(len(sys.argv) == 3):
		filesPath = sys.argv[1] # Path con archivos .conll
		outPath = sys.argv[2]
		trainSize = 100
		devSize  = 25
		testSize = 25
		paths = []
		pathTrain, pathDev, pathTest = [], [], []

		for filename_conll in glob.iglob(filesPath+"/**/*.conll", recursive=True):
			paths.append(filename_conll)

		randomPaths = np.random.choice(paths, trainSize+devSize+testSize, replace=False)
		shuffle(randomPaths)

		pathTrain = randomPaths[:trainSize]
		pathDev = randomPaths[trainSize:trainSize+devSize]
		pathTest = randomPaths[trainSize+devSize:]

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

		with open(outPath+'/SemEval_test.conll', 'w') as ftest:
			for f in pathTest:
				with(open(f)) as ftext:
					text = ftext.read()
					ftest.write(text+'\n')
	else:
		help()
