# program to sort an element using insertion sort
def isort(a):
    for index in range (1,len(a)):
        currentvalue =a[index]
        position =index
        while position>0 and a[position-1]>currentvalue:
            a[position]=a[position-1]
            position=position-1
        a[position]=currentvalue

a=[] #define  empty list
n=int(input("enter upper limit:"))
for i in range(n):
    a.append(int(input()))
    # call isort function
    isort(a)
    print("list after insert:",a)
