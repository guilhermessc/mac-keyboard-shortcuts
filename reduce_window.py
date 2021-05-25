#!/usr/bin/env python3

import os
import random
from utils import *

layout = get_layout_type()

if 'bsp' not in layout:
	a = os.system('yabai -m window --grid 120:120:%d:%d:60:90' % (random.randrange(60), random.randrange(30)))
