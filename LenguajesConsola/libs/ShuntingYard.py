"""
	This class will allow to check the gramar of the Regular Expresion (RE).
		Also to convert the RE to RPN.

"""
from Global import *

class ShuntingYard:
	# This is the constructor of the class.	
	def __init__(self, re):
		self.re = re
		self.tokens = to_token_list(re)
		self.rpn = to_rpn(self.tokens)

class Node:
	def __init__(self, char, left=None, right=None):
		self.char = char
		self.left = left
		self.right = right

	def __str__(self):
		s = ""
		if self.right != None:
			s += str(self.right)
		if self.left != None:
			s += str(self.left)
		s += '\'' + self.char  + '\', '
		return s

def create_tree(rpn):
	if isinstance(rpn,str):
		rpn = [i for i in rpn]
	pila = []
	for token in rpn:
		if token in Global.token_function.values():
			if len(pila) < 2:
				raise SyntaxError('Missing Operands')
			pila.append(Node(token,pila.pop(),pila.pop()))
		elif token in Global.token_unary_function.values():
			if len(pila) < 1:
				raise SyntaxError('Missing Operands')
			pila.append(Node(token,pila.pop()))
		else:
			pila.append(token)
	if len(pila) > 1:
		SyntaxError('Missing Operands')
	return pila.pop()

	# Metod used to change the string to a list and introduct a concatenation operator.
def to_token_list(re):
	token_list = [i for i in re]

	# With this for the concatenation operator is introduced.
	for i in reversed(range(len(token_list)-1)):
		if token_list[i] == Global.token_separator['Opening']:
			continue
		if token_list[i+1] == Global.token_separator['Ending']:
			continue
		if token_list[i] in Global.token_function.values():
			continue
		if token_list[i+1] in Global.all_token_function.values():
			continue
		token_list.insert(i+1,Global.token_function['Link'])

	return token_list

	# This metod convert the prefix notation to postfis notation (rpn).
def to_rpn(tokens):
	tokens = to_token_list(tokens)
	cola = []
	pila = []
	tokens.insert(0,Global.token_separator['Opening'])
	tokens.append(Global.token_separator['Ending'])
	for t in tokens:
		#This first statement move the operator to the stack and then to the queue.
		if t in Global.token_function.values():
			if len(pila) == 0:
				pila.append(t)
			else:
				auxT = pila.pop()
				while Global.token_function_value[auxT] < Global.token_function_value[t]:
					cola.append(auxT)
					auxT = pila.pop()
				pila.append(auxT)
				pila.append(t)
			#Here checks that the brackets are consistent.
		elif t in Global.token_separator.values():
			if t == Global.token_separator['Opening']:
				pila.append(t)
			else:
				if not Global.token_separator['Opening'] in pila:
					raise SyntaxError('Missing bracket')
				while pila[-1] != Global.token_separator['Opening']:
					cola.append(pila.pop())
				pila.pop()
		#All the simbols of the alphabet.
		else:
			cola.append(t)
		#Checks that the stack is empty.
	if Global.token_separator['Opening'] in pila:
		raise SyntaxError('Missing bracket')
	while len(pila) != 0:
		cola.append(pila.pop())
	eliminate_redundancy(cola)
	return cola

def eliminate_redundancy(tokens_rpn):
	i = 0
	while i < len(tokens_rpn)-1:
		if tokens_rpn[i] in Global.token_unary_function.values() and tokens_rpn[i+1] in Global.token_unary_function.values():
			if tokens_rpn[i] == Global.all_token_function['Closure']:
				tokens_rpn.pop(i+1)
			elif tokens_rpn[i+1] == Global.all_token_function['Closure']:
				tokens_rpn.pop(i)
			else:
				tokens_rpn.pop(i)
			i-=1
		i+=1
