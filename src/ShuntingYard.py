"""
	This class will allow to check the gramar of the Regular Expresion (RE).
		Also to convert the RE to RPN.

"""
from Global import *

class ShuntingYard:
		
	def __init__(self, re):
		self.tokenFunction = Global.tokenFunction
		self.tokenFunctionValue =  Global.tokenFunctionValue
		self.tokenSeparator =  Global.tokenSeparator
		self.re = re
		self.tokens = self.toTokenList(re)
		self.rpn = self.toRPN(self.tokens)

	def toTokenList(self, re):
		TokenList = [i for i in re]

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

	def toRPN(self, tokens):
		cola = []
		pila = []
		for t in tokens:
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
			elif t in self.tokenSeparator.values():
				if t == self.tokenSeparator['Opening']:
					pila.append(t)
				else:
					if not self.tokenSeparator['Opening'] in pila:
						raise SyntaxError('Parentesis incompletos')
					while pila[-1] != self.tokenSeparator['Opening']:
						cola.append(pila.pop())
					pila.pop()
			else:
				cola.append(t)

		if self.tokenSeparator['Opening'] in pila:
			raise SyntaxError('Parentesis incompletos')
		while len(pila) != 0:
			cola.append(pila.pop())
		return cola


exp = "(hola, hey) como (estas,te va)"
sy = ShuntingYard(exp)
for i in sy.rpn:
	print i,
