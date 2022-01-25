# program to find an element form the list using binary search
def bsearch(alist,item):
    first=0
    last=len(alist)-1
    found =False
    while first<=last and not found:
        midpoint=(first+last)//2
        if alist[midpoint]==item:
            found=True
            print("Element found in position :",midpoint)
        else:
            if item <alist[midpoint]:
                last=midpoint-1
            else:
                first=midpoint+1
    if (found==False):
        print("Element not found")
    return found
a=[]
n=int(input("enter upper limit"))
# read n number to list
for i in range(n):
    a.append(int(input()))
#  read an element to search in the list:
x=int(input("enter element to search in the list:"))
# calling bsearch function
bsearch(a,x)
