#!usr/bin/bash
# Author = 'Eva Linehan (eva.linehan18@imperial.ac.uk)'
# Version = 0.01
# Date = 'Nov 2018'
# Desc: 'Script to call, profile and print results of LV1.py and LV2.py while comparing speeds.'


echo "Run and profile LV1.py"
python3 -m cProfile LV1.py 2>&1 | head -10

echo "Run and profile LV2.py"
python3 -m cProfile LV2.py 2>&1 | head -10

echo "Run and profile LV3.py"
python3 -m cProfile LV3.py 2>&1 | head -10

echo "Run and profile LV4.py"
python3 -m cProfile LV4.py 2>&1 | head -10