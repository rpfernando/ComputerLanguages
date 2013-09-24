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

	states = automata['s'].closure
	initial_index = 0
	match = False

	list_of_matches = []

	for i,simbol in enumerate(text):
		states = state_list_delta(states, simbol)

		if match and not automata['f'] in states:
			if initial_index == i:
				continue
			list_of_matches.append((initial_index, i, text[initial_index:i]))

		if automata['f'] in states:
			match = True
			if initial_index == i:
				continue
			list_of_matches.append((initial_index, i, text[initial_index:i]))

		if len(states) == 0:
			states = [automata['s']]
			initial_index = i+1
			match = False
	
	if match or automata['f'] in states:
		list_of_matches.append((initial_index, len(text), text[initial_index:len(text)]))

	return list_of_matches


text = " hola como estas no se si esto vaya a funcionar pero me da mucha curiosidad de q va a pasar ahora"
text = "aaa"
re = "a*"

#text = "en la web encuentras todo lo que necesitas como por ejemplo cuando buscas en www.google.com"
#re = "web,www"

for i,f,t in get_re_matches(re, text):
	print i, f, t

