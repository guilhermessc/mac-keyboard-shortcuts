#!/usr/bin/env python3

import os


filename = r'/Users/gssc/.config/skhd/tmp.txt'


os.system("yabai -m query --spaces --display | jq 'map(select(.\"focused\" == 1))' | jq '.[0].type' > %s" % filename)
layout = open(filename).read()
os.system('rm %s' % filename)

if 'bsp' in layout:
	a = os.system('yabai -m space --layout float')
else:
	a = os.system('yabai -m space --layout bsp')
