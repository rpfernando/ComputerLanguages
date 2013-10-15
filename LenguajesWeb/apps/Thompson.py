from Global import *
from State import *
import ShuntingYard

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

		origin.add_transition(Global.epsilon, aux_state1)

		aux_state2.add_transition(Global.epsilon, aux_state1)
		list_to_return.append((aux_state2, Global.epsilon))

		for d in aux_destination:
			aux_state2.add_transition(Global.epsilon, d)
			origin.add_transition(Global.epsilon, d)

		aux_state1.add_transition(tree.left, aux_state2)
		list_to_return.append((aux_state1, tree.left))

		return list_to_return

	@staticmethod
	def positive_closure(origin, tree):
		list_to_return = [] #must contain the new transitions(origin, subtree) that will be needed and delete the oldones

		aux_destination = origin.delete_transition(tree)

		aux_state1 = State()
		aux_state2 = State()

		origin.add_transition(Global.epsilon, aux_state1)

		aux_state2.add_transition(Global.epsilon, aux_state1)
		list_to_return.append((aux_state2, Global.epsilon))

		for d in aux_destination:
			aux_state2.add_transition(Global.epsilon, d)

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


