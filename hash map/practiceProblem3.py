wordCount = {}
with open("attached_assets/poem.txt", "r") as f:
    for line in f:
        tokens = line.split(" ")
        # print(line) # This will print each line in poem in a new line
        # print (tokens) # after new para 'wood,\n'
        for token in tokens:
            # print(token) # This prints each word in line in a new line
            token = token.replace("\n", "")
            # token = token.replace("-", "")
            if token in wordCount:
                wordCount[token] += 1
            else:
                wordCount[token] = 1

print(wordCount)
# Printing the dictionary as provided in our course
for words, count in wordCount.items():
    print(f"{words} : {count}")