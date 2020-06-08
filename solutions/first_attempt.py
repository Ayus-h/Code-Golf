inp = "HHHHH\nHHIHH\nHHFFH\nHHHHH\nHHHHH"
gen = 1
li=[list(i) for i in inp.split("\n")]

for i in range(gen):
    change = []
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j] == "I":
                li[i][j] ="F"
                change.append([(i,j-1),(i,j+1),(i+1,j),(i-1,j)])
            elif li[i][j]== "F":
                li[i][j] = "A"
    
    for k,l in change[0]:
        if (k >=0 and l>=0) and (k<=j and l <=j):
            if li[k][l] != "F" and li[k][l] !="A":
                li[k][l] = "I"
    
    for i in range(len(li)):
        for j in range(len(li[i])):
            if li[i][j]=="A":
                li[i][j]="H"

print()       
for i in li:
    i = "".join(i)
    print(i)


        
    
            
            

