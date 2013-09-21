from Global import *
import ShuntingYard
from collections import defaultdict

def create_AFND(re):
	initial_node = ShuntingYard.create_tree(ShuntingYard.to_rpn(re))
	automaton = set()
	s = State('s')
	f = State('f')
	s.add_transition(initial_node, f);
	automaton.add(s)
	automaton.add(f)

 
class State:

	#Counts the number of states created and also allows you to name a state automaticaly.
	id = 0 

	def __init__(self, name=None):
		if name != None:
			self.name = name
		else:
			self.name = str(State.id)
			State.id += 1
		self.closure = set()
		self.add_to_closure(self)
		self.transitions = dict() 

	#Instead of adding an epsilon transition add it to the closure.
	def add_to_closure(self, state):
		self.closure.add(state)

	def add_transition(self, simbol, destination):
		try:
			self.transitions[simbol].append(destination)
		except Exception, e:
			self.transitions.setdefault(simbol, []).append(destination)

	def __str__(self):
		return "State: " + self.name + "."


#r = "(hola, hey) como (estas,te va)"
r = "(ab,c)*,(de+,fg*)+"
create_AFND(r)

