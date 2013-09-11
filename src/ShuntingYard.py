"""
	This class will allow to check the gramar of the Regular Expresion (RE).
		Also to convert the RE to RPN.

"""
from Global import *

class ShuntingYard:
	
	# This is the constructor of the class.	
	def __init__(self, re):
		#Taking the global necessary values.
		self.tokenFunction = Global.tokenFunction
		self.tokenFunctionValue =  Global.tokenFunctionValue
		self.tokenSeparator =  Global.tokenSeparator

		self.re = re
		self.tokens = self.toTokenList(re)
		self.rpn = self.toRPN(self.tokens)

	# Metod used to change the string to a list and introduct a concatenation operator.
	def toTokenList(self, re):
		TokenList = [i for i in re]

		# With this for the concatenation operator is introduced.
		for i in reversed(range(len(TokenList)-1)):
			if TokenList[i] == self.tokenSeparator['Opening']:
				continue
			if TokenList[i+1] == self.tokenSeparator['Ending']:
				continue
			if TokenList[i] in self.tokenFunction.values():
				continue
			if TokenList[i+1] in self.tokenFunction.values():
				continue
			TokenList.insert(i+1,self.tokenFunction['Link'])

		return TokenList

	# This metod convert the prefix notation to postfis notation (rpn).
	def toRPN(self, tokens):
		cola = []
		pila = []
		for t in tokens:
			#This first statement move the operator to the stack and then to the queue.
			if t in self.tokenFunction.values():
				if len(pila) == 0:
					pila.append(t)
				else:
					auxT = pila.pop()
					while self.tokenFunctionValue[auxT] < self.tokenFunctionValue[t]:
						cola.append(auxT)
						auxT = pila.pop()
					pila.append(auxT)
					pila.append(t)
			#Here checks that the brackets are consistent.
			elif t in self.tokenSeparator.values():
				if t == self.tokenSeparator['Opening']:
					pila.append(t)
				else:
					if not self.tokenSeparator['Opening'] in pila:
						raise SyntaxError('Parentesis incompletos')
					while pila[-1] != self.tokenSeparator['Opening']:
						cola.append(pila.pop())
					pila.pop()
			#All the simbols of the alphabet.
			else:
				cola.append(t)

		#Checks that the stack is empty.
		if self.tokenSeparator['Opening'] in pila:
			raise SyntaxError('Parentesis incompletos')
		while len(pila) != 0:
			cola.append(pila.pop())

		return cola


exp = "(hola, hey) como (estas,te va)"
sy = ShuntingYard(exp)
for i in sy.rpn:
	print i,
