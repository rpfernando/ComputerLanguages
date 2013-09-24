from Global import *
import ShuntingYard
from Thompson import *

def state_list_delta(list_of_states, simbol):
	list_to_return = []

	for state in list_of_states:	
		aux = state.extended_delta(simbol)
		for s in aux:
			if not s in list_to_return:
				list_to_return.append(s)

	return list_to_return

def check_string(automaton, word):
	inicial = automata['s'].closure
	for i in word:
		inicial = state_list_delta(inicial, i)
	return automaton['f'] in inicial

def create_AFND(re):
	deltas = []

	initial_node = ShuntingYard.create_tree(ShuntingYard.to_rpn(re))

	s = State('s')
	f = State('f')
	automaton = {s.name: s, f.name: f}

	s.add_transition(initial_node, f);
	deltas.append((s,initial_node))

	while len(deltas) > 0:
		(origin, simbol) = deltas.pop()
		
		if not origin in automaton.values():
			automaton.setdefault(origin.name, origin)

		if simbol.is_function:
			aux_deltas = Thompson.generic(origin, simbol)
			for t in aux_deltas:
				deltas.insert(0, t)
		else:
			aux = origin.delete_transition(simbol)
			for a in aux:
				origin.add_transition(simbol.char, a)
				#Descomentar la siguiente linea de codigo permite ver todas las transiciones generadas
				#print origin, "--" + str(simbol.char) + "-->", a
				#print origin, simbol, a

	for state in automaton:
		automaton[state].update_closure()

	return automaton
		
"""
r = "2*((01)*(0,&),(10)*(1,&))"
#r = "(ab,c)*,(de+,fg*)+"
#r = "a(b*)(c(d))"
#r = "(a*)+**"
automata = create_AFND(r)

print check_string(automata, "	")
"""
