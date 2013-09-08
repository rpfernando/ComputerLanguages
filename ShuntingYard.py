"""
	This class will allow to check the gramar of the Regular Expresion (RE).
		Also to convert the RE to RPN.

"""


class ShuntingYard:
		
	def __init__(self, re):
		self.tokenFunction = ( ',' )
		#self.tokenSeparator =  ( Opening:'(', Ending:')' )
		self.tokenSeparator =  ( '(', ')' )
		self.re = re
		self.tokens = self.toTokenList(re)
		self.rpn = self.toRPN(self.tokens)

	def toTokenList(self, re):
		TokenList = [re]
		aux = []
		for tf in self.tokenFunction:
			for r in TokenList:
				aux2 = r.split(tf)
				index = len(aux2)
				index-=1
				while index > 0:
					aux2.insert(index, tf)
					index-=1
				aux += aux2
			TokenList = aux
			aux = []
		for ts in self.tokenSeparator:
			for r in TokenList: 
				aux2 = r.split(ts)
				aux += aux2
			TokenList = aux
			aux = []
		return TokenList

	def toRPN(self, tokens):
		cola = []
		pila = []
		for t in tokens:
			if t in self.tokenFunction:
				pila.append(t)
			elif t in self.tokenSeparator:
				if t == self.tokenSeparator[0]:
					pila.append(t)
				else:
					auxT = pila.pop()
					while auxT != self.tokenSeparator[0] :
						cola.append(auxT)
						auxT = pila.pop()
			else:
				cola.append(t)
		while len(pila) != 0:
			cola.append(pila.pop())
		return cola



exp = "(hola, hey) como (estas,te va)"
tok = ['(','hola',',',' hey',')',' como ', '(', 'estas', ',', 'te va', ')']
sy = ShuntingYard(exp)
rpn = sy.toRPN(tok)
for i in rpn:
	print i