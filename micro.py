
def build ():
	return

class place:

	#__name__ = None

	def __init__ (self,*to,**here):
		self.links	= to
		self.actions = here
		self.run('__name__')

	def __repr__ (self):
		return self.__str__()
	def __str__ (self):
		s = ')'
		for a in self.actions:
			s = ',%s=%s' %(a,self.actions[a].__repr__()) + s
		return self.__class__.__name__ + str(self.links).replace(')',s)

	def act (self,action):
		try:
			return self.__getattribute__(action)
		except AttributeError:
			try:
				a = self.actions[action]
				if type(a) == str:
					a = eval(a)
			#	a = a.__call__
			except Exception:
				pass
			self.__setattr__(action,a)
		return a
	
	def run (self,action):
		try:
			a = self.__getattribute__(action)
			try:
				return a()
			except AttributeError:
				return a
		#	return self.__getattribute__(action)()
		except AttributeError:
			try:
				b = a = self.actions[action]
				if type(a) == str:
					a = eval(a)
					b = a()
			#	return b
			except AttributeError:
				b = a
			#	return a
			except KeyError:
				return NotImplemented
			#except:
			#	print('An error has occurred calling %s: %s' %(action.__repr__(),self.actions[action].__repr__()))
			#	return
			self.__setattr__(action,a)
			return b
	#			print('Erro')
	#		if type(a) == function:
	#			return a()
	#		return a
	
	def edit (self):
		pass

	def copy (self):
		return place(*self.links,**self.actions)

a = place(12,1,2,art='lambda: print("Artes")',Artes=123,__name__=None)
a.run('art')
print(a.run('Artes'))
print(a.__name__)
print(a)