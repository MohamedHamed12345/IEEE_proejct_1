
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
    zero,one,two,three ='0','1','2','3'
    for line in range(0,number_of_equation):
        s=str(line+1)
        str1=(f+s).translate(SUB)
        str2=(d+s+one).translate(SUB)
        str3=(a+one).translate(SUB)
        str4=(d+s+two).translate(SUB)
        str5=(a+two).translate(SUB)
        str6=(d+s+three).translate(SUB)
        str7=(a+three).translate(SUB)
        str8=(d+s+zero).translate(SUB)
        L=[str1,' : ',str2+str3,' + ',str4+str5,' + ', str6+str7,' = ',str8,]
        file.writelines(L)
        file.write('\n')
    file = open("user_manual.txt", "r")
    f_contents=file.readlines()
    print(f_contents,end='')
    print('\n',__file__)
    file.close()
    
    
examples()