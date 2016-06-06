#!/usr/bin/python3

from matrix import *

from pivots import *





cnt = 0

N= 10

for i in range(2**N):

	m = [int(elm) for elm in bin(i)[2:]]

	out = [0 for i in range(N-len(m))]
	out.extend(m)

	A = Matrix([out[:int(N/2)],out[int(N/2):]])

	pivots=find_pivot_columns(A,2)
	
	if int(N/2-1) not in pivots:
		cnt+= 1





print(cnt)

print(cnt/2**N)
