import os
import argparse
import sys
import re 

cParser = argparse.ArgumentParser('Video Render Selection Tool')

cParser.add_argument('--list',
        nargs="+",
        type=str,
        help="Filenames to match",
        default=None)

args = cParser.parse_args()

searchFiles = set()
existingFiles = set(os.listdir('.'))
notValidFiles = set()
selectedFiles = set()

# if list is empty select all 
if args.list is None:
    searchFiles = existingFiles 
else:
    searchFiles = args.list

blenderRegex = ".*\\.blend$"
for file in searchFiles:
    if re.search(blenderRegex, file) is None or file not in existingFiles: 
        notValidFiles.add(file)
    else:
        selectedFiles.add(file)

print(f"The following files did not exist or were not valid: \n{notValidFiles}\n")
confirm = input(f"Do you want to render the following files: \n{selectedFiles} (y/n)\n")
if confirm is 'y':
    for file in selectedFiles:
        os.system(f"./render-animation.sh {file[0:-6]}")
