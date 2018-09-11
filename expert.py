#!/usr/local/bin/python3

import copy
import sys
import re
from KB_fact import *

KB_Tree = {}
FactBase = {}

def line_parser(file):
	taskList = []

	try:
		for i, line in enumerate(file):
			line = line.split('#')[0]
			line = line.replace(' ', '').replace('\t', '').replace('\n', '')
			newKB = list()

			if (line == ''):
				continue
			elif (line.startswith('=')):
				line = line.replace('=', '')

				if (line.find(',') != -1):
					line = list(filter(None, line.split(',')))

				for elem in line:
					FactBase[elem] = True
			elif (line.find('?') != -1):
				line = line.replace('?', '')
				if (line.find(',') != -1):
					line = list(filter(None, line.split(',')))
				taskList = line
			else:
				newKB = KB_fact(line, FactBase, KB_Tree)
				names = []
				if (newKB.name.find('|') != -1 or newKB.name.find('^') != -1 or newKB.name.find('!') != -1):
					raise Exception('Inclution has non-supported logical operator!')
				if (newKB.name.find('+') != -1):
					names = newKB.name.split('+')
				else:
					names = [newKB.name]

				for n in names:
					kb_copy = copy.deepcopy(newKB)
					kb_copy.name = n
					kb_copy.tree = KB_Tree
					kb_copy.factBase = FactBase

					if (n in KB_Tree):
						KB_Tree[n].append(kb_copy)
					else:
						KB_Tree[n] = [kb_copy]
	except Exception as err:
		raise Exception(str(err) + ". At line #" + str(i + 1))

	return taskList

def resolveTask(taskList):
	for task in taskList:
		if task in FactBase:
			print("\033[1m\033[32m", task, " - ", True, "\033[0m", sep='')
		elif task in KB_Tree:
			res = False

			for eq in KB_Tree[task]:
				solve = eq.resolve()

				if solve:
					res = solve
					break

			print("\033[1m\033[32m", task, ' - ', res, "\033[0m", sep='')
		else:
			print("\033[1m\033[32m", task, ' - ', False, "\033[0m", sep='')

if __name__ == "__main__":
	taskList = str()
	arg = str()

	if (len(sys.argv) < 2):
		print("Пиздец, ты серьезно??? Ты че, охуел не подавать мне файл на чтение?!")
		exit()

	try:
		file = open(sys.argv[1], "r")

		taskList = line_parser(file)
		resolveTask(taskList)
	except Exception as err:
		print("\033[1m\033[41mError:", err, '\033[0m')

	while True:
		try:
			arg = input(">> ")

			if (arg.startswith('remove base')):
				KB_Tree = {}
			elif (arg.startswith('remove facts')):
				FactBase = {}
			else:
				if (arg.startswith('open ')):
					arg = open(arg.replace('open ', ''), 'r')
				taskList = line_parser([arg] if (type(arg) is str) else arg)
				if (taskList != []):
					resolveTask(taskList)

		except KeyboardInterrupt:
			exit()
		except Exception as err:
			print("\033[1m\033[41mError:", err, '\033[0m')
