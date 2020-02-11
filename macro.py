import string

def encode (s,k=0,hex=string.hexdigits):

	j = (k//10)%((k%4)+1)
	while j >= 0:
		j -= 1
		l = (k//(10**(1+j)))%100
		s = ((' '*(l//10))+str(s)+((l%10)*' ')).encode()
	s = s.hex().title()
	r = []
	for c in s:
		c = hex.find(c)
		c = (c+int(k%len(hex)))%len(hex)
		k = abs(k/len(hex)) + (k%len(hex))
		if (k < len(hex)):
			k *= len(s)
		r.append(c)
	return tuple(r)

def decode (s,k=0,hex=string.hexdigits):
	r = ''
	m = k
	for c in s:
		c = (c-int(m%len(hex)))%len(hex)
		m = abs(m/len(hex)) + (m%len(hex))
		if (m < len(hex)):
			m *= len(s)
		r += hex[c]
	s = b''.fromhex(r)
	m = (k//10)%((k%4)+1)
	j = -2
	while m > j:
		j += 1
		try:
			s = s.decode()
			s = eval(s)
		except Exception:
			s = str(s)
	return s

def read (f,k=0):
	f = open(f,'r')
	c = eval(f.read())
	f.close()
	if not type(c) in (world,set,list,tuple):
		raise TypeError("%s object isn't a world or valid iterable encoding"%c.__class__.__name__)

	if type(c) != world:
		c = eval(decode(c,k))
		if type(c) != world:
			raise KeyError('incorrect decoding key: %s' %k.__repr__())

	return c

def write (f,c,p=None,k=None):
	f = open(f,'w')
	f.write(c.show(p,k))
	f.close()

class world:

	def __init__ (self,w=None,k=None,p=None):
		if (k ==None):
			k = 0
		self.map	= w
		self.key	= k
		self.password=p
		if type(w) == dict:
			for v in w:
				try:
					if w[v] == w[v].__name__:
						continue 
				except AttributeError:
					pass
				w[v].__setattr__('__name__',v)

	def __str__ (self):
		return self.__repr__()
	def __repr__ (self):
		return self.__class__.__name__ + '(%s, %s,%s)' %(self.map.__repr__(), self.key.__repr__(),self.password.__repr__())
	#	return self.__class__.__name__ + '(%s)' %self.map.__repr__()
	#	return self.__str__().replace(')',', %s,%s)' %(self.key.__repr__(),self.password.__repr__()))

	def show (self,p=None,k=None):
		if p!=self.password:
			if k == None:
				k = self.key
		if k != None:
			return str(encode(str(self),k))
		return str(self)

	def edit (self,n=None,p=None):
		if p!=self.password:
			raise PermissionError('incorrect editing password: %s' %p.__repr__())
		if n == None:
			return self.map
		self.map = n

	def copy (self):
		w = [self.map,self.key,self.password]
		m = len(w)
		while m > 0:
			m += -1
			try:
				w[m] = w[m].copy()
			except AttributeError:
				continue
		return world(*w)

print(eval(decode(eval(world(123,123,5412435343124).show()))))
print(eval(decode(eval(world(123,123,123).show()),123)))
print(world(123,123,123).copy())