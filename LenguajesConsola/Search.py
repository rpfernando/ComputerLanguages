
import sys
from libs.AFND import *
from libs.Matches import *
import libs.cons as cons

OPTIONS = ['-h', '-e', '-a', '-oa', '-o']
automaton = None
files = None
matches = []
output_html = ""

def str_matches_by_line():
	global matches, files
	bounds = []
	s = ""
	for f in files:
		bounds.append([])
		of = open(f,'r').read()
		index = of.find('\n')
		while index != -1:
			bounds[-1].append(index)
			index = of.find('\n', index + 1)
		bounds[-1].append(len(of))
	for match, bound, f in zip(matches, bounds, files):
		of = open(f,'r').read()
		index = f.rfind('/') + 1
		for x, y in match:
			for line, b in enumerate(bound):
				if b >= x:
					cosa = f[index:] + '; line ' + str(line + 1) + ': ' + of[bound[line - 1] + 1 :x]
					sys.stdout.write(cosa)
   					sys.stdout.flush()
					cons.set_text_attr(cons.FOREGROUND_BLUE)
					cosa = of[x:y]
					sys.stdout.write(cosa)
   					sys.stdout.flush()
					cons.set_text_attr(cons.FOREGROUND_GREY)
					cosa = of[y:b]
					sys.stdout.write(cosa)
   					sys.stdout.flush()
					print
					s += f[index:] + '; line ' + str(line + 1) + ': ' + of[bound[line - 1] + 1 :x] + '<b>' + of[x:y] + '</b>' + of[y:b] + '<br>'
					break
	return s

def check_or_create_atomaton(args):
	global automaton, files
	if automaton != None:
		return

	if not '-e' in args:
		print
		print 'Invalid args: Regex missing.'
		sys.exit(2)

	index = args.index('-e')

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
	global automaton, files, output_html
	if opt == '-a':
		check_or_create_atomaton(args)
		print automaton
	if opt == '-o':
		check_or_create_atomaton(args)
		output = open('output/output.html', 'w')
		check_or_get_matches()
		output.write(output_html)
	if opt == '-oa':
		check_or_create_atomaton(args)
		ouputt = open('output/outputt.txt', 'w')
		ouputt.write(str(automaton))
	if opt == '-e':
		check_or_create_atomaton(args)
		check_or_get_matches()
		output_html = str_matches_by_line()


if __name__=='__main__':
	
	args = sys.argv

	for opt in OPTIONS:
		if opt in args:
			option_select(opt, args)

