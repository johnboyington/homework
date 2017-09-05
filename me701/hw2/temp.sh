#!/bin/bash

inputTemp=$1
fTemp=212

# inputTemp * (5/9)
cTemp=$(echo "scale=6;($fTemp-32)*(5/9)" | bc)

echo The temperature \in celcius is $cTemp.
