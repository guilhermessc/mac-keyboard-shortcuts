#!/usr/bin/env python3

from utils import *
import os

layout = get_layout_type()

if 'bsp' in layout:
	a = os.system('yabai -m space --layout float')


# state machine
pos = get_frame_position()
# states are the positions half, 1/3, 2/3, other

if pos == positions[4]: # left
	os.system('yabai -m window --grid 1:3:0:0:2:1')

elif pos == positions[44]: # left 2/3
	os.system('yabai -m window --grid 1:3:0:0:1:1')

elif pos == positions[444]: # left 1/3
	os.system('yabai -m window --grid 1:2:0:0:1:1')
	os.system('yabai -m window --display prev')

else:
	os.system('yabai -m window --grid 1:2:0:0:1:1')


# if none -> half
# if half -> 2/3
# if 2/3 -> 1/3
# if 1/3 -> half and next display
