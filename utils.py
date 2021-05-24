import os
import ast
import random

filename = r'/Users/gssc/.config/skhd/tmp.txt'

def get_layout_type():
	os.system("yabai -m query --spaces --display | jq 'map(select(.\"focused\" == 1))' | jq '.[0].type' > %s" % filename)
	layout = open(filename).read().strip()
	os.system('rm %s' % filename)
	return layout

def get_current_frame():
	os.system("yabai -m query --windows | jq 'map(select(.\"focused\" == 1))[0].\"frame\"' > %s" % filename)
	current_frame = open(filename)
	os.system('rm %s' % filename)
	tmp=''
	for i in current_frame:
		tmp+=i.strip()
	current_frame = ast.literal_eval(tmp)
	return current_frame

def get_display_id():
	os.system("yabai -m query --windows | jq 'map(select(.\"focused\" == 1))[0].\"display\"' > %s" % filename)
	display = open(filename).read()
	os.system('rm %s' % filename)
	display_id = int(display.strip())
	return display_id

def get_display_frame(display_id=None):

	if display_id is None:
		display_id = get_display_id()	

	os.system("yabai -m query --displays | jq 'map(select(.\"id\" == %d))[0].\"frame\"' > %s" % (display_id, filename))
	display_frame = open(filename)
	os.system('rm %s' % filename)
	tmp=''
	for i in display_frame:
		tmp+=i.strip()
	display_frame = ast.literal_eval(tmp)
	return display_frame

positions = {0:'no_pos', 1:'bottom-left', 2:'bottom', 3:'bottom-right', 
			 4:'left', 44:'2-3-left', 444:'1-3-left',
			 6:'right', 66:'2-3-right', 666:'1-3-right',
			 7:'top-left', 8:'top', 9:'top-right'}

def _is_pos_right(rel_frame):
	if rel_frame['x'] - 0.5 > -0.1:
		if rel_frame['y'] < 0.1:
			if rel_frame['h'] > 0.8:
				if abs(rel_frame['w'] - 0.5) < 0.1:
					return True
	return False

def _is_pos_right_1_3(rel_frame):
	if abs(rel_frame['x'] - 0.66) < 0.1:
		if rel_frame['y'] < 0.1:
			if rel_frame['h'] > 0.8:
				if abs(rel_frame['w'] - 0.33) < 0.1:
					return True
	return False

def _is_pos_right_2_3(rel_frame):
	if abs(rel_frame['x'] - 0.33) < 0.1:
		if rel_frame['y'] < 0.1:
			if rel_frame['h'] > 0.8:
				if abs(rel_frame['w'] - 0.66) < 0.1:
					return True
	return False


def _is_pos_left(rel_frame):
	if rel_frame['x'] < 0.1:
		if rel_frame['y'] < 0.1:
			if rel_frame['h'] > 0.8:
				if abs(rel_frame['w'] - 0.5) < 0.1:
					return True
	return False

def _is_pos_left_1_3(rel_frame):
	if rel_frame['x'] < 0.1:
		if rel_frame['y'] < 0.1:
			if rel_frame['h'] > 0.8:
				if abs(rel_frame['w'] - 0.33) < 0.1:
					return True
	return False

def _is_pos_left_2_3(rel_frame):
	if rel_frame['x'] < 0.1:
		if rel_frame['y'] < 0.1:
			if rel_frame['h'] > 0.8:
				if abs(rel_frame['w'] - 0.66) < 0.1:
					return True
	return False



def get_rel_frame(display_frame=None, current_frame=None):
	if display_frame is None:
		display_frame = get_display_frame()

	if current_frame is None:
		current_frame = get_current_frame()

	rel_frame = {}
	rel_frame['x'] = float(current_frame['x']-display_frame['x']) / display_frame['w']
	rel_frame['w'] = float(current_frame['w']) / display_frame['w']
	rel_frame['y'] = float(current_frame['y']-display_frame['y']) / display_frame['h']
	rel_frame['h'] = float(current_frame['h']) / display_frame['h']

	return rel_frame

def get_frame_position(display_frame=None, current_frame=None):
	
	rel_frame = get_rel_frame(display_frame, current_frame)

	if _is_pos_right(rel_frame):
		return positions[6]

	if _is_pos_right_2_3(rel_frame):
		return positions[66]

	if _is_pos_right_1_3(rel_frame):
		return positions[666]


	if _is_pos_left(rel_frame):
		return positions[4]

	if _is_pos_left_2_3(rel_frame):
		return positions[44]

	if _is_pos_left_1_3(rel_frame):
		return positions[444]



	return positions[0]



