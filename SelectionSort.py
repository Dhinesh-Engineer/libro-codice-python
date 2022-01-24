#program to sort an element using selection sort
# deffine selection sort function
def ssort(aList):
    for i in range (len(aList)):
        least=i
        for k in range(i+1,len(aList)):
            if aList[k]<aList[least]:
                least=k
                # call another functionn swap to interchange values
            swap(aList,least,i)

#define a function to swap the two values
def swap(A,x,y):
    temp=A[x]
    A[x]=A[y]
    A[y]=temp
    


# define empty list
a=[]
# read upper limit
n=int(input("ener upper limit:"))
#read n number to list
for i in range(n):
    a.append(int(input()))

# call ssort function
ssort(a)
print("after sorting :",a)
