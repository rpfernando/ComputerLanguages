from AFND import *
from Global import *

def state_list_delta(list_of_states, simbol):
	list_to_return = []

	for state in list_of_states:	
		aux = state.extended_delta(simbol)
		for s in aux:
			if not s in list_to_return:
				list_to_return.append(s)

	return list_to_return

def get_re_matches(atomaton, text):
	automata = atomaton

	states = []
	#initial_index = 0
	match = False

	list_of_matches = []

	automata['s'].index = [0]
	states = automata['s'].extended_delta(Global.epsilon)

	for index in range(len(text)):
		states = state_list_delta(states, text[index])
		automata['s'].index = [index+1]
		states.append(automata['s'])
		if automata['f'] in states: 
			for i in automata['f'].index:
				list_of_matches.append((i, index+1, text[i:index+1]))
		for s in states:
			print s,
		print 
		
	return list_of_matches
