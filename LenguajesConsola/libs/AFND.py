from Global import *
import ShuntingYard
from Thompson import *

class AFND:
	def __init__(self, re):
		self.re = re
		self.s = State('s')
		self.f = State('f')
		self.states = {self.s.name: self.s, self.f.name: self.f}
		self.__create_AFND()

	def __create_AFND(self):
		deltas = []
		initial_node = ShuntingYard.create_tree(ShuntingYard.to_rpn(self.re))
		self.s.add_transition(initial_node, self.f);
		deltas.append((self.s,initial_node))

		while len(deltas) > 0:
			(origin, simbol) = deltas.pop()
			if not origin in self.states.values():
				self.states.setdefault(origin.name, origin)

			if isinstance(simbol, ShuntingYard.Node):
				aux_deltas = Thompson.generic(origin, simbol)
				for t in aux_deltas:
					deltas.insert(0, t)

		for state_name in self.states:
			self.states[state_name].update_closure()

	def __state_list_delta(self, list_of_states, simbol):
		list_to_return = []

		for state in list_of_states:	
			aux = state.extended_delta(simbol)
			for s in aux:
				if not s in list_to_return:
					list_to_return.append(s)

		return list_to_return

	def get_matches(self, text):
		states = []
		#initial_index = 0
		match = False

		list_of_matches = []

		self.s.index = [0]
		states = self.s.extended_delta(Global.epsilon)
		if self.f in states:
			states.pop(states.index(self.f))

		for index in range(len(text)):
			states = self.__state_list_delta(states, text[index])
			self.s.index = [index + 1]
			states.append(self.s)
			if self.f in states: 
				for i in self.f.index:
					list_of_matches.append((i, index+1))
				self.f.index = []
				states.pop(states.index(self.f))
			
		return list_of_matches

	def __str__(self):
		return str(self.states)