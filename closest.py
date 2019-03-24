def closest(arr):
    f=sorted(arr)
    #print("Sorted Array-",f)
    k=[]
    y=[]
    for o in range(len(f)):
        i=o+1
        if o==(len(f)-1):
            t=f[o]
            k.append(t)
        else:
            t=f[i]-f[o]
            k.append(t)
            y.append((f[o],f[i]))
    #print(k,"\n",y)
    min_value = min(k)
    rr=[i for i, x in enumerate(k) if x == min_value]
    for j in rr:
        print(y[j][0],y[j][1],end=" ")
        
n = int(input())
arr = list(map(int, input().rstrip().split()))
closest(arr)
        
        
        
    
    
