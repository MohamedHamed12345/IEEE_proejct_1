


import os.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
def examples(): #This function creates a file called user_manual.txt
    try :
        file=open('user_manual.txt','w',encoding='utf-8',errors='ignore')
    except :
      file=open('user_manual.txt','x',encoding='utf-8',errors='ignore')
    SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    number_of_equation=int(input("enter number of equations : "))
    file=open('user_manual.txt','w',encoding='utf-8',errors='ignore')
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
            if i==number_of_equation-1 :
                break
            else :
               position=position+len(string)
               L[position:-3]=' + '
            position=position+1
        file.writelines(L)
        file.write('\n')
    file = open("user_manual.txt", "r",encoding='utf-8',errors='ignore')
    f_contents=file.readlines()
    print(f_contents,end='')
    print('\n',__file__)
    file.close()
    
    
# examples()






def getting_equations():
    
    path = open(os.path.join(BASE_DIR, " equations.txt"),'r')
    num=int(path.readline().split()[-1])
    lst=[]
    for line in path:
        line.replace('+',' + ')
        line.replace('-',' - ')
        line=line.replace('=',' = ')
        line=line.strip().split()[1:]
        tmplst=[0]*(num+1)
        for idx ,element in enumerate(line):
            if 'x' not in element :continue
            factor,ordx=element.split('x')
            
            factor=int(factor)
            if line[idx-1]=='-':factor*=-1
            ordx=int(str(ord(ordx))[3:])
        
            tmplst[ordx-1]=factor
        tmplst[-1]=int(line[-1])
        lst.append(tmplst)
        
       
    print(lst)
    return lst



getting_equations()




# def examples():
#     num =int(input('hi enter the number of equations : '))
#     SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
#     file=open('user_manual.txt', 'w')
#     file.write(f'Number of equations: {num}\n')
#     for i in range(1,num+1):
#         eq=''
#         for j in range(1,num+1):
#             if j!=1:eq+='+'               # not add + in last of equation 
#             eq+=f'a{i}{j} x {j}'          # every time  add term such a11x2
#         eq+=f'= a{i}\n'                   # at the end of equation add =a2
#         file.write(eq.translate(SUB))     # write the equation at the end 

# examples()
