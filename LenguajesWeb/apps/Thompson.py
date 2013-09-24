from Global import *
import ShuntingYard

class State:
	#Counts the number of states created and also allows you to name a state automaticaly.
	id = 0 

	def __init__(self, name=None):
		if name != None:
			self.name = name
		else:
			self.name = str(State.id)
			State.id += 1
		self.closure = []
		self.add_to_closure(self)
		self.transitions = dict() 

	#Instead of adding an epsilon transition add it to the closure.
	def add_to_closure(self, state):
		if self == state:
			self.closure.append(self)
		else:
			for s in state.closure:
				if not s in self.closure:	
					self.closure.append(s)

	def update_closure(self):
		for s1 in self.closure:
			if s1 != self:
				s1.update_closure()
			for s2 in s1.closure:
				if not s2 in self.closure:
					self.closure.append(s2)

	def delete_transition(self, simbol):
		return self.transitions.pop(simbol)

	def add_transition(self, simbol, destination):
		if simbol == Global.epsilon:
			self.add_to_closure(destination)
		else:
			try:
				self.transitions[simbol].append(destination)
			except Exception, e:
					self.transitions.setdefault(simbol, []).append(destination)

	def delta(self, simbol):
		if simbol == Global.epsilon:
			return self.closure
		try:
			return self.transitions[simbol]
		except Exception, e:
			return []

	def extended_delta(self, simbol):
		if simbol == Global.epsilon:
			return self.closure

		l = []
		for state in self.closure:
			l += state.delta(simbol)
		closure_l = []
		for state in l:
			closure_l += state.closure

		return closure_l		

	def __str__(self):
		return "State: " + self.name + "."

class Thompson:

	@staticmethod
	def generic(origin, tree):
		if tree.char == Global.all_token_function['Union']:
			return Thompson.union(origin, tree)
		if tree.char == Global.all_token_function['Link']:
			return Thompson.link(origin, tree)
		if tree.char == Global.all_token_function['Closure']:
			return Thompson.closure(origin, tree)
		if tree.char == Global.all_token_function['Positive_Closure']:
			return Thompson.positive_closure(origin, tree)

	@staticmethod
	def closure(origin, tree):
		list_to_return = [] #must contain the new transitions(origin, subtree) that will be needed and delete the oldones

		aux_destination = origin.delete_transition(tree)

		aux_state1 = State()
		aux_state2 = State()
		aux_epsilon_node = ShuntingYard.Node(Global.epsilon)

		origin.add_transition(aux_epsilon_node,aux_state1)
		list_to_return.append((origin, aux_epsilon_node))

		aux_state2.add_transition(aux_epsilon_node,aux_state1)
		list_to_return.append((aux_state2, aux_epsilon_node))

		for d in aux_destination:
			aux_state2.add_transition(aux_epsilon_node,d)
			origin.add_transition(aux_epsilon_node, d)

		aux_state1.add_transition(tree.left, aux_state2)
		list_to_return.append((aux_state1, tree.left))

		return list_to_return

	@staticmethod
	def positive_closure(origin, tree):
		list_to_return = [] #must contain the new transitions(origin, subtree) that will be needed and delete the oldones

		aux_destination = origin.delete_transition(tree)

		aux_state1 = State()
		aux_state2 = State()
		aux_epsilon_node = ShuntingYard.Node(Global.epsilon)

		origin.add_transition(aux_epsilon_node,aux_state1)
		list_to_return.append((origin, aux_epsilon_node))

		aux_state2.add_transition(aux_epsilon_node,aux_state1)
		list_to_return.append((aux_state2, aux_epsilon_node))

		for d in aux_destination:
			aux_state2.add_transition(aux_epsilon_node,d)

		aux_state1.add_transition(tree.left, aux_state2)
		list_to_return.append((aux_state1, tree.left))

		return list_to_return

	@staticmethod
	def link(origin, tree):
		list_to_return = [] #must contain the new transitions(origin, subtree) that will be needed and delete the oldones
		
		aux_state = State()
		aux_destination = origin.delete_transition(tree)

		origin.add_transition(tree.right, aux_state)
		list_to_return.append((origin, tree.right))

		for d in aux_destination:
			aux_state.add_transition(tree.left, d)
			list_to_return.append((aux_state, tree.left))

		return list_to_return

	@staticmethod
	def union(origin, tree):
		list_to_return = [] #must contain the new transitions(origin, subtree) that will be needed and delete the oldones

		aux_destination = origin.delete_transition(tree)

		for d in aux_destination:
			origin.add_transition(tree.left, d)
			origin.add_transition(tree.right, d)
			list_to_return.append((origin, tree.left))
			list_to_return.append((origin, tree.right))

		return list_to_return	


