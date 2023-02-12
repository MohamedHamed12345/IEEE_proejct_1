from getting_info import getting_equations, examples

def CheckConsistency(a, n):
		for i in range(n):
			sumrow = sum(a[i][:-1])
			if sumrow == 0:
				if a[i][-1] == 0:
					return 2
				return 3
		return 1
		
def gauss_jordan_elimination(a, n):
	c = 0
	flag = 0
	for i in range(n):
		if (a[i][i] == 0):
			c = 1
			while ((i + c) < n and a[i + c][i] == 0):
				c += 1
			if ((i + c) == n):
				flag = 1
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

	flag=CheckConsistency(a,n)
	return flag

def main():
	def PrintResult(a, n, flag):
		f=open('solution.txt','w')
		if (flag == 2):
			print("infinite number of solutions\n")
		elif (flag == 3):
			print("There is no solution\n")
		else:
			f.write("There is one solution:\n")
			for i in range(n):
				f.write(str(a[i][n] / a[i][i])+'\n')

	a = [[0, 2, 1, 4], [1, 1, 2, 6], [2, 2, 2, 12]]
	# a=getting_equations()
	n = len(a)
	flag = gauss_jordan_elimination(a, n)
	PrintResult(a, n, flag)

main()
