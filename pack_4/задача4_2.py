x=input( ).split( )
a=list(map(int,x))
i=0
b=[ ]
while not i == (len(x)):
	m=x[i] * x（i+1）
	n=x（i+1）-1
	if m:
		if x（i+1）==0 and not(x[i]==0):
			pass
		elif n==-1 and a[i]==0:
			m=0
			n=0
			c.append(str(m))
			c.append(str(n))
		else:
			c.append(str(m))
			c.append(str(n))
			i += 2
		if not(len(c)):
			print('0 0')
		else:
			print(''.join(c).strip())
