#!/bin/sh

for elt in `ls *.ui`
do
    dest=$(echo $elt | sed s/"ui"/"py"/g)
    pyuic5 -x $elt -o ../lib/$dest
    pyrcc5 ../images/res.qrc -o ../res_rc.py
done
