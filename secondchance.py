def findAndUpdate(x,arr,second_chance,frames):
    i=0
    #print(frames)
    for i in range(0,frames):
        if(arr[i]==x):
            second_chance.append(True)
            return True
    else:
        return False

def replaceAndUpdate(x,arr,second_chance,frames,pointer):
    #print(pointer)
    while(True):
        if(not second_chance[pointer]):
            arr[pointer]=x
            return ((pointer+1)%frames)
        second_chance[pointer]=False
        pointer=((pointer+1)%frames)

def printHitsAndFaults(ref_string,frames):
    pointer=0
    i=0
    l=0
    x=0
    pf=0
    arr=[]
    for i in range (0,frames):
        arr.append(-1)
    second_chance=[True for i in range(frames)]
    print(arr)
    #Arrays.fill(arr,-1)
    strdd=[]
    strdd = ref_string.split(" ")
    l=len(strdd)
    for i in range(0,l):
        x=int(strdd[i])
        if(not findAndUpdate(x,arr,second_chance,frames)):
            pointer = replaceAndUpdate(x,arr,second_chance,frames,pointer)
            pf=pf+1
    print("total page faults= "+str(pf)) 


ref_string=""
frames=0
ref_string="0 4 1 4 2 4 3 4 2 4 0 4 1 4 2 4 3 4"
frames = 3
printHitsAndFaults(ref_string,frames)
