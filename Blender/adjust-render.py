import argparse
import bpy

cParser = argparse.ArgumentParser('Blender Render Adjust Script')

cParser.add_argument('--resolution',
        type=int,
        help="Resolution of single frame",
        default=64)

args, _ = cParser.parse_known_args(['--', '-f'])

Scene = bpy.data.scenes["Scene"]
Scene.render.resolution_x = args.resolution
Scene.render.resolution_y = args.resolution
