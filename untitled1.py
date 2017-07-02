advCount=0
prilozi = ["ovde", "tamo", "tu", "desno", "negde"]
korpus = "Ovde mi je baš lepo. Džunglu ne volim. Ne bih volela da sam tamo. Moje mesto je tu. Tu se osećam kao da sam kod kuće. Stavila sam svoju šoljicu kafe desno, e baš tu."

tokeniziraniKorpus = korpus.split(" ")

for i in tokeniziraniKorpus:
    # prebacivanje reči u mala slova
    i = i.lower()
    # uklanjanje interpunkcijskih znaka
    i = i.strip(",.")
    if i in prilozi:
        advCount += 1 # brojPriloga = brojPriloga + 1

print(advCount)