#!/usr/local/bin/python3

import sys
import re
from KB_fact import *

KB_Tree = {}
FactBase = {}

if __name__ == "__main__":
	taskList = str()

	if (len(sys.argv) < 2):
		print("Пиздец, ты серьезно??? Ты че, охуел не подавать мне файл на чтение?!")

	file = open(sys.argv[1], "r")

	try:
		for i, line in enumerate(file):
			line = line.split('#')[0]
			line = line.replace(' ', '')
			newKB = list()

			if (line == ''):
				continue
			elif (line.startswith('=')):
				line = line.replace('=', '').replace('\n', '')

				for elem in line:
					FactBase[elem] = True
			elif (line.startswith('?')):
				taskList = line.replace('?', '')
			else:
				newKB = KB_fact(line, FactBase, KB_Tree)
				if (newKB.name in KB_Tree):
					KB_Tree[newKB.name].append(newKB)
				else:
					KB_Tree[newKB.name] = [newKB]
	except Exception as err:
		print(err, "At line #", i)

	for task in taskList:
		if task in FactBase:
			print(task, "-", True)
		elif task in KB_Tree:
			res = False

			for eq in KB_Tree[task]:
				solve = eq.resolve()

				if solve:
					res = solve
					break

			print(task, '-', res)
		else:
			print('Fact \'', task, '\' not found!', sep='')
			print(task, '-', False)
