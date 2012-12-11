class Handler(object):
	"""docstring for Handler"""
	def __init__(self):
		super(Handler, self).__init__()

	# why this function dosen't return anything ,then what exactly will it return to var = callback() ?
	def callback(self, prefix, name, *args):
		method = getattr(self, prefix + name, None)
		if method:
			return method(*args)
		else:
			return None

	def start(self, name):
		self.callback('start_', name)

	def end(self, name):
		self.callback('end_', name)

	def sub(self, name):
		def substituation(match):
			result = self.callback('sub_', name, match)
			if result is None:
				result = match.group(0)
			return result
		return substituation

class HTMLRenderer(Handler):
	"""docstring for HTMLRenderer"""
	def __init__(self):
		super(HTMLRenderer, self).__init__()

	def feed(self, block):
		print block

	def start_document(self):
		print '<html><head></head><body>'

	def end_document(self):
		print '</body></html>'			

	def start_heading(self):
		print '<h2>'

	def end_heading(self):
		print '</h2>'

	def start_paragraph(self):
		print '<p>'

	def end_paragraph(self):
		print '</p>'

	def start_list(self):
		print '<ul>'

	def end_list(self):
		print '</ul>'

	def start_listitem(self):
		print '<li>'

	def end_listitem(self):
		print '</li>'

	def start_title(self):
		print '<h1>'

	def end_title(self):
		print '</h1>'

	def sub_emphasize(self, match):
		return '<em><font size=\'20\'>%s</font></em>' % match.group(1)

	def sub_mailto(self, match):
		return "<a href='mailto:%s'>%s</a>" % (match.group(0), match.group(0))

	def sub_url(self, match):
		return "<a href='%s'>%s</a>" % (match.group(0), match.group(0))


#Questions:
"""
1.Should I create a class inherited from object?
2.Will the constructor of super class be automatically invoked 
	in case of visually define __init__ in sub class but not invoking super class's constructor  ,
	or in case of not visually define _init_ in sub class.
3.*arg : arbitary number arguments, diff between *arg , **arg , how to use them ?
4. getattr() ?
5. will var == None  ? 
	def func():
		pass
	var = func()
"""