# create a function to test there are solution return =>1
# or infinite solution return =>2
# no solution  return => 3

def CheckConsistency(a, n):
    for i in range(n):
        sumrow = sum(a[i][:-1])
        if sumrow == 0:
            if a[i][-1] == 0:
                return 2
            return 3
    return 1

# this function apply the transformation to the matrix
# and at the end of the matrix will be like this a=[[5,0,0],[0,6,0],[0,0,8]]
# and we call the CheckConsistency
# to test the matrix and check
# after this the main will print
# at the end of gauss_jordan_elimination return 1 or 2 or 3
# and the matrix will modified 
#


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

    return a


def main():
    """
    this function prints the solution for the equation 
    it sends the matrix to the other functions and recive an integar
    by this integar it can find whether there is a solution or not
    after that it prints the final answer
    """
    def Result(c, n, ans):
        f = open('solution.txt', 'w', encoding='utf-8', errors='ignore')
        if (ans == 2):
            f.write("infinite number of solutions\n")
        elif (ans == 3):
            f.write("There is no solution\n")
        else:
            f.write("There is one solution:\n")
            for i in range(n):
                try:
                    f.write(str(c[i][n] / c[i][i]) + '\n')
                except (ZeroDivisionError):
                    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
                    L = (("x" + str(i + 1)).translate(SUB) + " = zero")
                    f.writelines(L)
                    f.write('\n')
                    continue

    a = [[0, 0, 1, 5], [0, 0, 2, 10], [0, 0, 1, 5]]
    n = len(a)
    c = []
    c = gauss_jordan_elimination(a, n)
    ans = CheckConsistency(c, n)
    Result(c, n, ans)

    import os
    print('\n', '#' * 150)
    print("the path of the file is: ", os.path.abspath('solution.txt'))
    print('#' * 150, '\n')


main()
