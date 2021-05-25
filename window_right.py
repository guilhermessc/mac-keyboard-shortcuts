#!/usr/bin/env python3

from utils import *
import os

layout = get_layout_type()

if 'bsp' in layout:
	a = os.system('yabai -m space --layout float')

pos = get_frame_position()

if pos == positions[6]: # right
	os.system('yabai -m window --grid 1:3:1:0:2:1')
elif pos == positions[66]: # right 2/3
	os.system('yabai -m window --grid 1:3:2:0:1:1')
elif pos == positions[666]: # right 1/3
	os.system('yabai -m window --grid 1:2:1:0:1:1')
	os.system('yabai -m window --display next')
else:
	os.system('yabai -m window --grid 1:2:1:0:1:1')
