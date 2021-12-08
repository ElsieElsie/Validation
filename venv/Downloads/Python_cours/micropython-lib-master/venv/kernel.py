class semantic_transition_relation:
	def __init__(self):
	    def actions(self,conf):
	        def execute(self,conf,action):

class Beh_soup_Semantic():
	def initial(self):
	    return [soup.initial]

	def actions(self,conf):
	    return list(map(lamba beh: beh.action),filter(lamba beh: beh.guard_def),self.soup.behaviors)

	def execute(self,c,a):
		target = copy.deepcopy(c)
		r= a(target)
		return target
		
class Str2TR:
	def __init__(self,str):
		self.operand = str

	def initial(self):
		return self.operand.initial()

	def next(self,c):
		target = []

		for a in self.operand.actions(c):
			target = self.operand.execute(c,a)
			target.append(target)
		return target
