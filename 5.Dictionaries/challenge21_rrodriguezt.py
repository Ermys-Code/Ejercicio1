import random

thesaurus = {
    "hot"   :   ["balmy", "summery", "tropical", "boiling", "scorching"], 
    "cold"  :   ["chilly", "cool", "freezing", "frigid", "polar"],
    "happy" :   ["content", "cherry", "merry", "jovial", "jocular"],
    "sad"   :   ["unhappy", "downcast", "miserable", "glum", "melancholy"]
    }

keyList = thesaurus.keys()

print("Welcome to the Thesaurus App\n")

print("Here are the words in the thesaurus:")
for key in thesaurus.keys():
    print(f"\t-{key}")

word = str(input("\nWhat word would you like a synonym for: ")).lower()
if word in thesaurus:
    print(f"A synonym for {word} is {thesaurus[word][random.randint(0, 4)]}")
else:
    print(f"I'm sorry, that word is not currently in the thesaurus.")

showAll = str(input("\nWould you like to see the whole thesaurus (yes/no): ")).lower()
if showAll == "yes":
    for key in thesaurus.keys():
        print(f"\n{key.title()} synonyms are:")
        for value in thesaurus[key]:
            print(f"\t-{value}")
else:
    print("\nI hope you enjoyed the program. Thank you!")