
def examples():
    """ 
    This function creates a file called user_manual.txt
    getting input from user and checking it
    it opens the file and appends the formula of equation in it depending on the given number
    using some strings like eq, x, a  and SUB(to subscript numbers)
    to write them in the file
    it also prints the path of the created file

    """
    import os

    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

    try:
        number_of_equation = int(input("enter number of equations : "))
    except ValueError:
        file = open('user_manual.txt', 'w', encoding='utf-8', errors='ignore')
        file.write(
            "the number should be an integar(like this 2 or 3 or .....) not string ")
        print("the path of the file is: ", os.path.abspath('user_manual.txt'))
        return 0

    while int(number_of_equation) < 2:
        print("number of equations should at least be 2")
        number_of_equation = int(input("enter number of equations : "))

    file = open('user_manual.txt', 'w', encoding='utf-8', errors='ignore')
    L = ["Number of equations: ", str(number_of_equation), "\n"]
    file.writelines(L)
    a, d, f, zero = "x", "a", "eq", "0"

    for line in range(0, number_of_equation):
        s = str(line+1)
        str1 = (f + s).translate(SUB)
        print(str1)
        str8 = (d + s + zero).translate(SUB)
        L = [str1, ' : ', ' = ', str8]
        position = 2
        for i in range(0, number_of_equation):
            j = str(i + 1)
            str2 = (d + s + j + a + j).translate(SUB)
            string = ' ' + str2 + ' '
            L[position: -3] = string
            if i == number_of_equation - 1:
                break
            else:
                position = position + len(string)
                L[position: -3] = '+'
            position = position + 1
        file.writelines(L)
        file.write('\n')

    file = open("user_manual.txt", "r", encoding='utf-8', errors='ignore')
    # print(file.readlines())
    file.close()

    print('\n', '#' * 150)
    print("the path of the file is: ", os.path.abspath('user_manual.txt'))
    print('#' * 150, '\n')

    
examples()
