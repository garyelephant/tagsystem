from util import *
from handler import HTMLRenderer
from ruler import *
import sys
import re

class Parser(object):
	"""docstring for Parser"""
	def __init__(self, handler):
		super(Parser, self).__init__()
		self.rules = []
		self.filters = []
		self.handler = handler

	def addRule(self, rule):
		self.rules.append(rule)

	def addFilter(self, pattern, name):
		def filter(block, handler):
			return re.sub(pattern, handler.sub(name), block)
		self.filters.append(filter)

	def parse(self, file):
		self.handler.start('document')
		for block in blocks(file):
			for filter in self.filters:
				block = filter(block, self.handler)
			for rule in self.rules:
				if rule.condition(block):
					last = rule.action(block, self.handler)
					if last:
						break
		self.handler.end('document')

class BasicTextParser(Parser):
	def __init__(self, handler):
		super(BasicTextParser, self).__init__(handler)
		#self.addRule(heading_rule())
		self.addRule(paragraph_rule())

		self.addFilter(r'\*(.+?)\*', 'emphasize')
		self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
		self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mailto')
		
handler = HTMLRenderer()
htmlParser = BasicTextParser(handler)
htmlParser.parse(sys.stdin)		

#Question
"""
1. the mechanism of python to find module.
"""