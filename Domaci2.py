recnik={"happy": {"sinonimi": ["delighted","overjoyed","gladdened"],"antonimi":["miserable","unhappy","sorrowful"]},"unearth": {"sinonimi": ["excavate","uncover","grub"],"antonimi":["bury","cover","conceal"]},"kill": {"sinonimi": ["murder","terminate","dispatch"],"antonimi":["revive","reinvigorate","restore"]}}
print("Sinonimi za \"happy\": ",recnik["happy"]["sinonimi"])
print("Antonimi za \"happy\": ",recnik["happy"]["antonimi"])
print("Sinonimi za \"unearth\": ",recnik["unearth"]["sinonimi"])
print("Antonimi za \"unearth\": ",recnik["unearth"]["antonimi"])
print("Sinonimi za \"kill\": ",recnik["kill"]["sinonimi"])
print("Antonimi za \"kill\": ",recnik["kill"]["antonimi"])
print("Treci antonim trece reci: ",recnik["kill"]["antonimi"][2] + "\n")

#Morao sam samo da zamenim č sa c jer sam tako nazvao recnik;

for reč in recnik.keys():
    
    print("Reč: ", reč) 
    sin = "Sinonimi: "
    ant = "Antonimi: "

    for sinonim in recnik[reč]["sinonimi"]:
        sin += sinonim + ", "
    print(sin[:-2])

    for antonim in recnik[reč]["antonimi"]:
        ant += antonim + ", "    
    print(ant[:-2] + "\n")