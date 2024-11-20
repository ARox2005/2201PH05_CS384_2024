def organizeAnagrams(wordList):
    groupedAnagrams={}
    for term in wordList:
        sortedKey=''.join(sorted(term))
        if sortedKey not in groupedAnagrams:
            groupedAnagrams[sortedKey]=[]
        groupedAnagrams[sortedKey].append(term)
    return groupedAnagrams

def charCount(wordGroup):
    c={}
    for term in wordGroup:
        for letter in term:
            c[letter]=c.get(letter,0)+1
    return c

def frequentGrouo(groups):
    count=0
    result=None
    for key,terms in groups.items():
        c=charCount(terms)
        total=sum(c.values())
        if total>count:
            count=total
            result=(key,terms,c)
    return result

wordList=input("Enter words:").lower().split()
groups=organizeAnagrams(wordList)

for group in groups.values():
    print(group)

key,group,frequency=frequentGrouo(groups)
print(f"group with the highest frequency={group}")
print(f"Character frequency: {frequency}")
