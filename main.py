from getting_info import getting_equations, examples

def CheckConsistency():
	# create a function to test there are solution return =>1
	# or infinite solution return =>2 
	# no solution  return => 3

	pass

def gauss_jordan_elimination(a, n):
	c = 0
	for i in range(n):
		if (a[i][i] == 0):
			c = 1
			while ((i + c) < n and a[i + c][i] == 0):
				c += 1
			if ((i + c) == n):	
				break
			j = i
			for k in range(1 + n):
				temp = a[j][k]
				a[j][k] = a[j+c][k]
				a[j+c][k] = temp

		for j in range(n):
			if (i != j):
				p = a[j][i] / a[i][i]
				k = 0
				for k in range(n + 1):
					a[j][k] = a[j][k] - (a[i][k]) * p
	return CheckConsistency(a,n)

def main():
	pass
	



	
	

main()
