#!/usr/bin/env python3

import os
from utils import *

layout = get_layout_type()

if 'bsp' in layout:
	a = os.system('yabai -m space --rotate 90')
