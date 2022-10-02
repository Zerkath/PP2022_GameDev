#!/bin/bash

# Disabled texture selection script
# blender.exe $1.blend -b -o "//$1/###_render" -P ./select_texture.py -a 
blender.exe $1.blend -b -o "//$1/###_render" -a
montage -background none -geometry 1024x1024 $1/*_render.png $1/$1.png

