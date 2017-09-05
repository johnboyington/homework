#!/bin/bash

# input temperature as cmd line flag
inputTemp=$1

# (inputTemp-32) * (5/9)
cTemp=$(echo "scale=6;($inputTemp-32)*(5/9)" | bc)

# cTemp + 273.15
kTemp=$(echo "scale=6;($cTemp+273.15)" | bc)

# output information
echo The temperature \in celcius is $cTemp.
echo The temperature \in kelvin is $kTemp.
