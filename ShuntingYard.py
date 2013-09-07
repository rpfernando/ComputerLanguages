"""
	This class will allow to check the gramar of the Regular Expresion (RE).
		Also to convert the RE to RPN.

"""


class ShuntingYard:
		
	def __init__(self, re):
		self.tokenFunction = ( ',' )
		self.tokenSeparator =  ( '(' , ')' )
		self.re = re
		self.tokens = self.toTokenList(re)

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



exp = "(hola, hey) como (estas,te va)"

sy = ShuntingYard(exp)
for i in sy.tokens:
	print i