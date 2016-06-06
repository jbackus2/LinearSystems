#!/usr/bin/python3

from matrix import *


def find_pivot_columns(A,modp = 0):

	pivot_columns = []
	for j in range(A.number_of_columns()):
		i = find_pivot(A,j)
		if i is None:
			continue
		for r in range(i+1,A.number_of_rows()):
			for c in range(A.number_of_columns()-1,j-1,-1):
				A[r,c] = A[i,j]*A[r,c] - A[r,j]*A[i,c]
				if modp !=0:
					A[r,c]%=modp
		pivot_columns.append(j)
	return pivot_columns


def find_pivot(A,col_num):

	for i in range(A.number_of_rows()):
		if A[i,col_num] == 0:
			continue
		if all([A[i,c]==0 for c in range(col_num)]):
			return i
	return None



if __name__ == "__main__":

	m = [[1,2,3],[4,5,1],[6,7,8]]

	A = Matrix(m)


	print(find_pivot_columns(A,0))

	print(A)

