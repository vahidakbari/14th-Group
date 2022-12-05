from random import randint

print("Well Come to My game")
print("*"*40)

while True:
    n = input("Please Chice a valid number: ")
    if n.upper() == 'Q' or n.upper() == 'QUITE':
        break
    if not n.isdigit():
        n = input("Please Chice a valid number: ")
        continue
    else:
        de=[]
        i=0
        nn=int(n)
        while not (sum(de)==nn or sum(de)==-nn) or de==[] and not n=="Q":
            coi= input("Please Choice:")
            coi=coi.upper()
            if coi == 'Q' or coi == 'QUITE':
                n="Q"
                break
            co= 1 if coi.find("ROCK")>=0 or coi.find("R")>=0 else 2 if coi.find("PAPER")>=0 or coi.find("P")>=0 else 3 if coi.find("SCISSER")>=0 or coi.find("S")>=0 else 0
            if co == 0:
                print("Please Valid Choice:")
                continue
            else:
                r=randint(1,3)
                if r==1: cc="ROCK"
                elif r==2: cc="PAPER"
                else: cc="SCISSER"
                if co==r:
                    print("tie")
                    continue
                elif co==1 and r==2:
                    de.append(1)
                    i=i+1
                elif co==1 and r==3:
                    de.append(-1)
                    i=i+1
                elif co==2 and r==1:
                    de.append(-1)
                    i=i+1
                elif co==2 and r==3:
                    de.append(1)
                    i=i+1
                elif co==3 and r==1:
                    de.append(1)
                    i=i+1
                elif co==3 and r==2:
                    de.append(-1)
                    i=i+1
                print(sum(de))

        if sum(de)==nn:
            print("Win")
        elif sum(de)==-nn:
            print("Lose")
        if n=="Q": break