
import sys
from libs.AFND import *
from libs.Matches import *

OPTIONS = ['-h', '-e', '-a', '-oa', '-o']
automaton = None
files = None
matches = []

def str_matches_by_line():
	global matches
	return str(matches)

def check_or_create_atomaton(args):
	global automaton
	global files
	if automaton != None:
		return
	
	index = args.index('-e')
	if index == -1:
		print 'Invalid args: Regex missing.'
		sys.exit(2)

	automaton = AFND(args[index + 1][1:-1])
	files = args[index + 2].split(',')

def check_or_get_matches():
	global matches, automaton, files
	if matches == []:
		for f in files:
			of = open(f,'r')
			matches.append(automaton.get_matches(of.read()))	

def option_select(opt, args):
	if opt == '-h':
		print open('help.txt').read()
	global automaton, files
	if opt == '-a':
		check_or_create_atomaton(args)
		print automaton
	if opt == '-o':
		check_or_create_atomaton(args)
		output = open('output/output.txt', 'w')
		check_or_get_matches()
		output.write(str_matches_by_line())
	if opt == '-oa':
		check_or_create_atomaton(args)
		ouputt = open('output/outputt.txt', 'w')
		ouputt.write(str(automaton))
	if opt == '-e':
		check_or_create_atomaton(args)
		check_or_get_matches()
		print str_matches_by_line()


if __name__=='__main__':
	
	args = sys.argv

	for opt in OPTIONS:
		if opt in args:
			option_select(opt, args)

