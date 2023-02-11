
def examples(): #This function creates a file called user_manual.txt
    try :
        file=open('user_manual.txt','w')
    except :
      file=open('user_manual.txt','x')
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    number_of_equation=int(input("enter number of equations : "))
    file=open('user_manual.txt','w')
    L = ["Number of equations: ",str(number_of_equation)]
    file.writelines(L)
    file.write('\n')
    a="x"
    d="a"
    f="eq"
    zero ='0'
    for line in range(0,number_of_equation):
        s=str(line+1)
        str1=(f+s).translate(SUB)
        str8=(d+s+zero).translate(SUB)
        L=[str1,' : ',' = ',str8]
        position=2
        for i in range(0,number_of_equation):
            j=str(i+1)
            str2=(d+s+j).translate(SUB)
            str3=(a+j).translate(SUB)
            string=str2+str3
            L[position:-3]=string
            position=position+len(string)
            L[position:-3]='+'
            position=position+1
        file.writelines(L)
        file.write('\n')
    file = open("user_manual.txt", "r")
    f_contents=file.readlines()
    print(f_contents,end='')
    print('\n',__file__)
    file.close()
    
    
examples()