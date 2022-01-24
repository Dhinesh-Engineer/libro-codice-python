# BUBBLE SORT  using function
# define a function for bubble sort
def bubble(a):
    for i in range(len(a)-1,0,-1):
        for j in range (i):
            if (a[j]>a[j+1]):
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
#define an empty lisr
a=[]
#read upper limit
n=int(input("enter upper limit:"))
#read n  number to list
for i in range(n):
    a.append(int(input()))

print("Element in the list before sorting")
print(a)

# call bubble sort function
bubble(a)
print("element in list after sorting :")
print(a)
             
