#!/usr/bin/python3




class Matrix(object):


	def __init__(self,initial_matrix):

		m = max([len(row) for row in initial_matrix])
		if any([len(row)!=m for row in initial_matrix]):
			raise ValueError("Not a valid matrix")
	
		self.num_cols = m
		self.num_rows = len(initial_matrix)

		self.matrix = {}


		for row in range(self.num_rows):
			for col in range(self.num_cols):
				self.matrix[row,col] = initial_matrix[row][col]
				


	def __getitem__(self,key):
		return self.matrix[key]

	def __setitem__(self,key,value):
		try:
			self.matrix[key]
		except KeyError:
			raise KeyError("{0} out of bounds of matrix".format(key))
		self.matrix[key] = value


	def __str__(self):

		out = ""

		for row in self.get_rows():
			for entry in row:
				out += " {0}".format(entry)
			out+="\n"
		return out



	def get_rows(self,row=-1):
		out = []
		for r in range(row+1,self.number_of_rows()):
			tmp = []
			for c in range(self.number_of_columns()):
				tmp.append(self[r,c])
			out.append(tmp)
		return out

	def get_columns(self,col=-1):
		out = []
		for c in range(col+1,self.number_of_columns()):
			tmp = []
			for r in range(self.number_of_rows()):
				tmp.append(self[r,c])
			out.append(tmp)
		return out


	def number_of_rows(self):
		return self.num_rows

	def number_of_columns(self):
		return self.num_cols
		















if __name__=="__main__":

	m = [[1,2,3],[4,5,6]]

	A = Matrix(m)


	print(A.get_columns())







