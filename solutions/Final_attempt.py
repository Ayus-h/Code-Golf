inp = "HHHHH\nHHIHH\nHHFFH\nHHHHH\nHHHHH".replace("\n","")
gen= int(input("Gen "))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk),end="") 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk),end="") 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk),end="") 
def colors(x):
    for i in x:
        if i == "H":
            prGreen(i) 
        elif i== "I":
            prRed(i)
        else:
            prYellow(i)

n =  int(len(inp)**0.5)
num = len(inp)
for i in range(gen+1):
    for i in range(0,num,n):
        inp = inp.replace("D","H")
        x="".join(inp[i:i+n])
        colors(x)
        print()
    
    inp = list(inp.replace("F","D"))
    inf = [i for i in range(num) if inp[i]=="I"]
    for i in inf:
        for k in [i-1,i+1,i-n,i+n]:
                if k in range(num) and inp[k] == "H":
                    inp[k]="I"
        inp[i]="F"
    inp="".join(inp)
    print()


  