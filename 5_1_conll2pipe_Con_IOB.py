#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob

def help():
	sys.stderr.write("""
	PRE:
		1 - Archivo ".output"
		2 - OutPath
		* CUIDADO, hace append de los archivos asi que si existen no los sobreescribe y los concatena.
	POST: extrae del .output cada .pipePred
		 \n""")

if __name__ == "__main__":
	if(len(sys.argv) == 3):
		outputFile	= sys.argv[1]
		outPath		= sys.argv[2]
		colCons		= "Disease_Disorder"
		cui         = "None"

		with open(outputFile) as fT:
		    originalText = fT.read().splitlines()

		startOffset = -1
		endOffset = -1

		for i in range(0, len(originalText)):
			line = originalText[i]
			line = line.split()
			# Archivo nuevo
			if(line[-3:] == ['0', 'O', 'O']):
				#Compruebo si se ha quedado por escribir algo
				if(startOffset>0 and endOffset>0):
					lineOut = [fileName, colCons, cui, str(startOffset), str(endOffset)]
					with open(outPath+'/'+outFile, 'a') as fout:
						fout.write("||".join(lineOut)+'\n')
					startOffset = -1
					endOffset = -1

				name1 = line[0]
				#tiene que tener 6 digitos, ceros por la izquierda
				for j in range(len(name1), 6):
					name1 = '0' + name1

				i+=1;
				while(originalText[i].split()[0] == '|'):
					i+=1
				name2 = originalText[i].split()[0]
				for j in range(len(name2), 5):
					name2 = '0' + name2

				i+=1;
				while(originalText[i].split()[0] == '|'):
					i+=1
				i+=1
				while(originalText[i].split()[0] == '|'):
					i+=1
				typeReport = originalText[i].split()[0]
				i+=1
				typeReport += originalText[i].split()[0]
				i+=1
				typeReport += originalText[i].split()[0]

				fileName = name2+'-'+name1+'-'+typeReport+'.txt'
				outFile  = name2+'-'+name1+'.pipePred'

			elif(line[-1:] == ['B-DISORDER']):
				# existe ya un B-DISORDER?
				if(startOffset>0 and endOffset>0):
					lineOut = [fileName, colCons, cui, str(startOffset), str(endOffset)]
					with open(outPath+'/'+outFile, 'a') as fout:
						fout.write("||".join(lineOut)+'\n')

				startOffset = int(line[2])
				endOffset = int(line[1])

			elif(line[-1:] == ['I-DISORDER']):
				endOffset = int(line[1])

		if(startOffset>0 and endOffset>0):
			lineOut = [fileName, colCons, cui, str(startOffset), str(endOffset)]
			with open(outPath+'/'+outFile, 'a') as fout:
				fout.write("||".join(lineOut)+'\n')
	else:
		help()
