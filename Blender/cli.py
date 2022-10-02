import os
import argparse
import subprocess
import sys
import re 
absRoot = os.path.dirname(os.path.realpath(__file__))
os.chdir(absRoot)
cParser = argparse.ArgumentParser('Video Render Selection Tool')

cParser.add_argument('--list',
        nargs="+",
        type=str,
        help="Filenames to match",
        default=None)

cParser.add_argument('--resolution',
        type=int,
        help="Resolution of single frame",
        default=512)

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

subprocess.run(["pwd"], cwd=absRoot)

confirm = input(f"Do you want to render the following files: \n{selectedFiles} (y/n)\n")
if confirm.lower() == 'y':
    res = args.resolution
    adjustRenderArgs = f"--resolution {res}"
    print(f"Passing following args to blender python script: {adjustRenderArgs}")
    for file in selectedFiles:
        renderResultDir = file[0:-6]
        subprocess.run([
            "blender.exe",
            f"./{file}",
            "-b",
            "-o",
            f"//{renderResultDir}/###_render", # // is not a typo this is blender relative path
            "-P",
            "./adjust-render.py",
            "-a", "--", adjustRenderArgs
        ], cwd=absRoot),
        subprocess.run([
            "montage",
            "-background",
            "none",
            "-geometry",
            f"{res}x{res}",
            f"./{renderResultDir}/*_render.png",
            f"./{renderResultDir}/{renderResultDir}.png"
        ], cwd=absRoot)

