#!/bin/bash
# convierte "text" a "conll", SOLO ENTIDADES CONTINUAS.

if [ $# -ne 1 ]
then
  echo "PRE: Path con archivos '.text' y '.ann'"
  echo "POST: Convierte 'text' a 'conll', SOLO ENTIDADES CONTINUAS."
  exit 1
fi

PATH=$1
SCRIPT="./te/brat-fafac7008a397cb6632a01f66d3e4a04c3f9398a/tools/anntoconll.py"
for f in $(/usr/bin/find $PATH -name '*.text');do
    /usr/bin/python2.7 $SCRIPT $f;
done
