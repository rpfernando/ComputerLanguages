"""
	This class will allow to check the gramar of the Regular Expresion (RE).
		Also to convert the RE to RPN.

"""
from Global import *

class ShuntingYard:
	
	# This is the constructor of the class.	
	def __init__(self, re):
		#Taking the global necessary values.
		self.token_function = Global.token_function
		self.token_function_value =  Global.token_function_value
		self.token_separator =  Global.token_separator

		self.re = re
		self.tokens = self.to_token_list(re)
		self.rpn = self.to_rpn(self.tokens)

	# Metod used to change the string to a list and introduct a concatenation operator.
	def to_token_list(self, re):
		token_list = [i for i in re]

		# With this for the concatenation operator is introduced.
		for i in reversed(range(len(token_list)-1)):
			if token_list[i] == self.token_separator['Opening']:
				continue
			if token_list[i+1] == self.token_separator['Ending']:
				continue
			if token_list[i] in self.token_function.values():
				continue
			if token_list[i+1] in self.token_function.values():
				continue
			token_list.insert(i+1,self.token_function['Link'])

		return token_list

	# This metod convert the prefix notation to postfis notation (rpn).
	def to_rpn(self, tokens):
		cola = []
		pila = []
		for t in tokens:
			#This first statement move the operator to the stack and then to the queue.
			if t in self.token_function.values():
				if len(pila) == 0:
					pila.append(t)
				else:
					auxT = pila.pop()
					while self.token_function_value[auxT] < self.token_function_value[t]:
						cola.append(auxT)
						auxT = pila.pop()
					pila.append(auxT)
					pila.append(t)
			#Here checks that the brackets are consistent.
			elif t in self.token_separator.values():
				if t == self.token_separator['Opening']:
					pila.append(t)
				else:
					if not self.token_separator['Opening'] in pila:
						raise SyntaxError('Parentesis incompletos')
					while pila[-1] != self.token_separator['Opening']:
						cola.append(pila.pop())
					pila.pop()
			#All the simbols of the alphabet.
			else:
				cola.append(t)

		#Checks that the stack is empty.
		if self.token_separator['Opening'] in pila:
			raise SyntaxError('Parentesis incompletos')
		while len(pila) != 0:
			cola.append(pila.pop())

		return cola


exp = "(hola, hey) como (estas,te va)"
sy = ShuntingYard(exp)
for i in sy.rpn:
	print i,
