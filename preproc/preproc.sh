
PATH_SRC=../src/
PATH_POS=../pos/
PATH_XML=../xml/

# POS tagging des phrases avec MElt
for FILE in $PATH_SRC/*.tokens
do
    BASENAME=`basename "$FILE"`
    OUTFILE=$PATH_POS/${BASENAME%.tokens}'.pos'
    echo "MElt -r < $FILE > $OUTFILE"
    MElt -r < $FILE > $OUTFILE
done

# Conversion des phrases étiquetées en POS vers le format XML
for FILE in $PATH_POS/*.pos
do
    BASENAME=`basename "$FILE"`
    OUTFILE=$PATH_XML/${BASENAME%.pos}'.xml'
    echo "python preproc.py $FILE $OUTFILE"
    python preproc.py $FILE $OUTFILE
done