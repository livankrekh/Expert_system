import re

class KB_fact:

	def __init__(self, raw, fb, vocab):
		self.name = ""
		self.table = []
		self.factBase = fb
		self.tree = vocab
		self.implication = None

		if (raw.find('=>') == -1):
			raise Exception('No implication (\'=>\') or equality (\'<=>\') sign')
		elif (raw.find('<=>') != -1):
			eqution = raw.split('<=>')[0]
			name = raw.split('<=>')[1].replace('\n', '')
			self.implication = False
		else:
			eqution = raw.split('=>')[0]
			name = raw.split('=>')[1].replace('\n', '')
			self.implication = True

		eqution = eqution.replace('+', ' + ').replace('|', ' | ').replace('^', ' ^ ').replace('!', ' ! ').replace('(', ' ( ').replace(')', ' ) ').replace('  ', ' ')
		eqution = list(filter(None, eqution.split()))
		self.table = toPolish(eqution).split()
		self.name = name

	def resolve_name(self, name):

		if (name.find('|') != -1 or name.find('^') != -1 or name.find('!') != -1):
			raise Exception('Inclution has non-supported logical operator!')

		name_arr = name.split('+')

		for n in name_arr[1:]:
			new_fact = KB_fact(self.raw)

	def resolve(self):
		stack = []

		for elem in self.table:
			if (elem not in ['!', '+', '^', '|']):
				if (elem in self.factBase):
					stack.append(True)
				elif (elem in self.tree):
					res = False

					for eq in self.tree[elem]:
						solve = eq.resolve()

						if solve:
							res = solve
							break

					stack.append(res)

				else:
					stack.append(False)
					print('Not found fact \'', elem, '\'! By default = False', sep='')
			else:
				if (elem == '!'):
					stack[-1] = not stack[-1]
				else:
					if (len(stack) < 2):
						print('Warning! Redundant operator \'', elem, '\'. Ignored!', sep='')
					else:
						if (elem == '+'):
							stack[-2] = stack[-2] and stack[-1]
							stack.pop()
						elif (elem == '|'):
							stack[-2] = stack[-2] or stack[-1]
							stack.pop()
						elif (elem == '^'):
							stack[-2] = stack[-2] ^ stack[-1]
							stack.pop()

		return stack[-1]

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

def toPolish(tokenList):
    prec = {}
    prec["!"] = 3
    prec["^"] = 2
    prec["|"] = 2
    prec["+"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []

    for token in tokenList:
        if token not in prec and token != ')' and token != '(':
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)
