#!/bin/bash

declare filename='input_'
declare FileEND=99
declare EXT='.txt'


for G in $(seq 0 $FileEND);
do
echo 'Submitting' $filename
casmo4 $filename$G$EXT
done

