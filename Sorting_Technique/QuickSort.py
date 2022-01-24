# quick sort
def qsort(alist):
    qsorthelp(alist,0,len(alist)-1)
def  qsorthelp(alist,first,last):
    if first<last:
        splitpoint=partition(alist,first,last)
        qsorthelp(alist,first,splitpoint-1)
        qsorthelp(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivot=alist[first]
    leftm=first+1
    rightm=last
    done =False
    while not done:
        while leftm<=rightm and alist[leftm]<=pivot:
            leftm=leftm+1
        while alist[rightm]>=pivot and rightm>=leftm:
            rightm=rightm-1
        if rightm<leftm:
            done=True
        else:
            temp=alist[leftm]
            alist[leftm]=alist[rightm]
            alist[rightm]=temp

    temp=alist[first]
    alist[first]=alist[rightm]
    alist[rightm]=temp
    return rightm
# define empty list
a=[]
# read upper limit
n=int(input("enter upper limit:"))
#read n number to list
for i in range(n):
    a.append(int(input()))

# call quick sort function
qsort(a)
print("After sorting" ,a)
