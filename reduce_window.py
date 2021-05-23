#!/usr/bin/env python3

import os
import random

filename = r'/Users/gssc/.config/skhd/tmp.txt'


os.system("yabai -m query --spaces --display | jq 'map(select(.\"focused\" == 1))' | jq '.[0].type' > %s" % filename)
layout = open(filename).read()
os.system('rm %s' % filename)

if 'bsp' not in layout:
	a = os.system('yabai -m window --grid 120:120:%d:%d:60:90' % (random.randrange(60), random.randrange(30)))
