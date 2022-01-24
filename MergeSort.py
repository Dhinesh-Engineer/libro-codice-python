#Mergee Sort
def  msort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len (alist)//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        msort(lefthalf)
        msort(righthalf)
        i=0;j=0;k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1;k=k+1
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print ("Merging sort",alist)

alist=[13,2,17,76,82,12,7]
msort(alist)
print(alist)
