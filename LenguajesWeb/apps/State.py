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
				#s1.extended_delta(Global.epsilon)
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
		l = []
		for state in self.closure:
			l += state.delta(simbol)
		closure_l = []
		for state in l:
			closure_l += state.closure

		return closure_l		

	def __str__(self):
		return "State: " + self.name + "."