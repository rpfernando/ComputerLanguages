from AFND import *
from Global import *

def define_index(initial, final, lenght, diference):
	if initial - diference < 0:
		initial = 0
	else:
		initial -= diference

	if final + diference >= lenght:
		final  = lenght
	else:
		final += diference
	return (initial, final)

def get_re_matches(re, text):
	automata = create_AFND(re)

	states = []
	#initial_index = 0
	match = False

	list_of_matches = []

	for index in range(len(text)):
		initial_index = index
		final = index
		states = automata['s'].closure
		while len(states) > 0:
			if final == len(text):
				break
			states = state_list_delta(states, text[final])
			final += 1
			if automata['f'] in states:
				list_of_matches.append((initial_index, final, text[initial_index:final]))
		
	return list_of_matches
