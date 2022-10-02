import bpy
import json

RED=0
GREEN=0
BLUE=0
ALPHA=1

texture_name = bpy.data.filepath.split('\\')[-1].split('.')[0]
data = json.loads(open('base_color.json').read())

colors = data[texture_name]
print(colors)
RED = colors['red']
GREEN = colors['green']
BLUE = colors['blue']
ALPHA = colors['alpha']

material = bpy.data.materials['Placeholder_Material']
pri = material.node_tree.nodes['Principled BSDF']
pri.inputs[0].default_value = (RED,GREEN,BLUE,ALPHA)
