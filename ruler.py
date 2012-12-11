class Ruler(object):
	"""docstring for Ruler"""
	def __init__(self):
		super(Ruler, self).__init__()

	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
		return True

class heading_rule(Ruler):
	type = 'heading'
	def condition(self, block):
		return not '\n' in block and len(block) <= 70 and not block[-1] = ':'

class title_rule(Ruler):
	type = 'title'
	first = True
	def condition(self, block):
		if not self.first:
			return False
		self.first = False
		return heading_rule.condition(self, block)

class listitem_rule(Ruler):
	type = 'listitem'
	def condition(self, block):
		return block[0] == '-'

	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block[1:].strip)
		handler.end(self.type)
		return True

class list_rule(Ruler):
	type = 'list'
	inside_the_list = False
	def condition(self, block):
		if listitem_rule.condition(self, block) and not inside_the_list:
			return True
		elif not listitem_rule.condition(self, block) and inside_the_list:
			return True

	def action(self, block, handler):
		if not inside_the_list:
			handler.start(self.type)
			inside_the_list = True
		else:
			handler.end(self.type)

class paragraph_rule(Ruler):
	type = 'paragraph'

	def condition(self, block):
	return Trues

#Questions
"""
1. what is the result ?
class base:
	var = False
	def func(self):
		if not var:
			print "statement 1"

		if not self.var:
			print "statement 2"

"""