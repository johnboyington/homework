#!/bin/bash

numOfFilesReg="$(ls -1 | wc -l)"
numOfFilesTot="$(ls -1a | wc -l)"
echo The number of regular files and folders in the current directory are $numOfFilesReg.
echo The total number of files and folders in the current directory are $numOfFilesTot, including ., .., and other hidden items.
