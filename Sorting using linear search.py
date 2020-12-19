#sorting using linear search technique
list=[]
flag=0
n=int(input("Enter limit"))
for i in range(0,n):
    x=int(input())
    list.append(x)

def sor(list):    
    key=min(list)

    for i in range(len(list)):
        aa=list.index(key)
        for j in list:
            b=list[i]
            list[i]=list[aa]
            list[aa]=b
            if list==list.sort():
                flag=1
    print(list)
    return
if flag==1:
    sor(list)
        
else:
    sor(list[1::])
            
