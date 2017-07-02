l=0
t=0
b=0
sct=set()
c="Juče sam bio u zoo vrtu. Video sam tri lava i bila je tu jedna lavica. Lavica nije imala grivu, jer to imaju samo muški lavovi. Bila je u zoo vrtu i jedna tigrica. Ona je imala jako lepo krzno. Bilo mi je žao što tigrica i lavica ne mogu da se druže, jer mislim da bi se baš lepo slagale pošto su obe mačke."
cT = c.split(" ")

for i in cT:
    i=i.lower()
    i=i.strip(",.")
    sct.add(i)
    if i=="lavica":
        l+=1
    elif i=="tigrica":
        t+=1
                    
print("Broj javljanja reči lavica:", l)
print("Broj javljanja reči tigrica:", t) 
print(len(sct))