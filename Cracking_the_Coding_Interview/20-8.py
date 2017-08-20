
storybook = """
A fairy tale is a type of short story that typically features folkloric fantasy characters, such as dwarfs, dragons, elves, fairies, giants, gnomes, goblins, griffins, mermaids, talking animals, trolls, unicorns, or witches, and usually magic or enchantments. Fairy tales may be distinguished from other folk narratives such as legends which generally involve belief in the veracity of the events described and explicitly moral tales, including beast fables. The term is mainly used for stories with origins in European tradition and, at least in recent centuries, mostly relates to children's literature.
In less technical contexts, the term is also used to describe something blessed with unusual happiness, as in fairy tale ending a happy ending or fairy tale romance, though not all fairy tales end happily. Colloquially, a fairy tale or fairy story can also mean any far-fetched story or tall tale; it is used especially of any story that not only is not true, but could not possibly be true. Legends are perceived as real; fairy tales may merge into legends, where the narrative is perceived both by teller and hearers as being grounded in historical truth. However, unlike legends and epics, they usually do not contain more than superficial references to religion and actual places, people, and events; they take place once upon a time rather than in actual times.
Fairy tales are found in oral and in literary form; the name fairy tale was first ascribed to them by Madame d'Aulnoy in the late 17th century. Many of today's fairy tales have evolved from centuries-old stories that have appeared, with variations, in multiple cultures around the world. The history of the fairy tale is particularly difficult to trace because only the literary forms can survive. Still, according to researchers at universities in Durham and Lisbon, such stories may date back thousands of years, some to the Bronze Age more than 6,000 years ago. Fairy tales, and works derived from fairy tales, are still written today.
Folklorists have classified fairy tales in various ways. The Aarne-Thompson classification system and the morphological analysis of Vladimir Propp are among the most notable. Other folklorists have interpreted the tales' significance, but no school has been definitively established for the meaning of the tales.
"""

findstrings = ["in", "story", "tale", "various", "surprise"]

def searchStrings(data, strings):
    count = len(data)
    fcount = len(strings)
    flen = [len(strings[i]) for i in range(fcount)]
    finds = [0 for i in range(fcount)]
    for i in range(count):
        for j in range(len(strings)):
            if (data[i:i+flen[j]] == strings[j]):
                finds[j] += 1
    return finds
    
print(searchStrings(storybook, findstrings))