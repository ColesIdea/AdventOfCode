import math
input = [874324,1096487,6106748,6273465,1751,4283,294380,348021,5217788,5252660,828815656,828846474,66486,157652,477,1035,20185,55252,17,47,375278481,375470130,141,453,33680490,33821359,88845663,88931344,621298,752726,21764551,21780350,58537958,58673847,9983248,10042949,4457,9048,9292891448,9292952618,4382577,4494092,199525,259728,9934981035,9935011120,6738255458,6738272752,8275916,8338174,1,15,68,128,7366340343,7366538971,82803431,82838224,72410788,72501583]

ids = []

inputLen = int(len(input)/2)
 
for x in range(inputLen):
    start = input[x*2]
    stop = input[x*2+1]
    while stop >= start:
        strLenHalv = int(math.ceil(len(str(start))/2))
        if len(str(start))%2 == 0:
            if int(str(start)[:strLenHalv])-int(str(start)[strLenHalv:]) == 0:
                ids.append(start)
                #print(start)
        start += 1
idSum = 0
for x in ids:
    idSum += x
print(f"done: {idSum}")
