from Global import *
import ShuntingYard
from Thompson import *

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
	#automaton = {s.name: s}

	s.add_transition(initial_node, f);
	deltas.append((s,initial_node))

	while len(deltas) > 0:
		(origin, simbol) = deltas.pop()
		
		if not origin in automaton.values():
			automaton.setdefault(origin.name, origin)

		if isinstance(simbol, ShuntingYard.Node):
			aux_deltas = Thompson.generic(origin, simbol)
			for t in aux_deltas:
				deltas.insert(0, t)

	for state_name in automaton:
		automaton[state_name].update_closure()

	return automaton
