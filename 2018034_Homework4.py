'''
NAME - GARVITA JAIN
SECTION - A
GROUP - 2
ROLL NO. - 2018034 
'''

import math

import matplotlib
from matplotlib import pyplot as py

py.ion()

def multiply(m1,m2):
	if len(m1)!=len(m2[0]):
		return False
	matrix=[]
	for i in range(len(m2)):
		l=[]
		for j in range(len(m1[0])):
			num=0
			for k in range(len(m1)):
				num+=m1[k][j]*m2[i][k]
			l.append(num)
		matrix.append(l)
	return matrix

class Polygon():
	def __init__(self):
		print('Enter x-coordinates of vertices')
		x=list(map(int, input().split()))
		print('Enter y-coordinates of vertices')
		y=list(map(int, input().split()))
		self.list_of_coordinates=[x,y]
		self.list_of_tuples=[]
		self.list_of_coordinates[0].append(self.list_of_coordinates[0][0])
		self.list_of_coordinates[1].append(self.list_of_coordinates[1][0])
		for i in range(len(x)):
			self.list_of_tuples.append((x[i],y[i]))

	def printit(self):
		print(self.list_of_coordinates[0])
		print(self.list_of_coordinates[1])

	def update_coordinates(self):
		for i in range(len(self.list_of_tuples)):
			self.list_of_coordinates[0][i]=self.list_of_tuples[i][0]
			self.list_of_coordinates[1][i]=self.list_of_tuples[i][1]

	def query(self):
		query_st=''
	#	query_st=query_st.split(' ')
		while query_st!='quit':
			query_st=input()
	#		query_st=query_st.split(' ')
			if query_st[0]=='s':
				self.scaling(query_st)
				self.printit()
			if query_st[0]=='t':
				self.translation(query_st)
				self.printit()
			if query_st[0]=='r':
				self.rotation(query_st)
				self.printit()

	def scaling(self, query):
		a, sx, sy=query.split(" ")
		sx=int(sx)
		sy=int(sy)
		scale=[[sx, 0, 0], [0, sy, 0], [0, 0, 1]]

		for k in range(len(self.list_of_tuples)):
			coord=[self.list_of_tuples[k][0], self.list_of_tuples[k][1], 1]
			newcoord=multiply(scale, [coord])
			self.list_of_tuples[k]=(newcoord[0][0], newcoord[0][1])

		self.update_coordinates()
		py.plot(self.list_of_coordinates[0], self.list_of_coordinates[1])

	def translation(self, query):
		a, dx, dy=query.split(" ")
		dx=int(dx)
		dy=int(dy)
		trans=[[1,0,0],[0,1,0],[dx,dy,1]]

		for k in range(len(self.list_of_tuples)):
			coord=[self.list_of_tuples[k][0], self.list_of_tuples[k][1], 1]
			newcoord=multiply(trans, [coord])
			self.list_of_tuples[k]=(round(newcoord[0][0],2), round(newcoord[0][1],2))

		self.update_coordinates()
		py.plot(self.list_of_coordinates[0], self.list_of_coordinates[1])

	def rotation(self, query):
		x, theta=query.split(" ")
		theta=int(theta)
		rotate=[[math.cos(theta), math.sin(theta), 0],
				[-math.sin(theta), math.cos(theta), 0],
				[0, 0, 1]]

		for k in range(len(self.list_of_tuples)):
			coord=[self.list_of_tuples[k][0], self.list_of_tuples[k][1], 1]
			newcoord=multiply(rotate, [coord])
			self.list_of_tuples[k]=(round(newcoord[0][0],2), round(newcoord[0][1],2))

		self.update_coordinates()
		py.plot(self.list_of_coordinates[0], self.list_of_coordinates[1])


class Disc():
	def __init__(self):
		self.x=int(input('Enter x-coordinate of center : '))
		self.y=int(input('Enter y-coordinate of center : '))
		r=int(input('Enter radius of disc : '))
		self.rx=r
		self.ry=r
		self.list_of_x=[]
		self.list_of_y=[]


		i=0
		while i<=(2*math.pi):
			self.list_of_x.append(self.x+self.rx*math.cos(i))
			self.list_of_y.append(self.y+self.ry*math.sin(i))
			i=i+0.01

		py.plot(self.list_of_x, self.list_of_y)

	def printit(self):
		print('Coordinates of center are ',(self.x,self.y))
		print('Radius along x-axis : ',self.rx)
		print('Radius along y-axis : ',self.ry)

	def query(self):
		query_st=''
		query_st=query_st.split(' ')
		while query_st[0]!='quit':
			query_st=input()
			query_st=query_st.split(' ')
			if query_st[0]=='s':
				self.scaling(query_st)
				self.printit()
			if query_st[0]=='t':
				self.translation(query_st)
				self.printit()
			if query_st[0]=='r':
				self.rotation(query_st)
				self.printit()

	def scaling(self, query):
			sx=int(query[1])
			sy=int(query[2])
			scale=[[sx, 0, 0], [0, sy, 0], [0, 0, 1]]

			for i in range(len(self.list_of_x)):
				coord=[self.list_of_x[i], self.list_of_y[i], 1]
				newcoord=multiply(scale, [coord])
				self.list_of_x[i]=newcoord[0][0]
				self.list_of_y[i]=newcoord[0][1]

			self.rx*=sx
			self.ry*=sy

			py.plot(self.list_of_x, self.list_of_y)

	def translation(self, query):
			dx=int(query[1])
			dy=int(query[2])
			translate=[[1, 0, 0], [0, 1, 0], [dx, dy, 1]]

			for i in range(len(self.list_of_x)):
				coord=[self.list_of_x[i], self.list_of_y[i], 1]
				newcoord=multiply(translate, [coord])
				self.list_of_x[i]=newcoord[0][0]
				self.list_of_y[i]=newcoord[0][1]

			self.x+=dx
			self.y+=dy

			py.plot(self.list_of_x, self.list_of_y)

	def rotation(self, query):
		theta=int(query[1])
		rotate=[[math.cos(theta), math.sin(theta), 0],
				[-math.sin(theta), math.cos(theta), 0],
				[0, 0, 1]]

		for i in range(len(self.list_of_x)):
			coord=[self.list_of_x[i], self.list_of_y[i], 1]
			newcoord=multiply(rotate, [coord])
			self.list_of_x[i]=newcoord[0][0]
			self.list_of_y[i]=newcoord[0][1]

		m=multiply(rotate,[[self.x, self.y, 1]])
		self.x=round(m[0][0],2)
		self.y=round(m[0][1],2)

		py.plot(self.list_of_x, self.list_of_y)


if __name__ == '__main__':
	shape=input('Enter shape type (disc/polygon) : ')
	if shape=='disc':
		obj=Disc()
		obj.query()
	elif shape=='polygon':
		obj=Polygon()
		obj.query()
	else:
		print('Invalid Shape')










