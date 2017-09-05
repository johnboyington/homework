#!/bin/bash

# create trash folder in home directory and output appropriate message
(((mkdir ~/trash) 2> /dev/null) && echo trash folder created in home directory) || echo trash folder already exists in home directory

# take in input filename
fileToDelete=$1

# move file to trash if it exist and output appropriate message
(((mv $fileToDelete ~/trash) 2> /dev/null) && echo $fileToDelete moved to trash folder) || echo $fileToDelete does not exist in current directory
