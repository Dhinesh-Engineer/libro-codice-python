#program to find the specified elemenr from the list using
#linear searching
def ssearch(alist,item):
    pos=0
    found =False
    stop= False
    while pos<len(alist) and not found and not stop:
        if alist[pos]==item:
            found =True
            print("elements found in the list at postion:",pos)
        else:
            if alist[pos]>item:
                stop=True
            else:
                pos=pos+1
    if (found ==False):
        print("element not found")
    return found
# define empty list
a=[]
# read  upper limit
n=int(input("Enter the upper limit:"))
# read n numer to list
for i in range(n):
    a.append(int(input()))

#read an element to search in the lisit
x=int(input("enter the element to search in the list:"))

#calling ssearch function
ssearch(a,x)

    
