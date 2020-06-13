site = input()

index = site.index("/") + 2
index2 = site.index(".")
word = site[int(index):int(index2)]
wordlen = len(word)
enum = 0
for i in site:
    if (i == 'e'):
        enum += 1
print(word[0:3] + str(wordlen) + str(enum) + "!")
