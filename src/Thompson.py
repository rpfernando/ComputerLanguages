from Global import *
import ShuntingYard
from collections import defaultdict

def create_AFND(re):
	initial_node = ShuntingYard.create_tree(ShuntingYard.to_rpn(re))
	atomaton = set()
	s = State('s')
	f = State('f')
	s.add_transition(initial_node, f);
 
class State:
	def __init__(self, name):
		self.name = name
		self.closure = set()
		self.add_to_closure(self)
		self.transitions = dict() 

	def add_to_closure(self, state):
		self.closure.add(state)

	def add_transition(self, simbol, destination):
		self.transitions.setdefault(simbol, []).append(destination)

	def __str__(self):
		return "State: " + self.name + "."


#r = "(hola, hey) como (estas,te va)"
r = "(ab,c)*,(de+,fg*)+"
create_AFND(r)

