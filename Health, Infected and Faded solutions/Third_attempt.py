inp = list("HHHHH\nHHIHH\nHHFFH\nHHHHH\nHHHHH".replace("\n",""))
num = len(inp)
numsq = int(num**0.5)
for k in range(10):
    for i in range(num):
        if inp[i]=="I":
            inp[i]="2"
            for k in [-1,1,-numsq,numsq]:
                if ((i+k)>=0 and (i+k)<num and inp[i+k]!="F"):
                    inp[i+k]="1"
        if inp[i]=="F":
            inp[i]="3"
    dix={"1":"I","2":"F","3":"H"}
    for i in range(num):
        if inp[i] in dix:
            inp[i]=dix[inp[i]]
        if i%numsq == 0:
            print("".join(inp[i-numsq:i]))

    
    
    