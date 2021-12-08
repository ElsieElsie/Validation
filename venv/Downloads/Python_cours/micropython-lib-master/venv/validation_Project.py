#TP 3
def hanoi_soup(nb_stock, nb_disk):
	i_conf = hanoiConfig(nb_stock, nb_disk)
	soup = behavior_Soup(i_conf)
  	for i in range(nb_stock):
		for j in range(nb_stock):
			soup.add((f'{i} - {j}'),guard_def(i,j),action_def(i,j))
	return soup

def guard_def(s,t):
    return lambda c:len(c.stocks[s]) and len(c.stocks[t] ==0) or c.stocks[s][-1]< c.stocks[t][-1]


def action_def(s,t):
    def action(c):
	disk = c.stocks[s].pap()
	c.stocks[t].append(disk)
	return action


class behavior_Soup:
	def __init__(self, conf):
	    self.initial = conf
	    self.behaviors = []

def add(n,g,a):
	self.behaviors.append(beh(n,g,a))

class Behavior:
	def __init__(self,name,g,a):
		self.name = name
		self.action = a
		self.guard_def = g

