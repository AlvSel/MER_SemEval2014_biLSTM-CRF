#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob

# PRE: existe por cada pipe un text
def help():
	sys.stderr.write("""
	PRE:
		1 - Path con archivos ".pipe" y ".text"
		*   Necesario python 3.6 para glob
	POST: convierte "pipe" a "ann", SOLO ENTIDADES CONTINUAS, en el path de los pipes y text:
	    "pipe: 00381-006281-DISCHARGE_SUMMARY.txt||Disease_Disorder||C0000737||344||358"
		"ann:  T1\tDISORDER 344 358\tAbdominal pain"
		 \n""")

if __name__ == "__main__":
	if(len(sys.argv) == 2):
		filesPath		= sys.argv[1] # Path con archivos .pipe

		for filename_pipe in glob.iglob(filesPath+"/**/*.pipe", recursive=True):
			filename_text = filename_pipe[:-4]+"text"
			outFile = filename_pipe[:-4]+"ann"

			offsetAux = [] #para no add offset iguales

			tag         = 'DISORDER'
			text        = ""
			ident       = 1

			with open(filename_text) as fT:
			    originalText = fT.read()

			with open(filename_pipe) as fP:
			    pipes = fP.read().splitlines()
			lPipes = [p.split("||")[3:] for p in pipes]

			for i, pipe in enumerate(lPipes):
				# SOLO entidades CONTINUAS
				if(len(pipe) == 2):
					if([pipe[0], pipe[1]] in offsetAux):
						print("ERROR duplicated offset in "+ str(filename_pipe) +" line "+ str(i))
					else:
						aux = "T"+str(ident)+"\t"+tag+" "+pipe[0]+" "+pipe[1]
						entity = originalText[int(pipe[0]):int(pipe[1])]
						entity = entity.replace("\n", " ")
						aux += "\t"+entity+"\n"
						text += aux
						ident += 1
						offsetAux.append([pipe[0], pipe[1]])

			with open(outFile, 'w') as fO:
				fO.write(text)

	else:
		help()
