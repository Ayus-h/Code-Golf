import pandas as pd

def subs(a,b,c):
    li[a][b]=c
    return (a,b)
    
inp = "HHHHH\nHHIHH\nHHFFH\nHHHHH\nHHHHH"
li=[list(i) for i in inp.split("\n")]
faded = [(i,j) for i in range(len(li)) for j in range(len(li[i])) if li[i][j]=="F"]
infected = [subs(i,j,"F") for i in range(len(li)) for j in range(len(li[i])) if li[i][j]=="I"]
spread = [subs(i,j,"I") for x,y in infected for (i,j) in [(x+1,y),(x-1,y),(x,y-1),(x,y+1)] if ((i&j)>=0 &(i&j)<=len(li[0]))]

for i,j in faded:
    li[i][j]="H"
print(pd.DataFrame(li))



