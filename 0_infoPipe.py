#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import glob

# PRE: existe por cada pipe un text
def help():
	sys.stderr.write("""
	PRE:
		1 - Path con archivos ".pipe"
		*   Necesario python 3.6 para glob
	POST: check if exist repeated lines
		 \n""")

if __name__ == "__main__":
	if(len(sys.argv) == 2):
		filesPath = sys.argv[1] # Path con archivos .pipe
		total = 0
		totalJoin, totalDis = 0,0
		totalOffDCUI, totalOffICUI = 0,0
		totalF = 0

		for filename_pipe in glob.iglob(filesPath+"/**/*.pipe", recursive=True):
			auxCUI = []
			auxSinCui = []
			with open(filename_pipe) as f:
				text = f.read().splitlines()
			total += len(text)
			for i,line in enumerate(text):
				line = line.split('||')
				if(len(line)>4):
					if(len(line)==5):
						totalJoin += 1
					else:
						totalDis += 1

					if(line in auxCUI):
						if(len(line)==5):
							print("CONTINUO")
						else:
							print("DISCONTINUO")
						totalOffICUI += 1
						print("IGUAL offset Y CUI, "+str(filename_pipe)+" line "+str(i))
					else:
						auxCUI.append(line)

					auxLine = line[:2]+line[3:]
					if(auxLine in auxSinCui):
						if(len(line)==5):
							print("CONTINUO")
						else:
							print("DISCONTINUO")
						totalOffDCUI += 1
						print("IGUAL offset Y distinto CUI, "+str(filename_pipe)+" line "+str(i))
					else:
						auxCUI.append(auxLine)

				else:
					totalF += 1
					print("ERROR, "+str(filename_pipe)+" line "+str(i))

		print("TOTAL "+str(total))
		print("N Join "+str(totalJoin))
		print("N Disjoin "+str(totalDis))
		print("N Offset igual y CUI igual "+str(totalOffICUI))
		print("N Offset igual y CUI distinto "+str(totalOffDCUI))
		print("N FAIL "+str(totalF))

	else:
		help()
