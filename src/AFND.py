from Global import *
import ShuntingYard
from Thompson import *

def create_AFND(re):
	deltas = []

	initial_node = ShuntingYard.create_tree(ShuntingYard.to_rpn(re))

	s = State('s')
	f = State('f')
	automaton = {s.name: s, f.name: f}

	s.add_transition(initial_node, f);
	deltas.append((s,initial_node,f))

	while len(deltas) > 0:
		(origin, simbol, destination) = deltas.pop()
		if simbol.is_function:
			aux_deltas = Thompson.generic(origin, simbol, destination)
			for t in aux_deltas:
				deltas.insert(0, t)
		else:
			aux = origin.delete_transition(simbol)
			for a in aux:
				origin.add_transition(simbol.char, a)

	return automaton
		

#r = "(hola, hey) como (estas,te va)"
r = "(ab,c)*,(de+,fg*)+"
#r = "a"
automata = create_AFND(r)


print automata['s']
print automata['f'] in automata['s'].delta('a')

	
