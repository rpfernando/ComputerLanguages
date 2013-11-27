"""
	This class will contain the global variables that will be used.
"""
class Global:
	comodin_token = '.'
	token_function = { 'Union':',', 'Link':'#'}
	token_unary_function = {'Closure': '*', 'Positive_Closure': '+'}
	all_token_function = dict(token_function.items() + token_unary_function.items())
	token_function_value =  {'*': 2, '+': 2, ',': 1, '#': 0, '(' : 5}
	token_separator =  { 'Opening':'(', 'Ending':')'}
	epsilon = '&'
