def sort(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                l[i],l[j] = l[j],l[i]
    return l
