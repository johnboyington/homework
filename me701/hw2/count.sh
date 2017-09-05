#!/bin/bash

# uses ls to list the files in the current directory, then wc (word count, I
# assume) to count the number of new lines listed.
numOfFilesReg="$(ls -1 | wc -l)"
numOfFilesTot="$(ls -1a | wc -l)"

# print something meaningful regarding the numbers calculated
echo The number of regular files and folders in the current directory are $numOfFilesReg.
echo The total number of files and folders in the current directory are $numOfFilesTot, including ., .., and other hidden items.
