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
		self.closure = set()
		self.add_to_closure(self)
		self.transitions = dict() 

	#Instead of adding an epsilon transition add it to the closure.
	def add_to_closure(self, state):
		self.closure.add(state)

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
		try:
			return self.transitions[simbol]
		except Exception, e:
			return []
			

	def __str__(self):
		return "State: " + self.name + "."

class Thompson:

	@staticmethod
	def generic(origin, tree, destination):
		if tree.char == Global.all_token_function['Union']:
			return Thompson.union(origin, tree, destination)
		if tree.char == Global.all_token_function['Link']:
			return Thompson.link(origin, tree, destination)
		if tree.char == Global.all_token_function['Closure']:
			return Thompson.closure(origin, tree, destination)
		if tree.char == Global.all_token_function['Positive_Closure']:
			return Thompson.positive_closure(origin, tree, destination)

	@staticmethod
	def positive_closure(origin, tree, destination):
		list_to_return = [] #must contain the new transitions(origin, subtree, destination) that will be needed and delete the oldones
		return list_to_return

	@staticmethod
	def closure(origin, tree, destination):
		list_to_return = [] #must contain the new transitions(origin, subtree, destination) that will be needed and delete the oldones
		return list_to_return

	@staticmethod
	def link(origin, tree, destination):
		list_to_return = [] #must contain the new transitions(origin, subtree, destination) that will be needed and delete the oldones
		return list_to_return

	@staticmethod
	def union(origin, tree, destination):
		list_to_return = [] #must contain the new transitions(origin, subtree, destination) that will be needed and delete the oldones
		return list_to_return	


