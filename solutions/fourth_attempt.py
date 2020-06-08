inp = "HHHHH\nHHIHH\nHHFFH\nHHHHH\nHHHHH".replace("\n","")
gen= int(input("Gen "))
n =  int(len(inp)**0.5)
num = len(inp)
for _ in range(gen):
    inp = list(inp.replace("F","D"))
    inf = [i for i in range(num) if inp[i]=="I"]
    for i in inf:
        for k in [i-1,i+1,i-n,i+n]:
                if k in range(num) and inp[k] == "H":
                    inp[k]="I"
        inp[i]="F"
    inp="".join(inp)
    for i in range(0,num,n):
        inp = inp.replace("D","H")
        x="".join(inp[i:i+n])
        print(x)
    print()
    
    

        
            