from collections import Counter

print("Welcome to the Frequency Analysis App\n")

nonLetters = ["-", ",", ".", "!", "?", ";", ":", "'", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", "\t"]

keyPhrase1 = str(input("\nEnter a word or phrase to count the occurrence of each letter: ")).lower()
for letter in keyPhrase1:
    if letter in nonLetters:
        keyPhrase1 = keyPhrase1.replace(letter, "")

keyPhrase1 = sorted(keyPhrase1)

totalOcurrences = len(keyPhrase1)

letterCount = Counter(keyPhrase1)

print("\nHere is the frequency analysis from key phrase 1:\n")
print("\tLetter\t\tOccurrence\tPecentage")
for key, value in letterCount.items():
    print(f"\t{key}\t\t{value}\t\t{round(((value/totalOcurrences)*100), 2)}%")

orderedLetterCount = letterCount.most_common()

keyPhrase1OrderedLetters = []

print("\nLetters ordered from highest occurrence to lowest:")
for i in orderedLetterCount: 
    keyPhrase1OrderedLetters.append(i[0])
for i in keyPhrase1OrderedLetters:
        print(i, end="")
print("\n")



keyPhrase2 = str(input("\nEnter a word or phrase to count the occurrence of each letter: ")).lower()
for letter in keyPhrase2:
    if letter in nonLetters:
        keyPhrase2 = keyPhrase2.replace(letter, "")

keyPhrase2 = sorted(keyPhrase2)

totalOcurrences2 = len(keyPhrase2)

letterCount2 = Counter(keyPhrase2)

print("\nHere is the frequency analysis from key phrase 1:\n")
print("\tLetter\t\tOccurrence\tPecentage")
for key, value in letterCount2.items():
    print(f"\t{key}\t\t{value}\t\t{round(((value/totalOcurrences2)*100), 2)}%")

orderedLetterCount2 = letterCount2.most_common()

keyPhrase2OrderedLetters = []

print("\nLetters ordered from highest occurrence to lowest:")
for i in orderedLetterCount2: 
    keyPhrase2OrderedLetters.append(i[0])
for i in keyPhrase2OrderedLetters:
        print(i, end="")
print("\n")